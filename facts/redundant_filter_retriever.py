from langchain.embeddings.base import Embeddings
from langchian.vectorstores import Chroma
from langchain.schema import BaseRetriever

class RedundantFilterRetriever(BaseRetriever):
    def get_relevant_documents(self, query):
        # calculate embeddings for the 'query' string

        # take embeddings and feed them into that
        # max_marginal_relevance_search_by_vector
        return []
    
    async def aget_relevant_documents(self):
        return []
