"""Loads local airbyte json files."""
import json
from typing import List

from oplangchain.docstore.document import Document
from oplangchain.document_loaders.base import BaseLoader
from oplangchain.utils import stringify_dict


class AirbyteJSONLoader(BaseLoader):
    """Loads local airbyte json files."""

    def __init__(self, file_path: str):
        """Initialize with a file path. This should start with '/tmp/airbyte_local/'."""
        self.file_path = file_path
        """Path to the directory containing the json files."""

    def load(self) -> List[Document]:
        text = ""
        for line in open(self.file_path, "r"):
            data = json.loads(line)["_airbyte_data"]
            text += stringify_dict(data)
        metadata = {"source": self.file_path}
        return [Document(page_content=text, metadata=metadata)]
