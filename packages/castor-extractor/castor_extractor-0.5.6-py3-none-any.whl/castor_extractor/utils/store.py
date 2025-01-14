import os
from abc import ABC, abstractmethod
from io import StringIO
from typing import Iterable, Iterator, Optional

from .formatter import CsvFormatter, Formatter
from .time import current_timestamp
from .write import timestamped_filename


class AbstractStorage(ABC):
    """Abstract class to store warehouse assets"""

    @abstractmethod
    def path(self, name: str) -> str:
        """builds the path associated to the given name (it doesn't necessarily exist)"""
        pass

    @abstractmethod
    def exists(self, name: str) -> bool:
        """checks file existence"""
        pass

    @abstractmethod
    def put(self, name: str, data: Iterable[dict]) -> str:
        """put the given data in the storage and returns its path"""
        pass

    @abstractmethod
    def get(self, name: str) -> Iterable[dict]:
        """read data"""
        pass


class LocalStorage(AbstractStorage):
    """Store assets in local file system"""

    def __init__(
        self,
        directory: str,
        formatter: Optional[Formatter] = None,
        with_timestamp: bool = True,
    ):
        self._directory = directory
        self._formatter = CsvFormatter() if formatter is None else formatter
        self.stored_at_ts = current_timestamp()
        self._with_timestamp = with_timestamp

    def path(self, name: str) -> str:
        filename = f"{name}.{self._formatter.extension()}"
        if self._with_timestamp:
            filename = timestamped_filename(filename, self.stored_at_ts)
        return os.path.join(
            self._directory,
            filename,
        )

    def exists(self, name: str) -> bool:
        path = self.path(name)
        return os.path.isfile(path)

    def put(self, name: str, data: Iterable[dict]) -> str:
        path = self.path(name)
        with open(path, "w") as file:
            self._formatter.serialize(file, data)
        return path

    def get(self, name: str) -> Iterator[dict]:
        path = self.path(name)
        with open(path, "r") as file:
            return self._formatter.deserialize(StringIO(file.read()))
