from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="Answer the following question \n{question} from the following text -\n{text}",
    input_variables=['question','text']
)

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

parser = StrOutputParser()

url = "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

while True:
    
    user_input = input("You: ")
    if user_input == "exit":
        break

    result = chain.invoke({'question': user_input, 'text':docs[0].page_content})

    print("AI:",result)



    # embeding and model dimentions are differnt and vector store dimentions 