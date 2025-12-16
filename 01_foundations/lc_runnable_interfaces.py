from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a joke on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain the following joke \n{text}",
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

parser = StrOutputParser()

joke_gen = prompt1 | model | parser

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination': prompt2 | model| parser
})

final_chain = joke_gen| parallel_chain

result = final_chain.invoke({'topic': "AI"})

print(result['joke'])
print(result['explaination'])