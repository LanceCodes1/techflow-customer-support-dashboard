from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

from database import engine

Base = declarative_base()


class SupportCall(Base):
    __tablename__ = "support_calls"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    issue_type = Column(String)
    resolution_status = Column(String)
    call_duration = Column(Float)
    satisfaction_score = Column(Integer)


Base.metadata.create_all(bind=engine)