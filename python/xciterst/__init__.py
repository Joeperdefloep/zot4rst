import re

class CitationInfo(object):
    """Class to hold information about a citation for passing to citeproc."""
    def __init__(self, **kwargs):
        self.key = kwargs.get('key')
        self.label = kwargs.get('label', None)
        self.locator = kwargs.get('locator', None)
        self.suppress_author = kwargs.get('suppress_author', False)
        self.prefix = kwargs.get('prefix', None)
        if self.prefix:
            self.prefix = re.sub(r'\s+,', ',', self.prefix)
        self.suffix = kwargs.get('suffix', None)
        if self.suffix:
            self.suffix = re.sub(r'\s+,', ',', self.suffix)
        self.author_only = kwargs.get('author_only', False)
        self.id = None
