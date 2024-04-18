from pydantic import BaseModel
from typing import Optional

from app.models import MaterialType


class CharactersBase(BaseModel):
    character_name: str
    birthday_month: int
    birthday_date: int
    title: str
    vision: str
    constellation: str
    avatar_img: str
    avatar_icon_img: str
    namecard_img: str


class CharactersWithA(CharactersBase):
    affiliation: str


class CharactersCreate(CharactersBase):
    affiliation_id: int
    special_food_id: int


class CharactersUpdate(CharactersCreate):
    pass


class CharactersInDBBase(CharactersBase):
    character_id: int
    affiliation_id: int
    special_food_id: int

    class Config:
        from_attributes = True


class Characters(CharactersInDBBase):
    pass


class CharactersInDB(CharactersInDBBase):
    pass


class AffiliationBase(BaseModel):
    affiliation: str
    nation: str


class AffiliationCreate(AffiliationBase):
    pass


class AffiliationUpdate(AffiliationBase):
    pass


class AffiliationInDBBase(AffiliationBase):
    affiliation_id: int

    class Config:
        from_attributes = True


class LivingBeingBase(BaseModel):
    living_being_name: str
    living_being_description: str
    living_being_icon_img: str


class LivingBeingCreate(LivingBeingBase):
    living_being_type_id: int


class LivingBeingUpdate(LivingBeingCreate):
    pass


class LivingBeingInDBBase(LivingBeingBase):
    living_being_id: int
    living_being_type_id: int

    class Config:
        from_attributes = True


class LivingBeingTypeBase(BaseModel):
    living_type_type: str


class LivingBeingTypeCreate(LivingBeingTypeBase):
    pass


class LivingBeingTypeUpdate(LivingBeingTypeBase):
    pass


class LivingBeingTypeInDBBase(LivingBeingTypeBase):
    living_being_type_id: int

    class Config:
        from_attributes = True


class FoodBase(BaseModel):
    food_name: str
    food_utility: str
    food_description: str
    food_icon_img: str


class FoodCreate(FoodBase):
    pass


class FoodUpdate(FoodBase):
    pass


class FoodDelete(FoodBase):
    pass


class FoodInDBBase(FoodBase):
    food_id: int

    class Config:
        from_attributes = True


class MaterialTypeBase(BaseModel):
    material_type: str


class MaterialTypeCreate(MaterialTypeBase):
    pass


class MaterialTypeUpdate(MaterialTypeBase):
    pass


class MaterialTypeInDBBase(MaterialTypeBase):
    material_id: int

    class Config:
        from_attributes = True


class MaterialBase(BaseModel):
    material_name: str
    material_description: str
    material_icon_img: str


class MaterialCreate(MaterialBase):
    material_type_id: int
    pass


class MaterialUpdate(MaterialCreate):
    pass


class MaterialInDBBase(MaterialBase):
    material_id: int
    material_type_id: int

    class Config:
        from_attributes = True


class NationBase(BaseModel):
    nation: str
    element: str


class NationCreate(NationBase):
    pass


class NationUpdate(NationBase):
    pass


class NationInDBBase(NationBase):
    pass
