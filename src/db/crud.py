from typing import List

from sqlalchemy.orm import Session

from .models import (
    Table as TableModel,
    Reservation as ReservationModel
)
from .schemas import (
    TableBase as TableBaseSchema,
    ReservationBase as ReservationBaseSchema
)


def get_all_tables_info(db: Session) -> List[TableModel]:
    return db.query(TableModel).all()


def get_table_info(db: Session, table_id: int) -> TableModel:
    return db.query(TableModel).filter(TableModel.id == table_id).one()


def update_table(db: Session, table_id: int, table: TableBaseSchema) -> TableModel:
    fetched_table = db.query(TableModel).filter(TableModel.id == table_id)
    fetched_table.update(table.dict())
    db.commit()
    return fetched_table.one()


def add_new_table(db: Session, seats: int) -> TableModel:
    table = TableModel(seats=seats)
    db.add(table)
    db.commit()
    db.refresh(table)
    return table


def remove_table(db: Session, table_id: int):
    table = db.query(TableModel).filter(TableModel.id == table_id).one()
    db.delete(table)
    db.commit()


def create_new_reservation(
        db: Session, reservation_data: ReservationBaseSchema
) -> ReservationModel:
    reservation = ReservationModel(**reservation_data.dict())
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation
