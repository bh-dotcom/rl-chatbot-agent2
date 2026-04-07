from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
state = {"last_message": ""}

class Message(BaseModel):
    text: str

@app.get("/state")
def get_state():
    return state

@app.post("/reset")
def reset():
    state["last_message"] = ""
    return {"status": "reset"}

@app.post("/chat")
def chat(msg: Message):
    state["last_message"] = msg.text
    reply = f"Bot says: {msg.text[::-1]}"
    return {"reply": reply}
