import uvicorn
import google.generativeai as genai
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Crucial: This allows your index.html to communicate with this Python server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Replace with your actual Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        user_text = data.get("text", "")
        
        if not user_text:
            return {"reply": "I am waiting for your voice signal."}

        # Human-Machine Interface Logic
        response = model.generate_content(f"Respond concisely as a machine interface to: {user_text}")
        ai_reply = response.text
        
        return {"reply": ai_reply}
    except Exception as e:
        print(f"Error: {e}")
        return {"reply": "System link failure. Please check backend."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)