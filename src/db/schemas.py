import datetime

from pydantic import BaseModel


class TableBase(BaseModel):
    seats: int


class Table(TableBase):
    id: int

    class Config:
        orm_mode = True


class ReservationBase(BaseModel):
    date: datetime.date
    duration: int
    persons: int

    class Config:
        orm_mode = True


class Reservation(ReservationBase):
    id: int
