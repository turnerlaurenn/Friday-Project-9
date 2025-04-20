# AI Prompt Completion GUI

This is a simple interactive GUI built with Python and Tkinter that allows users to enter a prompt and receive a response using OpenAI's GPT model.

---

## Features

- Input a prompt through a text box  
- Submit the prompt and receive a GPT-generated response  
- Displays the result in a scrollable output box  
- Prevents prompts from exceeding token limits  
- Keeps your OpenAI API key secure via a `.env` file  

---

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine and navigate into the project folder.

---

### 2. Install Dependencies

Make sure you have Python installed. Then install the required libraries:

pip install -r requirements.txt

Required packages:
- openai
- python-dotenv
- tkinter (usually comes with Python)

---

### 3. Add Your OpenAI API Key

1. Rename `.env.example` to `.env`
2. Get an OpenAI API key from https://platform.openai.com/account/api-keys
3. Replace `your-api-key-here` with your actual key

---

### 4. Run the App

To launch the application, run:

python main.py

The window will pop up, and you can start typing prompts right away!

---

## About the `.gitignore` File

This project includes a `.gitignore` file that tells Git to ignore sensitive files like `.env`. That means the personal API key **will not be tracked**, committed, or uploaded to GitHub when the project is pushed.

If someone else clones the repository, they won’t see the personal API key — they’ll have to create their own `.env` file (or rename the provided `.env.example` file) and add their own key.

---

## Notes

- Output may be truncated at around 500 tokens for safety and clarity.  
- Prompts longer than 400 words will be rejected with a helpful message.  
- If you see an error about the API key, make sure `.env` exists and contains your key.

---

## Questions?

Feel free to open an issue or reach out if you get stuck!