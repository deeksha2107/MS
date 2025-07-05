import langchain
#from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Load PDF document
loader = PyPDFLoader("docs/Deeksha_Hareesha_Kulal_Resume_ML.pdf")  
documents = loader.load()

# Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Create embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Store in Chroma (creating a new DB)
persist_directory = "docs/chroma/"
vectordb = Chroma.from_documents(docs, embedding=embedding, persist_directory=persist_directory)

# Initialize LLM
llm = ChatOllama(model="llama3", temperature=0.0)
template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
{context}
Question: {question}
Helpful Answer:"""
QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)
while(True):
    user_input = input("Do you have a question? Yes or No:")
    if(user_input == 'Yes'):
        user_question = input("Enter your question: ")
        docs = vectordb.max_marginal_relevance_search(user_question, k=2, fetch_k = 3)

        # Setup the RetrievalQA chain
        qa_chain = RetrievalQA.from_chain_type(llm,
                                            retriever=vectordb.as_retriever(),
                                            return_source_documents=True,
                                            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})

        # Invoke the chain with the user's question
        result = qa_chain.invoke({"query": user_question})

        # Print the final answer
        print("\nAnswer:")
        print(result["result"])
    else:
        print("Thank you!")
        break
