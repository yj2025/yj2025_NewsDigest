from fastapi import APIRouter
from app.services.crawler import get_article
from app.services.summarizer import summarize
from app.models.schema import SummaryRequest, SummaryResponse

router = APIRouter()

@router.post("/summarize", response_model=SummaryResponse)
def summarize_news(req: SummaryRequest):
    text = get_article(req.url)
    result = summarize(text)

    return SummaryResponse(summary=result)
