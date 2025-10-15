from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from appointment_module import book_appointment
import os
from tts_module import tts_speak
import re

os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant")

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
    print("AI Response:", text)
    tts_speak(text)


    if "book" in text.lower():
        book_appointment(name="Customer", date="2025-10-15", time="17:00")
        text += " Your appointment has been booked!"

    return text
