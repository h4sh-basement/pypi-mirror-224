"""Loads Roam directory dump."""
from pathlib import Path
from typing import List

from oplangchain.docstore.document import Document
from oplangchain.document_loaders.base import BaseLoader


class RoamLoader(BaseLoader):
    """Loads Roam files from disk."""

    def __init__(self, path: str):
        """Initialize with a path."""
        self.file_path = path

    def load(self) -> List[Document]:
        """Load documents."""
        ps = list(Path(self.file_path).glob("**/*.md"))
        docs = []
        for p in ps:
            with open(p) as f:
                text = f.read()
            metadata = {"source": str(p)}
            docs.append(Document(page_content=text, metadata=metadata))
        return docs
