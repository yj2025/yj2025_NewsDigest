import requests
from bs4 import BeautifulSoup


def clean_text(text: str) -> str:
    blacklist = ["구독", "저작권", "무단", "배포", "광고", "댓글", "공유"]
    for b in blacklist:
        text = text.replace(b, "")
    return text.strip()


def get_article(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Referer": "https://news.naver.com/",
        "Accept-Language": "ko-KR,ko;q=0.9",
    }

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        raise ValueError("페이지 요청 실패")

    soup = BeautifulSoup(res.text, "html.parser")

    # -----------------------------
    # 1️⃣ 네이버 뉴스 (최우선)
    # -----------------------------
    content = soup.select_one("#dic_area")
    if content:
        # 노이즈 태그 제거
        for tag in content.select("span.end_photo_org, em, strong"):
            tag.decompose()

        # 줄 단위로 나눠서 짧은 조각 필터링
        lines = content.get_text(separator="\n", strip=True).splitlines()
        lines = [line for line in lines if len(line.strip()) >= 20]
        return clean_text("\n".join(lines))

    # -----------------------------
    # 2️⃣ article 내부 p 태그만
    # -----------------------------
    article = soup.find("article")
    if article:
        paragraphs = article.find_all("p")
        text = " ".join([p.get_text(strip=True) for p in paragraphs])
        if len(text) > 200:
            return clean_text(text)

    # -----------------------------
    # 3️⃣ p 태그 중 긴 문장만 필터링
    # -----------------------------
    paragraphs = soup.find_all("p")
    filtered = []
    for p in paragraphs:
        txt = p.get_text(strip=True)
        if len(txt) < 30:
            continue
        if "@" in txt or "☞" in txt:
            continue
        filtered.append(txt)

    text = " ".join(filtered)
    if len(text) > 200:
        return clean_text(text)

    raise ValueError("본문 추출 실패")