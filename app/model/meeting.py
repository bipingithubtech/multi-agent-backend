from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    organizer_email = Column(String)
    participant_email = Column(String)
    meeting_time = Column(DateTime)
    status = Column(String)
