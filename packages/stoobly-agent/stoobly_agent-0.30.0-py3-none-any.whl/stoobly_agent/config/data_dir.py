import os
import shutil

from stoobly_agent.config.constants.env_vars import ENV

class DataDir:
    DATA_DIR_NAME = '.stoobly'
    DB_FILE_NAME = 'stoobly_agent.sqlite3'
    DB_VERSION_NAME = 'VERSION'

    _instance = None

    def __init__(self):
        if DataDir._instance:
            raise RuntimeError('Call instance() instead')
        else:
            cwd = os.getcwd()
            self.__data_dir_path = os.path.join(cwd, self.DATA_DIR_NAME)

            # If the current working directory does not contain a .stoobly folder,
            # then search in the parent directories until the home directory.
            if not os.path.exists(self.__data_dir_path):
                data_dir = self.find_data_dir(cwd)

                if not data_dir:
                    self.__data_dir_path = os.path.join(os.path.expanduser('~'), self.DATA_DIR_NAME)
                else:
                    self.__data_dir_path = data_dir

            if not os.path.exists(self.__data_dir_path):
                os.makedirs(self.__data_dir_path, exist_ok=True)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    @property
    def path(self):
        if os.environ.get(ENV) == 'test':
            test_path = os.path.join(self.__data_dir_path, 'tmp', self.DATA_DIR_NAME)

            if not os.path.exists(test_path):
                os.makedirs(test_path, exist_ok=True)

            return test_path

        return self.__data_dir_path

    @property
    def tmp_dir_path(self):
        tmp_dir_path = os.path.join(self.path, 'tmp')

        if not os.path.exists(tmp_dir_path):
            os.mkdir(tmp_dir_path)

        return tmp_dir_path

    @property
    def db_dir_path(self):
        db_dir_path = os.path.join(self.path, 'db')

        if not os.path.exists(db_dir_path):
            os.mkdir(db_dir_path)

        return db_dir_path

    @property
    def db_file_path(self):
        return os.path.join(self.db_dir_path, self.DB_FILE_NAME)

    @property
    def db_version_path(self):
        return os.path.join(self.db_dir_path, self.DB_VERSION_NAME)

    @property
    def settings_file_path(self):
        return os.path.join(self.path, 'settings.yml')

    @property
    def snapshots_dir_path(self):
        snapshots_dir_path = os.path.join(self.path, 'snapshots')

        if not os.path.exists(snapshots_dir_path):
            os.mkdir(snapshots_dir_path)

        return snapshots_dir_path

    @property
    def snapshots_requests_dir_path(self):
        base_path = self.snapshots_dir_path
        requests_dir_path = os.path.join(base_path, 'requests')

        if not os.path.exists(requests_dir_path):
            os.mkdir(requests_dir_path)

        return requests_dir_path

    @property
    def snapshots_scenarios_dir_path(self):
        base_path = self.snapshots_dir_path
        scenarios_dir_path = os.path.join(base_path, 'scenarios')

        if not os.path.exists(scenarios_dir_path):
            os.mkdir(scenarios_dir_path)

        return scenarios_dir_path

    @property
    def snapshots_scenario_requests_dir_path(self):
        base_path = self.snapshots_scenarios_dir_path
        requests_dir_path = os.path.join(base_path, 'requests')

        if not os.path.exists(requests_dir_path):
            os.mkdir(requests_dir_path)

        return requests_dir_path

    @property
    def snapshosts_version_path(self):
        return os.path.join(self.snapshots_dir_path, 'VERSION')

    def remove(self):
        if os.path.exists(self.path):
            shutil.rmtree(self.path) 

    def create(self, directory_path = None):
        if not directory_path:
            directory_path = os.getcwd()

        self.__data_dir_path = os.path.join(directory_path, self.DATA_DIR_NAME)

        if not os.path.exists(self.__data_dir_path):
            os.mkdir(self.__data_dir_path)

    def find_data_dir(self, start_path: str) -> str:
        # Note: these paths won't work for Windows
        root_dir = os.path.abspath(os.sep)
        home_dir = os.path.expanduser("~")

        while start_path != home_dir:
            if start_path == root_dir:
                start_path = home_dir

            data_dir_path = os.path.join(start_path, self.DATA_DIR_NAME)

            if os.path.exists(data_dir_path):
                return data_dir_path

            start_path = os.path.dirname(start_path)

        return ""

