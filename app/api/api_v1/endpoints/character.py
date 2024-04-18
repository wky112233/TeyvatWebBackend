from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import crud, schemas
from ....dependencies import get_db
router = APIRouter()


@router.get("/", response_model=list[schemas.CharactersBase])
def read_all_characters(db: Session = Depends(get_db)):
    characters = crud.get_all_characters(db)
    if characters is None:
        raise HTTPException(status_code=404, detail="Not found")
    return characters


@router.post("/", response_model=schemas.CharactersBase)
def create_character(character: schemas.CharactersCreate, db: Session = Depends(get_db)):
    return crud.create_character(db, character=character)