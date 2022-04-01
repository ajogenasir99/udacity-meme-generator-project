"""Module for creating Quotes with a body and author."""


class QuoteModel():
    """A Quote.

    A Quote encapsulates the body(content) of the quote and the author.
    """

    def __init__(self, body, author):
        """Create a new Quote.

        :param body: a str text containing the content of the quote.
        :param author: a str text containing the quotes author.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return human readable string representation.

        using the class attributes.
        """
        return f"{self.body}, {self.author}"

    def __repr__(self):
        """Return `repr(self)`.

        a computer-readable string representation of this object.
        """
        return f'<{self.body}, {self.author}>'
