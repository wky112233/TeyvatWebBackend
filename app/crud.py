from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import select


# characters
def get_character_by_name(db: Session, name: str):
    return db.query(models.Characters).filter(models.Characters.character_name == name).all()


def get_character_by_region(db: Session, name: str):
    return db.query(models.Characters).filter(models.Characters.character_name == name).all()


def get_all_characters(db: Session):
    return db.query(models.Characters).all()


def create_character(db: Session, character: schemas.CharactersCreate):
    db_character = models.Characters(**character.model_dump())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


def update_character_by_name(db: Session, character: schemas.CharactersUpdate):
    update_data = character.model_dump(exclude_unset=True)
    # 查找要更新的角色记录
    db_character = db.query(models.Characters).filter(models.Characters.character_name == character.character_name)
    db_character.update(update_data)
    db.commit()
    return db_character.first()


def delete_character_by_name(db: Session, character: schemas.CharactersBase):
    db_character = db.query(models.Characters).filter(models.Characters.character_name == character.character_name)
    db_character.delete(synchronize_session=False)
    db.commit()
    return db_character.first()


# Affiliation
def get_all_affiliations(db: Session):
    return db.query(models.Affiliation).all()


def create_affiliation(db: Session, affiliation: schemas.AffiliationBase):
    db_affiliation = models.Affiliation(**affiliation.model_dump())
    db.add(db_affiliation)
    db.commit()
    db.refresh(db_affiliation)
    return db_affiliation


def update_affiliation(db: Session, affiliation: schemas.AffiliationBase):
    update_data = affiliation.model_dump(exclude_unset=True)
    db_affiliation = db.query(models.Affiliation).filter(models.Affiliation.affiliation == affiliation.affiliation)
    db_affiliation.update(update_data)
    db.commit()
    return db_affiliation.first()


def delete_affiliation(db: Session, affiliation: schemas.AffiliationBase):
    db_affiliation = db.query(models.Affiliation).filter(models.Affiliation.affiliation == affiliation.affiliation)
    db_affiliation.delete(synchronize_session=False)
    db.commit()
    return db_affiliation.first()


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


def update_living_being_by_name(db: Session, living_being: schemas.LivingBeingCreate):
    update_data = living_being.model_dump(exclude_unset=True)
    db_living_being = db.query(models.LivingBeing).filter(models.LivingBeing.living_being_name == living_being.living_being_name)
    db_living_being.update(update_data)
    db.commit()
    return db_living_being.first()


def delete_living_being_by_name(db: Session, living_being: schemas.LivingBeingBase):
    db_living_being = db.query(models.LivingBeing).filter(models.LivingBeing.living_being_name == living_being.living_being_name)
    db_living_being.delete(synchronize_session=False)
    db.commit()
    return db_living_being.first()


# food
def get_all_foods(db: Session):
    return db.query(models.Food).all()


def get_food_by_id(db: Session, id: int):
    return db.query(models.Food).filter(models.Food.food_id == id).first()


def create_food(db: Session, food: schemas.FoodCreate):
    db_food = models.Food(
        food_name=food.food_name,
        food_description=food.food_description,
        food_utility=food.food_utility,
        food_icon_img=food.food_icon_img
    )
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food


def update_food(db: Session, food: schemas.FoodUpdate):
    update_data = food.model_dump(exclude_unset=True)
    db_food = db.query(models.Food).filter(
        models.Food.food_name == food.food_name
    )
    db_food.update(update_data)
    db.commit()
    return db_food.first()


def delete_food(db: Session, food: schemas.FoodBase):
    db_food = db.query(models.Food).filter(models.Food.food_name == food.food_name)
    db_food.delete(synchronize_session=False)
    db.commit()
    return db_food.first()


# Material
def get_all_material_types(db: Session):
    return db.query(models.MaterialType).all()


def get_all_material(db: Session):
    return db.query(models.Material).all()


def get_all_material_by_food_id(db: Session, food_id: int):
    query = db.query(models.Material) \
        .join(models.FoodToMaterial, models.FoodToMaterial.material_id == models.Material.material_id) \
        .filter(models.FoodToMaterial.food_id == food_id)
    print(query.statement)  # 输出SQL语句检查是否正确
    return query.all()


def create_material(db: Session, material: schemas.MaterialCreate):
    db_material = models.Material(
        material_name=material.material_name,
        material_description=material.material_description,
        material_icon_img=material.material_icon_img,
        material_type_id=material.material_type_id
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


def update_material_by_name(db: Session, material: schemas.MaterialUpdate):
    update_data = material.model_dump(exclude_unset=True)
    db_material = db.query(models.Material).filter(
        models.Material.material_name == material.material_name
    )
    db_material.update(update_data)
    db.commit()
    return db_material


def delete_material(db: Session, material: schemas.MaterialBase):
    db_material = db.query(models.Material).filter(
        models.Material.material_name == material.material_name
    )
    db_material.delete(synchronize_session=False)
    db.commit()
    return db_material


# Nation
def get_all_nations(db: Session):
    return db.query(models.Nation).all()
