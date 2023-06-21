import openai

def request_openai(text):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Please simplify the following text: {text}",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        simplified_text = response.choices[0].text.strip()
        return {"simplified_text": simplified_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
