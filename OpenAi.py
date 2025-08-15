import ollama

def ask_gpt(prompt):
    try:
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )
        # Extract content safely
        return response.get("message", {}).get("content", "Sorry, I couldn't find an answer.")
    except Exception as e:
        return f"Error: {str(e)}"

