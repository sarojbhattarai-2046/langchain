from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="Return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()


llm = OpenAI()


code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=[ "language", "task" ]
)

test_prompt = PromptTemplate(
    input_variables=["language", "code"],
    template="Write a test for the following {language} code; \n{code}"
)

code_chain = LLMChain(
    llm = llm,
    prompt = code_prompt,
    output_key="code" # to override the text output key
)

test_chain = LLMChain(
    llm=llm,
    prompt=test_prompt,
    output_key="test"
)

chain = SequentialChain(
    chains=[code_chain, test_chain],
    input_variables=["task", "language"],
    output_variables=["test", "code"]
)

result = chain({
    "language": args.language,
    "task": args.task
})

print(result["code"])

print(">>>>> GENERATED CODE")

print(result["test"])
