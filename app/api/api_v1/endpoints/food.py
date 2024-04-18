from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from .... import crud, schemas
from ....dependencies import get_db
router = APIRouter()


@router.get("/foods", response_model=List[schemas.FoodInDBBase])
def get_foods(db: Session = Depends(get_db)):
    foods = crud.get_all_foods(db)
    if not foods:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return foods


@router.post("/foods", response_model=schemas.FoodCreate)
def create_food(food: schemas.FoodCreate, db: Session = Depends(get_db)):
    return crud.create_food(db, food=food)


@router.delete("/foods", response_model=schemas.FoodDelete)
def delete_food(food: schemas.FoodDelete, db: Session = Depends(get_db)):
    return crud.delete_food(db, food=food)


@router.put("/foods", response_model=schemas.FoodUpdate)
def update_food(food: schemas.FoodUpdate, db: Session = Depends(get_db)):
    return crud.update_food(db, food=food)
