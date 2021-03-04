from typing import List

from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from src.db import base, crud, schemas


router = APIRouter(prefix="/tables", tags=["tables"])

responses = {
    404: {"description": "Table not found"},
}


@router.get("/", response_model=List[schemas.Table])
async def get_tables(db: Session = Depends(base.get_db)):
    return crud.get_all_tables_info(db)


@router.post("/", response_model=schemas.Table, status_code=status.HTTP_201_CREATED)
async def add_new_table(db: Session = Depends(base.get_db), seats: int = Body(..., embed=True)):
    return crud.add_new_table(db, seats=seats)


@router.get("/{table_id}", response_model=schemas.Table, responses=responses)
async def get_table(table_id: int, db: Session = Depends(base.get_db)):
    try:
        return crud.get_table_info(db, table_id)
    except NoResultFound:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{table_id}", response_model=schemas.Table, responses=responses)
async def edit_table(table_id: int, table: schemas.TableBase, db: Session = Depends(base.get_db)):
    try:
        return crud.update_table(db, table_id, table)
    except NoResultFound:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{table_id}", status_code=status.HTTP_204_NO_CONTENT, responses=responses)
async def remove_table(table_id: int, db: Session = Depends(base.get_db)):
    try:
        crud.remove_table(db, table_id)
    except NoResultFound:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/decide_reservation")
async def decide_reservation():
    """
    Description
    """
    return {"table": "is reserved"}
