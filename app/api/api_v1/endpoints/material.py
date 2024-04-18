from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import crud, schemas
from ....dependencies import get_db
router = APIRouter()


@router.get("/allMaterialTypes", response_model=list[schemas.MaterialTypeInDBBase])
def get_all_materials(db: Session = Depends(get_db)):
    material_type = crud.get_all_material_types(db)
    if not material_type:
        raise HTTPException(status_code=404, detail="No materials found")
    return material_type


@router.get("/material", response_model=list[schemas.MaterialBase], operation_id="GetMaterials")
def get_materials(db: Session = Depends(get_db)):
    material = crud.get_all_material(db)
    if not material:
        raise HTTPException(status_code=404, detail="No material")
    return material


@router.post("/material", response_model=schemas.MaterialInDBBase, status_code=201)
def create_material(material: schemas.MaterialCreate, db: Session = Depends(get_db)):
    material = crud.create_material(db, material=material)
    if not material:
        raise HTTPException(status_code=404, detail="No material")
    return material


@router.delete("/material", response_model=schemas.MaterialBase, status_code=200)
def delete_material(material: schemas.MaterialBase, db: Session = Depends(get_db)):
    material = crud.delete_material(db, material=material)
    if not material:
        raise HTTPException(status_code=404, detail="No material")
    return material


@router.put("/material", response_model=schemas.MaterialBase, status_code=200)
def update_material(material: schemas.MaterialUpdate, db: Session = Depends(get_db)):
    material = crud.update_material_by_name(db, material=material)
    if not material:
        raise HTTPException(status_code=404, detail="No material")
    return material
