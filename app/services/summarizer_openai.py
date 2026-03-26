import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize(text: str) -> str:
    # 토큰
    text = text[:3000]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "너는 뉴스 요약 전문가야. 핵심만 3줄로 요약해."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()