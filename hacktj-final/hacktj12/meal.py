import openai
import guidance
from guidance import system, user, assistant, models, gen
from openai import OpenAI
import re

client = OpenAI()

gpt35 = models.OpenAI('gpt-4o-mini')

def generate_response(text, question):
    llm = gpt35

    with system():
        llm += "You are an intelligent assistant."

    with user():
        llm += f"{question}\nText: {text}\n"

    with assistant():
        #llm += f'Answer: {gen("answer")}'
        response = gen("Answer: {answer}", max_tokens=5000)
        llm += response
    
    return llm

def ask_openai(conversation_history):
    response = client.chat.completions.create(
        messages=conversation_history,
        model="gpt-3.5-turbo",
        temperature=0,
    )
    return response.choices[0].message.content

def chatbot(text, response):
    conversation_history = [
        {'role': 'system', 'content':f'You will answer questions about {text} and {response}. Respond in structured, bulleted format with headings as needed.'}
    ]

    while True:
        query = input("Query: ")
        conversation_history.append({'role': 'user', 'content': query})
        answer = ask_openai(conversation_history)
        print(f"Answer: {answer}")
        conversation_history.append({'role': 'assistant', 'content': answer})


#REPORT CARD COMMENTS
def meal_plan(form_data):
    diabetes = form_data["Diabetes"] 
    lactose = form_data["Lactose"]
    calcium = form_data["Calcium"]
    ethnicity = form_data["Ethnicity"]
    special = form_data["Special Requests"]

    text = f"""
    risk of diabetes: {diabetes}
    lactose intolerance (y/n): {lactose}
    calcium intake: {calcium}
    intensity of liver cirrhosis: {"HIGH"} 
    ethnicity (for food recommendations): {ethnicity}
    additional special recommendations: {special}
    """

    question = "Based on the text above, create a detailed, personalized meal plan for a patient. Include quantifiable percentages for each macronutrients."
    response = str(generate_response(text, question))
    first_index = response.rfind("<|im_start|>") + 22
    last_index = response.rfind("<|im_end|>")
    return {'output' : str(response[int(first_index): int(last_index)])}

form_data = {"Diabetes": "High", "Lactose": "Yes", "Calcium": "Severely Low", "Ethnicity": "Indian", "Special Requests": "No nuts"}
print(meal_plan(form_data))
