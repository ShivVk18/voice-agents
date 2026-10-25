from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import generate_response
from app.recorder import record_audio
from app.speech import transcribe_audio
from app.tts import speak

app = FastAPI()


class AgentRequest(BaseModel):
    message:str


@app.post("/record")
async def record():

    file_path = record_audio()

    text = transcribe_audio(file_path)

    response = await generate_response(text)
    
    speak(response)

    return {
        "user": text,
        "assistant": response
    }



@app.post('/agent')
async def agent_message(req:AgentRequest):
      response = await generate_response(req.message)
      
      return {
          "user":req.message,
          "agent":response
      }
    


@app.get('/health')
async def root(): 
    return {
        "message": "Voice Agent is running!"
    }