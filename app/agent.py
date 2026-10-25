from google import genai

from app.config import GEMINI_API_KEY

ai_agent = genai.Client(api_key=GEMINI_API_KEY)







async def generate_response(message:str)->str:
   message = message.lower()
   
   response = ai_agent.models.generate_content(
       model='gemini-3.8-flash',
       contents=message
   )
   
   return response.text