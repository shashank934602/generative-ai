import sys
sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

# model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

model = init_chat_model("groq:openai/gpt-oss-120b")

response = model.invoke("wite a poem on cricket")

print(response.text)
