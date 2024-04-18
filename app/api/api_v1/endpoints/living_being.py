from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import crud, schemas
from ....dependencies import get_db
router = APIRouter()


@router.get("/", response_model=List[schemas.LivingBeingBase])
def get_living_beings(db: Session = Depends(get_db)):
    living_being = crud.get_all_living_beings(db)
    if not living_being:
        raise HTTPException(status_code=404, detail="Living Beings not found")
    return living_being


@router.post("/", response_model=schemas.LivingBeingBase)
def create_living_being(
        living_being: schemas.LivingBeingCreate,
        db: Session = Depends(get_db),
):
    return crud.create_living_being(db, living_being)
