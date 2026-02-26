from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from app.config import OPENAI_API_KEY
import os
import pickle

class MemoryService:
    def __init__(self, persist_path="memory_store"):
        self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        self.persist_path = persist_path
        self.store = None
        self._load()
        
    def _load(self):
        if os.path.exists(self.persist_path):
            self.store = FAISS.load_local(
                self.persist_path,
                self.embeddings,
                allow_dangerous_deserialization=True
            )

    def _save(self):
        if self.store:
            self.store.save_local(self.persist_path)
        
    def load_or_create(self, documents):
        if self.store is None:
            self.store = FAISS.from_texts(documents, self.embeddings)
        else:
            self.store.add_texts(documents)

        self._save()
        return self.store
    
    def search(self, query, k=4):
        if not self.store:
            return []
        return self.store.similarity_search(query, k=k)