# 📰 뉴스 요약 웹 서비스 (News Summarizer)

뉴스 URL을 입력하면 본문을 크롤링하고, AI 모델을 활용해 핵심 내용을 요약해주는 웹 서비스입니다.

---

## 🚀 프로젝트 소개

이 프로젝트는 사용자가 뉴스 URL을 입력하면
자동으로 기사 내용을 수집하고 요약 결과를 제공하는 서비스입니다.

* FastAPI 기반 백엔드 API 구현
* 뉴스 본문 크롤링 기능
* HuggingFace KoBART 모델을 활용한 한국어 뉴스 요약
* 간단한 웹 UI 제공

---

## 🛠 기술 스택

* **Backend**: FastAPI
* **AI Model**: HuggingFace Transformers (KoBART)
* **Crawling**: requests, BeautifulSoup
* **Frontend**: HTML, JavaScript
* **Server**: Uvicorn

---

## 📂 프로젝트 구조

```
fastapi/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   ├── crawler.py
│   │   └── summarizer.py
│   ├── models/
│   │   └── schema.py
│
├── templates/
│   └── index.html
```

---

## ⚙️ 주요 기능

### 1. 뉴스 크롤링

* 입력된 URL에서 뉴스 본문을 추출

### 2. AI 요약

* HuggingFace의 KoBART 모델을 사용하여 뉴스 요약

### 3. REST API 제공

* `/api/summarize` 엔드포인트를 통해 요약 결과 반환

### 4. 웹 UI

* URL 입력 → 버튼 클릭 → 요약 결과 확인

---

## 🔗 API 명세

### POST `/api/summarize`

#### Request

```json
{
  "url": "https://example.com/news"
}
```

#### Response

```json
{
  "summary": "요약된 뉴스 내용"
}
```

---

## ▶️ 실행 방법

### 1. 패키지 설치

```
pip install -r requirements.txt
```

### 2. 서버 실행

```
python -m uvicorn app.main:app --reload
```

### 3. 접속

```
http://127.0.0.1:8000
```

---

## 구현 과정에서 고려한 점

* 뉴스 본문 길이 제한 처리 (모델 입력 길이 초과 방지)
* FastAPI 라우터 구조 분리 (api / service / model)
* 프론트와 백엔드 역할 분리
* 예외 처리 및 기본 UX 개선 (로딩 상태 표시)

---

## 개선 가능 사항

* OpenAI API 연동으로 요약 품질 향상
* 뉴스 제목 및 이미지 함께 제공
* 사용자 히스토리 저장 기능
* React 기반 프론트엔드로 확장
* 요약 길이 옵션 기능 추가

---

## 배운 점

* FastAPI를 활용한 REST API 설계
* 크롤링과 AI 모델을 결합한 서비스 구현
* HuggingFace 모델을 활용한 자연어 처리 경험
* 프론트-백엔드 연동 흐름 이해

---

## 한 줄 소개

> FastAPI와 HuggingFace를 활용하여 뉴스 크롤링부터 AI 요약까지 구현한 웹 서비스
