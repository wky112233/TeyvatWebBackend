from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import crud, schemas
from ....dependencies import get_db
router = APIRouter()


@router.get("/nation", response_model=List[schemas.NationBase], operation_id="get_nations")
def get_nations(db: Session = Depends(get_db)):
    nations = crud.get_all_nations(db)
    if not nations:
        raise HTTPException(status_code=404, detail="Nations not found")
    return nations
