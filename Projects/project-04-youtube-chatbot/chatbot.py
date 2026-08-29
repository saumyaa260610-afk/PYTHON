from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings,HuggingFacePipeline
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from transformers import pipeline
from langchain_core.runnables import RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def get_video_id(url):
    return url.split("v=")[1]
youtube_url=input("Enter YouTube URL: ")
video_id=get_video_id(youtube_url)
#indexing
try:
    api=YouTubeTranscriptApi()
    transcript_list=api.fetch(video_id,languages=["en"])
    transcript=" ".join(snippet.text for snippet in transcript_list)
except TranscriptsDisabled:
    print("No captions available for this video.")
splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
chunks=splitter.create_documents([transcript])
embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_Store=FAISS.from_documents(chunks,embedding)
#chain
prompt=PromptTemplate(template="""
    Answer only from the provided transcript context.
    If the context is insufficient,just say you don't know.
    {context}
    Question: {question}""",
    input_variables=["context", "question"])
retriever=vector_Store.as_retriever(search_type="similarity",search_kwargs={"k":1})
llm=HuggingFacePipeline.from_model_id(model_id="Qwen/Qwen2.5-0.5B-Instruct",task="text-generation")

parallel_chain=RunnableParallel({"context":retriever,"question":RunnablePassthrough()})
parser=StrOutputParser()
main_chain=parallel_chain|prompt|llm|parser
response=main_chain.invoke("Give a summary of the video")
print(response)
