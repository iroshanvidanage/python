import streamlit as st
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

st.header("RAG Chatbot")

with st.sidebar:
    st.title("Uploads")
    file = st.file_uploader("Upload a pdf file", type=["pdf", "txt", "docx"])


# Extract content from the uploaded file

if file is not None:
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    # st.write(text)

    # split it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n", "\n\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=20
    )
    chunks = text_splitter.split_text(text)
    # st.write(chunks)

    # generate embeddings for the chunks
    embeddings = OpenAIEmbeddings(
        model = "text-embedding-3-small",
        openai_api_key = OPENAI_API_KEY,

    )

    # store embeddings
    vector_store = FAISS.from_texts(chunks, embeddings)

    # get user query
    user_query = st.text_input("Ask a query about the document:")
    
    # retrieve relevant chunks from the vector store -> generate answers using LLM
    # question -> embeddings -> vector_store -> similarity search -> relevant chunks -> LLM -> generate answer (CHAIN)

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])
    
    # retriever settings
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 3}
    )

    # llm settings
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3, # randomness of the output 0, 1, 2, 0.1, 0.2
        max_tokens=1000,
        openai_api_key=OPENAI_API_KEY
    )

    # prompts
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are a helpful assistant that answers questions based on the provided document.\n\n"
         "Guidelines:\n"
         "1. Provide complete, well-explained answers using the context below.\n"
         "2. Include relevant details, numbers, and explanations to give a thorough response.\n"
         "3. If the context mentions related information, include it to give a comprehensive answer.\n"
         "4. Only use information from the provided context - do not use outside knowledge.\n"
         "5. Summarize long information, ideally in bullets where needed, but ensure the answer is complete and clear.\n"
         "6. If the answer is not found in the context, respond with 'I could not find an answer to your question in the provided document.'\n\n"
         "Context:\n{context}"),
        ("human", "{question}")
    ])

    # if user_query:
        # relevant_chunks = vector_store.similarity_search(user_query, k=3)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough() }
        | prompt
        | llm
        | StrOutputParser()
    )

    response = chain.invoke(user_query)
    st.write(response)
