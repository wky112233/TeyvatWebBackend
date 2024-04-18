from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import crud, schemas
from ....dependencies import get_db
router = APIRouter()


@router.get("/allCharacter", response_model=list[schemas.CharactersInDBBase], operation_id="read_all_characters")
def read_all_characters(db: Session = Depends(get_db)):
    characters = crud.get_all_characters(db)
    if characters is None:
        raise HTTPException(status_code=404, detail="Not found")
    return characters


@router.get("/character/", response_model=list[schemas.CharactersBase], operation_id="get_character_by_name")
def get_character_by_name(name: str, db: Session = Depends(get_db)):
    characters = crud.get_character_by_name(db, name)
    if characters is None:
        raise HTTPException(status_code=404, detail="Not found")
    return characters


@router.post("/character", response_model=schemas.CharactersCreate, operation_id="create_character")
def create_character(character: schemas.CharactersCreate, db: Session = Depends(get_db)):
    return crud.create_character(db, character=character)


@router.put("/character", response_model=schemas.CharactersBase)
def update_character(character: schemas.CharactersUpdate, db: Session = Depends(get_db)):
    return crud.update_character_by_name(db, character=character)


@router.delete("/character", response_model=schemas.CharactersBase)
def delete_character(character: schemas.CharactersBase, db: Session = Depends(get_db)):
    return crud.delete_character_by_name(db, character=character)
