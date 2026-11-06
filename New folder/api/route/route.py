from fastapi import (
    APIRouter,
    HTTPException,
)

from service.services.ai_service import (
    AIService,
)
from service.classifier.keyword_classifier import (
    KeywordClassifier,
)


router = APIRouter()


classifier = KeywordClassifier()

ai_service = AIService(
    classifier
)


@router.get("/")
def root():

    return {
        "message": "AI Service is running",
        "version": "1.0.0",
    }


@router.post("/classify")
def classify(
    text: str,
):

    try:

        return ai_service.classify(
            text
        )

    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )