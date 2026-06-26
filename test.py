from langchain_community.llms import Ollama # type: ignore

llm = Ollama(model="llama3.2")

print(llm.invoke("Say hello"))