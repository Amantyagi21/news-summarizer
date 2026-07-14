 from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def summarize_karo(text, language="Hindi"):
    if language == "Hindi":
        prompt = f"Is news ko 3 lines mein summarize karo simple Hindi mein: {text}"
    else:
        prompt = f"Summarize this news in 3 simple English lines: {text}"
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )
    return response.choices[0].message.content

def sentiment_karo(title):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": f"Is news headline ka sentiment batao — sirf ek word mein jawab do: Positive, Negative, ya Neutral: {title}"
        }]
    )
    result = response.choices[0].message.content.strip()
    if "Positive" in result:
        return "Positive"
    elif "Negative" in result:
        return "Negative"
    else:
        return "Neutral"