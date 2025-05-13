from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# Load your API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 🧠 Define LLM
llm = ChatOpenAI(model="gpt-4o")

# 📝 Prompt Template
diet_prompt = PromptTemplate(
    input_variables=["age", "weight"],
    template="""
    You are a professional dietitian. Create a personalized, healthy 1-day diet plan 
    for a person who is {age} years old and weighs {weight} kg.
    
    Include:
    - Breakfast
    - Mid-morning snack
    - Lunch
    - Evening snack
    - Dinner

    Make sure it's balanced and culturally neutral.
    """
)

# 🔗 Chain
diet_chain = LLMChain(llm=llm, prompt=diet_prompt)

# 👤 User input
user_age = input("Enter age: ")
user_weight = input("Enter weight (kg): ")

# 🔍 Run Chain
result = diet_chain.run(age=user_age, weight=user_weight)

# 🖨️ Output
print("\n🥗 Personalized Diet Plan:\n")
print(result)
