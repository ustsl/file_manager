import os
import yaml
import json

from .files import FileManager, FilesManager


class OpenFile(FileManager):
    def open_yaml(self):
        self._open_file()
        try:
            data = yaml.safe_load(self._f)
        finally:
            self._close_file()
        return data

    def open_json(self):
        self._open_file()
        try:
            data = json.load(self._f)
        finally:
            self._close_file()
        return data


class OpenFiles(FilesManager):
    def __init__(self):
        super().__init__()
        self._files = None

    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        self._files = value

    def filelist(self):
        try:
            self.files = os.listdir(self.path)
        except FileNotFoundError:
            print("Папка не найдена")


class SaveFile(FilesManager):
    def save(self, file_name, file):
        with open(os.path.join(self.path, file_name), "w") as f:
            f.write(file)
