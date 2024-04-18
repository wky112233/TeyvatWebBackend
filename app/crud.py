from sqlalchemy.orm import Session
from . import models, schemas


# characters
def get_characters_by_region(db: Session, region: str):
    return db.query(models.Characters).filter(models.Characters.Region == region).all()


def get_all_characters(db: Session):
    return db.query(models.Characters).all()


def create_character(db: Session, character: schemas.CharactersCreate):
    db_character = models.Characters(**character.model_dump())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


# Affiliation
def get_all_affiliations(db: Session):
    return db.query(models.Affiliation).all()


# living_being
def get_all_living_being_types(db: Session):
    return db.query(models.LivingBeingType).all()


def get_all_living_beings(db: Session):
    return db.query(models.LivingBeing).all()


def create_living_being(db: Session, living_being: schemas.LivingBeingCreate):
    db_living_being = models.LivingBeing(
        living_being_name=living_being.living_being_name,
        living_being_description=living_being.living_being_description,
        living_being_icon_img=living_being.living_being_icon_img,
        living_being_type_id=living_being.living_being_type_id  # 正确地处理外键
    )
    db.add(db_living_being)
    db.commit()
    db.refresh(db_living_being)
    return db_living_being


# food
def get_all_foods(db: Session):
    return db.query(models.Food).all()


# Material
def get_all_material_types(db: Session):
    return db.query(models.MaterialType).all()


def get_all_material(db: Session):
    return db.query(models.Material).all()


# Nation
def get_all_nations(db: Session):
    return db.query(models.Nation).all()
