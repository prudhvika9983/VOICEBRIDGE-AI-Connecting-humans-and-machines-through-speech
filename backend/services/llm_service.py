import google.generativeai as genai

# Replace with your actual Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-flash')

def get_llm_response(prompt):
    try:
        if not prompt:
            return "System standby. Please provide voice input."
        
        response = model.generate_content(f"You are a machine interface. Briefly respond to: {prompt}")
        return response.text
    except Exception as e:
        print(f"LLM Error: {e}")
        return "Connection to core brain interrupted."