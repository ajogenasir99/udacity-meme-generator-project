"""Module for creating Abstact base class with
class and abstract methods needed for parsing file data"""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class with class and abstract method."""
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """gets file extention and validates it."""
        fileTyp = path.split('.')[-1]
        return fileTyp in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ creates abstract method for parsing files"""
        pass
