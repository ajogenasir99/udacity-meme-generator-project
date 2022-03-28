from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TxtIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
