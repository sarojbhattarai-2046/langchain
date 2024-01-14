from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
import langchain
# A retriever is an object that can take in a string and return some relevant documents
# To be retriever, the object must have a method called "get_relevant_documents" that takes a string and returns a list of documents.
# 
# it will automatically create the chain we could do manually as well
# it provides the context pass it to llm, pass the system message everything on our behalf
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

langchain.debug = True

load_dotenv()

chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()

db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

# it returns a object with a method get_relevant_documents which then call the chroma's similarity_search(string) function
retriever = db.as_retriever()


chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff", # map_reduce, map_rerank, refine
)
      

result = chain.run("What is an interesting fact about English language?")