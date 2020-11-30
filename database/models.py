from database import db
from sqlalchemy.sql import func
from sqlalchemy import Column, String, TypeDecorator, VARCHAR, ForeignKey
from sqlalchemy.sql import operators
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LinebackerReps(db.Model):

    __tablename__ = 'linebackerrep'

    linebacker_rep_id = Column(db.Integer, primary_key=True)
    playerid = Column(db.Text)
    rep_date = db.Column(db.DateTime(timezone=True))
    periodnum = Column(db.Integer)
    playnum = Column(db.Integer)
    drill = Column(db.Text)
    alignmentquality = Column(db.Integer)
    assignmentquality = Column(db.Integer)
    effortquality = Column(db.Integer)
    finishquality = Column(db.Integer)
    position = Column(db.Text)
    note = Column(db.Text)
