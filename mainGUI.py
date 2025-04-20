import tkinter as tk
from tkinter import scrolledtext
import openai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Completion function
def get_completion(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# GUI setup
def submit_prompt():
    prompt = input_box.get("1.0", tk.END).strip()
    if not prompt:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter a prompt.")
        return
    result = get_completion(prompt)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

# Main window
window = tk.Tk()
window.title("AI Prompt Completion")
window.geometry("600x500")

# Prompt input
tk.Label(window, text="Enter your prompt:").pack(pady=5)
input_box = scrolledtext.ScrolledText(window, height=8, wrap=tk.WORD)
input_box.pack(padx=10, fill=tk.BOTH, expand=False)

# Submit button
submit_btn = tk.Button(window, text="Submit", command=submit_prompt)
submit_btn.pack(pady=10)

# Output
tk.Label(window, text="Completion:").pack(pady=5)
output_box = scrolledtext.ScrolledText(window, height=12, wrap=tk.WORD)
output_box.pack(padx=10, fill=tk.BOTH, expand=True)

# Start GUI loop
window.mainloop()
