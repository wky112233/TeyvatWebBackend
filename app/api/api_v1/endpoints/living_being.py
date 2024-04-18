from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import crud, schemas
from ....dependencies import get_db
router = APIRouter()


@router.get("/livingBeingTypes", response_model=List[schemas.LivingBeingTypeBase])
def get_living_being_types(db: Session = Depends(get_db)):
    types = crud.get_all_living_being_types(db)
    if not types:
        raise HTTPException(status_code=404, detail="No living being types found")
    return types


@router.get("/livingBeing", response_model=List[schemas.LivingBeingBase], operation_id="get_living_beings")
def get_living_beings(db: Session = Depends(get_db)):
    living_being = crud.get_all_living_beings(db)
    if not living_being:
        raise HTTPException(status_code=404, detail="Living Beings not found")
    return living_being


@router.post("/livingBeing", response_model=schemas.LivingBeingBase, operation_id="create_living_being")
def create_living_being(
        living_being: schemas.LivingBeingCreate,
        db: Session = Depends(get_db),
):
    return crud.create_living_being(db, living_being)


@router.put("/livingBeing", response_model=schemas.LivingBeingBase, operation_id="create_living_being")
def create_living_being(
        living_being: schemas.LivingBeingUpdate,
        db: Session = Depends(get_db),
):
    return crud.update_living_being_by_name(db, living_being)


@router.delete("/livingBeing", response_model=schemas.LivingBeingBase, operation_id="create_living_being")
def create_living_being(
        living_being: schemas.LivingBeingUpdate,
        db: Session = Depends(get_db),
):
    return crud.delete_living_being_by_name(db, living_being)
