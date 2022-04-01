"""Csv File Parsing Module."""
from typing import List
import pandas

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CsvIngestor(IngestorInterface):
    """Parses and splits Csv data using pandas."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse data from each row of the csv file.

        Creates the body and author of the quote model using parsed data.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
