from typing import List
import docx

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class DocXIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for paragraph in doc.paragraphs:
            if paragraph.text != "":
                parse = paragraph.text.split('-')
                new_quote = QuoteModel(parse[0], (parse[1]))
                quotes.append(new_quote)

        return quotes
