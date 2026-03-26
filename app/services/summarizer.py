from transformers import pipeline

# 모델 로드 (처음에 좀 오래 걸림)
# HuggingFace
summarizer_model = pipeline(
    "summarization",
    model="digit82/kobart-summarization",
    tokenizer="digit82/kobart-summarization",
)

def summarize(text: str) -> str:
    # kobart 한국어 800자 제한
    text = text[:800]

    result = summarizer_model(
        text,
        max_length=150,
        min_length=50,
        do_sample=False,
        no_repeat_ngram_size=3,  # 반복 방지
    )

    return result[0]["summary_text"]