from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    seats = Column(Integer)

    reservations = relationship("Reservation", back_populates="table",
                                cascade="all, delete, delete-orphan")


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    persons = Column(Integer)
    duration = Column(Integer)
    table_id = Column(Integer, ForeignKey(Table.id), nullable=False)

    table = relationship("Table", back_populates="reservations")
