from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.disaster_response_coordinator.schemas import AgenticDisasterResponseCoordinatorSessionCreate, AgenticDisasterResponseCoordinatorSessionResponse
from app.domain.disaster_response_coordinator.service import AgenticDisasterResponseCoordinatorService

router = APIRouter(prefix="/api/v1/disaster_response_coordinator", tags=["Agentic Disaster Response Coordinator Domain"])

@router.post("/sessions", response_model=AgenticDisasterResponseCoordinatorSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticDisasterResponseCoordinatorSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Disaster Response Coordinator.
    """
    return AgenticDisasterResponseCoordinatorService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticDisasterResponseCoordinatorSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticDisasterResponseCoordinatorService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
