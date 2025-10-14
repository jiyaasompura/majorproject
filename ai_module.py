from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from appointment_module import book_appointment
import os

os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"

model = ChatOpenAI(model="gpt-4o-mini")

prompt_template = """
You are an AI receptionist for a dental clinic.
Extract intent (book, cancel, query) and entities (name, service, date, time).
If intent is booking, return confirmation message.
User: {user_input}
AI:
"""

prompt = ChatPromptTemplate.from_template(prompt_template)

def get_ai_response(user_input):
    response = model.invoke(prompt.format_messages(user_input=user_input))
    text = response.content
    
    # Simple entity detection (can improve with NLP parsing)
    if "book" in text.lower():
        # Example default name/date/time extraction
        book_appointment(name="Customer", date="2025-10-15", time="17:00")
        text += " Your appointment has been booked!"
    
    return text
