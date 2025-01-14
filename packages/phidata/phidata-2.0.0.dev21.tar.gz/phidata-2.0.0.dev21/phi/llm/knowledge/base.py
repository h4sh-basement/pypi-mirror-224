from typing import List, Optional, Iterator

from pydantic import BaseModel, ConfigDict

from phi.document import Document
from phi.document.reader.base import Reader
from phi.vectordb import VectorDb
from phi.utils.log import logger


class LLMKnowledgeBase(BaseModel):
    """Base class for LLM knowledge base"""

    # Reader to read the documents
    reader: Optional[Reader] = None
    # Vector db to store the knowledge base
    vector_db: Optional[VectorDb] = None
    # Number of relevant documents to return on search
    relevant_documents: int = 5
    # Number of documents to optimize the vector db on
    optimize_on: int = 1000

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @property
    def document_lists(self) -> Iterator[List[Document]]:
        """Iterator that yields lists of documents in the knowledge base
        Each object yielded by the iterator is a list of documents.
        """
        raise NotImplementedError

    def search(self, query: str, relevant_documents: Optional[int] = None) -> List[Document]:
        """Returns relevant documents matching the query"""

        if self.vector_db is None:
            logger.warning("No vector db provided")
            return []

        _num_documents = relevant_documents or self.relevant_documents
        logger.debug(f"Getting {_num_documents} relevant documents for query: {query}")
        return self.vector_db.search(query=query, relevant_documents=_num_documents)

    def load(self, recreate: bool = False) -> None:
        """Load the knowledge base to vector db

        TODO: Use upsert instead of insert
        """

        if self.vector_db is None:
            logger.warning("No vector db provided")
            return

        if recreate:
            logger.debug("Deleting collection")
            self.vector_db.delete()

        logger.debug("Creating collection")
        self.vector_db.create()

        logger.info("Loading knowledge base")
        num_documents = 0

        for document_list in self.document_lists:
            # Filter out documents which already exist in the vector db
            if not recreate:
                document_list = [document for document in document_list if self.vector_db.doc_exists(document)]

            self.vector_db.insert(documents=document_list)
            num_documents += len(document_list)
        logger.info(f"Loaded {num_documents} documents to knowledge base")

        if num_documents > self.optimize_on:
            logger.debug("Optimizing Vector DB")
            self.vector_db.optimize()

    def exists(self) -> bool:
        """Returns True if the knowledge base exists"""
        if self.vector_db is None:
            logger.warning("No vector db provided")
            return False
        return self.vector_db.exists()
