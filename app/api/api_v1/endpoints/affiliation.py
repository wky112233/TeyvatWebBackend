from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import crud, schemas
from ....dependencies import get_db
router = APIRouter()


@router.get("/affiliations", response_model=list[schemas.AffiliationInDBBase], operation_id="get_affiliations")
def get_affiliations(db: Session = Depends(get_db)):
    affiliations = crud.get_all_affiliations(db)
    if not affiliations:
        raise HTTPException(status_code=404, detail="No affiliations found")
    return affiliations


@router.post("/affiliation", response_model=schemas.AffiliationInDBBase, status_code=201)
def create_affiliation(affiliation: schemas.AffiliationBase, db: Session = Depends(get_db)):
    return crud.create_affiliation(db, affiliation)


@router.put("/affiliation", response_model=schemas.AffiliationInDBBase, status_code=200)
def update_affiliation(affiliation: schemas.AffiliationBase, db: Session = Depends(get_db)):
    return crud.update_affiliation(db, affiliation)


@router.delete("/affiliation", response_model=schemas.AffiliationInDBBase)
def delete_affiliation(affiliation: schemas.AffiliationBase, db: Session = Depends(get_db)):
    return crud.delete_affiliation(db, affiliation)
