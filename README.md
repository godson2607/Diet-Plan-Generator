🥗 Personalized Diet Plan Generator using LangChain & OpenAI

This project generates a culturally neutral, healthy 1-day diet plan using OpenAI's GPT-4o via LangChain. You simply input your **age** and **weight**, and it returns a full-day meal plan created by an AI dietitian.

---

## 📁 Project Structure



diet-plan-generator/
│
├── main.py        # Main script to generate the diet plan
├── .env           # Contains your OpenAI API key
└── README.md      # Project documentation

`

---

## ⚙ Requirements

- Python 3.8+
- OpenAI API Key

### 📦 Install dependencies

bash
pip install langchain langchain-openai python-dotenv
`

---

## 🔑 Setup API Key

Create a `.env` file in the root directory and add your OpenAI API key:


OPENAI_API_KEY=your_openai_api_key_here


---

## ▶ Run the Project

bash
python main.py


You’ll be asked to enter:

* Your age
* Your weight (in kg)

Then, the program will generate a healthy, balanced meal plan.

---

## 💡 Features

* Uses GPT-4o for high-quality, natural-sounding responses.
* Personalized meal plan based on user age and weight.
* Covers all meals:

  * Breakfast
  * Mid-morning snack
  * Lunch
  * Evening snack
  * Dinner

---

## 📌 Sample Output


Enter age: 25
Enter weight (kg): 70

🥗 Personalized Diet Plan:

Breakfast:
- Oatmeal with banana slices and almonds
...

Dinner:
- Grilled salmon with roasted vegetables
...


---

## 📚 Technologies Used

* [LangChain](https://www.langchain.com/) – Framework for chaining LLMs
* [OpenAI](https://platform.openai.com/docs) – GPT-4o model
* [Python dotenv](https://pypi.org/project/python-dotenv/) – For managing API keys securely

---

## 📝 License

MIT License – Free to use and modify

---

## 👥 Author

Made with ❤ using LangChain & GPT-4o



---

