"""PDF File Parsing Module"""
from typing import List
import subprocess
import os
import random

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class PDFIngestor(IngestorInterface):
    """Parses and splits pdf data using subprocess
    and pdftotext"""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ uses subprocess to access pdftotext
        and converts the pdf data to txt
        (using pdftotext) then
        parses data from each line of the txt file
        and creates the body and author of the quote model
        using the parsed data"""

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        temp = f'./temp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, temp])

        quotes = []
        with open(temp, "r") as pdfF:
            for line in pdfF.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0], (parse[1]))
                    quotes.append(new_quote)
        os.remove(temp)
        return quotes
