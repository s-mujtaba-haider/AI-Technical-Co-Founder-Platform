from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from app.config import OPENAI_API_KEY

class MemoryService:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        self.store = None
        
    def load_or_create(self, documents):
        if self.store is None:
            self.store = FAISS.from_texts(documents, self.embeddings)
        else:
            self.store.add_texts(documents)

        return self.store
    
    def search(self, query, k=4):
        if not self.store:
            return []
        return self.store.similarity_search(query, k=k)