from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.disaster_response_coordinator.models import AgenticDisasterResponseCoordinatorSession, AgenticDisasterResponseCoordinatorItem
from app.domain.disaster_response_coordinator.schemas import AgenticDisasterResponseCoordinatorSessionCreate, AgenticDisasterResponseCoordinatorItemCreate

class AgenticDisasterResponseCoordinatorService:
    @staticmethod
    def create_session(db: Session, data: AgenticDisasterResponseCoordinatorSessionCreate) -> AgenticDisasterResponseCoordinatorSession:
        db_obj = AgenticDisasterResponseCoordinatorSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticDisasterResponseCoordinatorSession:
        return db.query(AgenticDisasterResponseCoordinatorSession).filter(AgenticDisasterResponseCoordinatorSession.id == session_id).first()
