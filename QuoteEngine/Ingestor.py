from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .DocXIngestor import DocXIngestor
from .CsvIngestor import CsvIngestor
from .PdfIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor


class Ingestor(IngestorInterface):
    ingestors = [DocXIngestor, CsvIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
