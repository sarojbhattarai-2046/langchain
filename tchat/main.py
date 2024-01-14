from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts import MessagesPlaceholder,HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory, FileChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

# returnMessage=True will pass message as input with actual fancy object like HumanMessages rather than plain string
# memory_key="message" when we feed input into chain it will flow into memory and memory has the ability to 
# add in some additional keys to input variables. And, the input name that gets added is the memory_key we provide
# and whatever data we have stored is assigned to that key


# ConversationSummaryMemory will have it's own chain, which will feed the input from the user and result received from AI. Then
# the Language model will summarize that information and pass it as SystemMessage in input.

memory = ConversationSummaryMemory(
    # chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages", 
    return_messages=True,
    llm=chat, # since ConversationSummaryMemory it will have it's own language model
)

prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        # tells go and look at input variables and find the key messages and associated data
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
    verbose=True
)

while True:
    content = input(">> ")

    result = chain({ "content": content })

    print(result["text"])