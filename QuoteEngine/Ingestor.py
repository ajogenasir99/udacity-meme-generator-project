"""Module for base class to extract data from various files"""
from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .DocXIngestor import DocXIngestor
from .CsvIngestor import CsvIngestor
from .PdfIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor


class Ingestor(IngestorInterface):
    """Base class which supports various file formats and
        will also readily support more file formats in the future"""
    ingestors = [DocXIngestor, CsvIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """iterates over the ingestors and returns the
        parse mthd of valid ingestors"""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
