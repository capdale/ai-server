import abc
from typing import Any

class ModelBox(abc.ABC):
    """Interface for end-to-end pipe"""
    @abc.abstractmethod
    def input(self) -> Any:
        """Take input values and return output"""
        pass