from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

# emb = embeddings.embed_query("hi there")

# print(emb)

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200, # no of character it should hold
    chunk_overlap=0, # add last 0 characters from prev chunks
)

loader = TextLoader("facts.txt")
docs = loader.load_and_split(
    text_splitter=text_splitter
)

# vector store
db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="emb"
)

# for doc in docs:
#     print(doc.page_content)
#     print("\n")


# use similarity_search if you don't want the score
results = db.similarity_search_with_score(
    "what is an interesting facts about English language?",
    k=2
)


for result in results:
    print("\n")
    print(result[1])
    print(result[0].page_content)