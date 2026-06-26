from langchain_core.documents import Document # type: ignore

from langchain_community.vectorstores import FAISS # type: ignore

from langchain_community.embeddings import HuggingFaceEmbeddings # type: ignore

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def dataframe_to_docs(df):
    docs = []

    for _, row in df.iterrows():
        text = ", ".join(
            [f"{col}: {row[col]}" for col in df.columns]
        )

        docs.append(
            Document(page_content=text)
        )

    return docs


def create_vector_db(df):
    docs = dataframe_to_docs(df)

    db = FAISS.from_documents(
        docs,
        embedding
    )

    db.save_local("vector_db")

    return db


def load_vector_db():
    return FAISS.load_local(
        "vector_db",
        embedding,
        allow_dangerous_deserialization=True
    )