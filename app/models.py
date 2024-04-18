from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Affiliation(Base):
    __tablename__ = 'affiliation'

    affiliation_id = Column(Integer, primary_key=True, autoincrement=True)
    affiliation_name = Column(String(255), nullable=False)

    character_id = relationship("Character", back_populates="Affiliation")


class Food(Base):
    __tablename__ = 'food'

    food_id = Column(Integer, primary_key=True, autoincrement=True)
    food_name = Column(Text, nullable=False, unique=True)
    food_utility = Column(Text, nullable=False)
    food_description = Column(Text, nullable=False)
    food_icon_img = Column(Text, nullable=False)

    character = relationship("Character", back_populates="Food")


class Characters(Base):
    __tablename__ = 'characters'

    character_id = Column(Integer, primary_key=True, autoincrement=True)
    character_name = Column(String(255), nullable=False)
    birthday_mouth = Column(String(255), nullable=False)
    birthday_date = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    vision = Column(String(255), nullable=False)
    constellation = Column(String(255), nullable=False)
    avatar_img = Column(Text, nullable=False)
    avatar_icon_img = Column(Text, nullable=False)
    namecard_img = Column(Text, nullable=False)
    affiliation_id = Column(Integer, ForeignKey(Affiliation.affiliation_id), nullable=False)
    special_food_id = Column(Integer, ForeignKey(Food.food_id),nullable=False)

    affiliation = relationship("Affiliation", back_populates="Character")
    food = relationship("Food", back_populates="Characters")


class LivingBeingType(Base):
    __tablename__ = 'living_being_type'

    living_being_type_id = Column(Integer, primary_key=True, autoincrement=True)
    living_being_type = Column(Text, nullable=False, unique=True)

    living_being = relationship("LivingBeing", back_populates="LivingBeingType")


class LivingBeing(Base):
    __tablename__ = 'living_being'

    living_being_id = Column(Integer, primary_key=True, autoincrement=True)
    living_being_name = Column(String(255), nullable=False, unique=True)
    living_being_description = Column(Text, nullable=False)
    living_being_icon_img = Column(Text, nullable=False)
    living_being_type_id = Column(Integer, ForeignKey(LivingBeingType.living_being_type_id), nullable=False)

    living_being_type = relationship("LivingBeingType", back_populates="LivingBeing")


class MaterialType(Base):
    __tablename__ = 'material_type'

    material_type_id = Column(Integer, primary_key=True, autoincrement=True)
    material_type = Column(Text, nullable=False, unique=True)

    material = relationship("Material", back_populates="MaterialType")


class Material(Base):
    __tablename__ = 'material'

    material_id = Column(Integer, primary_key=True, autoincrement=True)
    material_name = Column(Text, nullable=False, unique=True)
    material_description = Column(Text, nullable=False)
    material_icon_img = Column(Text, nullable=False)
    material_type_id = Column(Integer, ForeignKey(MaterialType.material_type_id), nullable=False)

    material_type = relationship("MaterialType", back_populates="Material")


class Nation(Base):
    __tablename__ = 'nation'

    nation = Column(String(255), nullable=False, primary_key=True, unique=True)
    element = Column(Text, nullable=False)


class FoodToMaterial(Base):
    __tablename__ = 'food_to_material'

    food_id = Column(Integer, ForeignKey(Food.food_id), primary_key=True, nullable=False)
    material_id = Column(Integer, ForeignKey(Material.material_id), primary_key=True, nullable=False)
