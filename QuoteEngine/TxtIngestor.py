"""Txt File Parsing Module"""
from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TxtIngestor(IngestorInterface):
    """Parses and splits txt data"""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parses data from each line of the txt
        file and creates the body and author of
        the quote model using the parsed data"""

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, "r") as txtF:
            for line in txtF.readlines():
                line = line.strip()
                if len(line) > 0:
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0], (parse[1]))
                    quotes.append(new_quote)
        return quotes
