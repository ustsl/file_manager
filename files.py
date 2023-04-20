from abc import ABC
import os


class FileManager(ABC):
    def __init__(self, path, file):
        self.path = path
        self.file = file
        self._f = None

    def _open_file(self):
        self._f = open(os.path.join(self.path, self.file), "r")

    def _close_file(self):
        if self._f is not None:
            self._f.close()


class FilesManager(ABC):
    def __init__(self):
        self._path = None

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
