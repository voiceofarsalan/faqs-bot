from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

load_dotenv()
model_name = "models/text-bison-001"  # Choose your desired model size
llm = GoogleGenerativeAI(model=model_name, google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.7)

model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': True}
hf = HuggingFaceEmbeddings(
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs,
)
vectordb_file_path = "faiss_index"


def create_vector_db():
    loader = CSVLoader(file_path="codebasics_faqs.csv", encoding="latin-1", source_column='prompt')
    data = loader.load()
    vectorDB = FAISS.from_documents(documents=data, embedding=hf)
    vectorDB.save_local(vectordb_file_path)


def get_qa_chain():

    vectorDB = FAISS.load_local(vectordb_file_path, hf, allow_dangerous_deserialization=True)

    retriever = vectorDB.as_retriever()

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
        In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
        If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

        CONTEXT: {context}

        QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm = llm,
                                        retriever=retriever,
                                        chain_type="stuff",
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})
    return chain


if __name__ == "__main__":
    #create_vector_db()

    chain = get_qa_chain()

    print(chain("do you provide internship? Do you have EMI option?"))
