from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

video_id = input("Enter the video_id ") #############  "LPZh9BOjkQs"

def get_transcript(video_id:str):
    api = YouTubeTranscriptApi()
    transcript_list = api.list(video_id)
    for transcript in transcript_list:
            transcript = transcript.fetch()
    return " ".join([i.text for i in transcript.snippets])

def chunk_transcript(transcript:str):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.create_documents([transcript])
    return docs

def embed_docs(docs):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/gemini-embedding-001")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

vector_store = embed_docs(chunk_transcript(get_transcript(video_id)))
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

prompt = PromptTemplate(
    template="""
        You are a helpful assistant.
        Answer in english even if the transcript context is in another language.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
        Question: {question}
        """,
    input_variables=['context', 'question']
)

parallel_chain = RunnableParallel({
        "context": retriever | RunnableLambda(format_docs),
        "question":RunnablePassthrough()
    })

parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

while True:

    question = input("\n\nYou: ")
    if question == "exit":
        break

    print("\n\nAI:", main_chain.invoke(question))