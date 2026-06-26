from langchain_community.llms import Ollama # type: ignore

llm = Ollama(
    model="llama3.2"
)


def ask_llm(question, context):

    prompt = f"""
    You are a CSV Data Analyst.

    Context:
    {context}

    Answer only using context.

    Question:
    {question}
    """

    return llm.invoke(prompt)