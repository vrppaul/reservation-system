from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db import base, crud, schemas

router = APIRouter(prefix="/tables", tags=["tables"])


@router.post("/reserve", response_model=schemas.Reservation)
async def reserve_table(reservation: schemas.ReservationBase, db: Session = Depends(base.get_db)):
    """
    Description
    """
    return crud.create_new_reservation(db, reservation)


@router.get("/availability")
async def availability():
    """
    Description
    """
    return {"table": "is reserved"}


@router.get("/table_available")
async def table_available():
    """
    Description
    """
    return {"table": "is reserved"}
