from fastapi import ( # type: ignore
    FastAPI,
    UploadFile,
    File
)

from fastapi.middleware.cors import CORSMiddleware # type: ignore

from csv_loader import (
    save_csv,
    load_csv
)

from vector_store import (
    create_vector_db,
    load_vector_db
)

from chat_engine import (
    ask_llm
)

from insights import (
    generate_insights
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

current_df = None


@app.post("/upload")
async def upload_csv(
    file: UploadFile = File(...)
):

    global current_df

    path = save_csv(file)

    current_df = load_csv(path)

    create_vector_db(current_df)

    return {
        "message": "CSV uploaded",
        "rows": current_df.shape[0]
    }


@app.get("/insights")
def insights():

    return {
        "insights":
        generate_insights(
            current_df
        )
    }


@app.post("/chat")
async def chat(
    data: dict
):

    question = data["question"]

    db = load_vector_db()

    docs = db.similarity_search(
        question,
        k=5
    )

    context = "\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    answer = ask_llm(
        question,
        context
    )

    return {
        "answer": answer
    }