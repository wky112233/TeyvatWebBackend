from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import crud, schemas
from ....dependencies import get_db
router = APIRouter()


@router.get("/", response_model=list[schemas.MaterialBase])
def get_materials(db: Session = Depends(get_db)):
    material = crud.get_all_material(db)
    if not material:
        raise HTTPException(status_code=404, detail="No material")
    return material
