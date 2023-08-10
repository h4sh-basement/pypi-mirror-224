import os
import time
from typing import Optional

import fire
from watchdog.observers import Observer

from rocket.logger import logger
from rocket.utils import execute_shell_command, extract_project_name_from_wheel, \
    extract_python_package_dirs, extract_python_files_from_folder, execute_for_each_multithreaded
from rocket.watcher import Watcher


def _add_index_urls_to_cmd(cmd, index_urls):
    if index_urls:
        return f"{' '.join(index_urls)} {cmd}"
    else:
        return cmd


class Rocket:
    """Entry point of the installed program, all public methods are options of the program"""

    # in seconds
    _interval_repeat_watch: int = 2
    _python_executable: str = "python3"
    _rocket_executable: str = "rocket"

    def setup(self):
        """
        Initialize the application.
        """
        if os.path.exists("setup.py") or os.path.exists(f"pyproject.toml"):
            logger.info("Packaing file already exists so no need to create a new one")
            return

        content = """
import setuptools

setuptools.setup(
    name="myproject",
    version="0.0.1",
    author="",
    author_email="",
    description="",
    url="https://github.com/getyourguide/databricks-rocket",
    packages=setuptools.find_packages(),
)
        """

        with open("setup.py", "a") as myfile:
            myfile.write(content)
        logger.info("Setup.py file created, feel free to modify it with your needs.")

    def launch(
            self,
            project_location: str = ".",
            dbfs_path: Optional[str] = None,
            watch=True,
            _deploy=True,
    ):
        """
        Entrypoint of the application, triggers a build and deploy
        :param project_location:
        :param dbfs_path: path where the wheel will be stored, ex: dbfs:/tmp/myteam/myproject
        :param watch: Set to false if you don't want to automatically sync your files
        :return:
        """

        if os.getenv("DATABRICKS_TOKEN") is None:
            raise Exception("DATABRICKS_TOKEN must be set for db-rocket to work")

        if not dbfs_path:
            dbfs_path = f"dbfs:/temp/{os.environ['USER']}"

        self.project_location = project_location
        project_directory = os.path.dirname(project_location)
        project_directory = project_directory[:-1]

        self.dbfs_folder = dbfs_path + project_directory

        if _deploy:
            self._build_and_deploy(watch)

        if watch:
            observer = Observer()
            watcher = Watcher(observer)
            observer.schedule(watcher, project_location, recursive=True)
            observer.start()
            try:
                time.sleep(2)
            finally:
                observer.stop()
            observer.join()
            if watcher.modified_files:
                self._deploy(watch=watch, modified_files=watcher.modified_files)
            return self.launch(project_location=project_location, dbfs_path=dbfs_path, watch=True, _deploy=False)

    def _build_and_deploy(self, watch, modified_files=None):
        self._build()
        result = self._deploy(watch=watch, modified_files=modified_files)
        return result

    def _deploy(self, watch, modified_files):
        """
        Copies the built library to dbfs
        """

        try:
            if modified_files:
                logger.info(f"Found changes in {modified_files}. Overwriting them.")
                for file in modified_files:
                    logger.info(f"Sync {file}")
                    execute_shell_command(
                        f"databricks fs cp --recursive --overwrite {file} {self.dbfs_folder}/{os.path.relpath(file, self.project_location)}"
                    )
            else:
                execute_shell_command(
                    f"databricks fs cp --overwrite {self.wheel_path} {self.dbfs_folder}/{self.wheel_file}"
                )
                if watch:
                    package_dirs = extract_python_package_dirs(self.project_location)
                    for package_dir in package_dirs:
                        python_files = extract_python_files_from_folder(package_dir)

                        def helper(file):
                            execute_shell_command(
                                f"databricks fs cp --recursive --overwrite {file} {self.dbfs_folder}/{os.path.relpath(file, self.project_location)}"
                            )
                            logger.info(f"Sync {file}")
                        execute_for_each_multithreaded(python_files, helper)
        except Exception as e:
            raise Exception(
                f"Error while copying files to databricks, is your databricks token set and valid? Try to generate a new token and update existing one with `databricks configure --token`. Error details: {e}"
            )

        base_path = self.dbfs_folder.replace("dbfs:/", "/dbfs/")
        install_cmd = f'{base_path}/{self.wheel_file}'
        install_cmd = _add_index_urls_to_cmd(install_cmd, self.index_urls)
        project_name = extract_project_name_from_wheel(self.wheel_file)

        if modified_files:
            logger.info("Changes are applied")
        elif watch:
            logger.info(
                f"""You have watch activated. Your project will be automatically synchronised with databricks. Add following in one cell:
%pip install --upgrade pip
%pip install {install_cmd} --force-reinstall
%pip uninstall -y {project_name}

and then in new Python cell:
%load_ext autoreload
%autoreload 2
import sys
import os
sys.path.append(os.path.abspath('{base_path}')""")
        else:
            logger.info(f"""Install your library in your databricks notebook by running:
    %pip install --upgrade pip
    %pip install {install_cmd} --force-reinstall""")

    def _build(self):
        """
        builds a library with that project
        """
        logger.info("We are now building your Python repo as a library...")

        # cleans up dist folder from previous build
        dist_location = f"{self.project_location}/dist"
        execute_shell_command(f"rm {dist_location}/* 2>/dev/null || true")

        if os.path.exists(f"{self.project_location}/setup.py"):
            logger.info("Found setup.py. Building python library")
            execute_shell_command(
                f"cd {self.project_location} ; {self._python_executable} -m build --outdir {dist_location} 2>/dev/null"
            )
            self.index_urls = []
            if os.path.exists(f"{self.project_location}/requirements.txt"):
                with open(f"{self.project_location}/requirements.txt") as f:
                    self.index_urls = [line.strip() for line in f.readlines() if "index-url" in line]

        elif os.path.exists(f"{self.project_location}/pyproject.toml"):
            logger.info("Found pyproject.toml. Building python library with poetry")
            execute_shell_command(f"cd {self.project_location} ; poetry build --format wheel")
            requirements = execute_shell_command(
                f"cd {self.project_location} ; poetry export --with-credentials --without-hashes")
            self.index_urls = [line.strip() for line in requirements.split("\n") if "index-url" in line]
        else:
            raise Exception(
                "To be turned into a library your project has to contain a setup.py or pyproject.toml file"
            )

        self.wheel_file = execute_shell_command(
            f"cd {dist_location}; ls *.whl 2>/dev/null | head -n 1"
        ).replace("\n", "")
        self.wheel_path = f"{dist_location}/{self.wheel_file}"
        logger.debug(f"Build Successful. Wheel: '{self.wheel_path}' ")


def main():
    fire.Fire(Rocket)
