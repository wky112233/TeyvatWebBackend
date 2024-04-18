from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Nation(Base):
    __tablename__ = 'nation'

    nation = Column(String(255), nullable=False, primary_key=True, unique=True)
    element = Column(Text, nullable=False)

    Affiliation = relationship('Affiliation', back_populates='Nation')


class Affiliation(Base):
    __tablename__ = 'affiliations'

    affiliation_id = Column(Integer, primary_key=True, autoincrement=True)
    affiliation = Column(String(255), nullable=False)
    nation = Column(String(255), ForeignKey(Nation.nation), nullable=False)

    Nation = relationship("Nation", back_populates="Affiliation")
    Characters = relationship("Characters", back_populates="Affiliation")


class Food(Base):
    __tablename__ = 'foods'

    food_id = Column(Integer, primary_key=True, autoincrement=True)
    food_name = Column(Text, nullable=False)
    food_utility = Column(Text, nullable=False)
    food_description = Column(Text, nullable=False)
    food_icon_img = Column(Text, nullable=False)

    Characters = relationship("Characters", back_populates="Food")
    FoodToMaterial = relationship("FoodToMaterial", back_populates="Food")


class Characters(Base):
    __tablename__ = 'characters'

    character_id = Column(Integer, primary_key=True, autoincrement=True)
    character_name = Column(String(255), nullable=False)
    birthday_month = Column(String(255), nullable=False)
    birthday_date = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    vision = Column(String(255), nullable=False)
    constellation = Column(String(255), nullable=False)
    avatar_img = Column(Text, nullable=False)
    avatar_icon_img = Column(Text, nullable=False)
    namecard_img = Column(Text, nullable=False)
    affiliation_id = Column(Integer, ForeignKey(Affiliation.affiliation_id), nullable=False)
    special_food_id = Column(Integer, ForeignKey(Food.food_id),nullable=False)

    Affiliation = relationship("Affiliation", back_populates="Characters")
    Food = relationship("Food", back_populates="Characters")


class LivingBeingType(Base):
    __tablename__ = 'living_being_type'

    living_being_type_id = Column(Integer, primary_key=True, autoincrement=True)
    living_being_type = Column(Text, nullable=False, unique=True)

    LivingBeing = relationship("LivingBeing", back_populates="LivingBeingType")


class LivingBeing(Base):
    __tablename__ = 'living_being'

    living_being_id = Column(Integer, primary_key=True, autoincrement=True)
    living_being_name = Column(String(255), nullable=False, unique=True)
    living_being_description = Column(Text, nullable=False)
    living_being_icon_img = Column(Text, nullable=False)
    living_being_type_id = Column(Integer, ForeignKey(LivingBeingType.living_being_type_id), nullable=False)

    LivingBeingType = relationship("LivingBeingType", back_populates="LivingBeing")


class MaterialType(Base):
    __tablename__ = 'material_type'

    material_type_id = Column(Integer, primary_key=True, autoincrement=True)
    material_type = Column(Text, nullable=False, unique=True)

    Material = relationship("Material", back_populates="MaterialType")


class Material(Base):
    __tablename__ = 'material'

    material_id = Column(Integer, primary_key=True, autoincrement=True)
    material_name = Column(Text, nullable=False)
    material_description = Column(Text, nullable=False)
    material_icon_img = Column(Text, nullable=False)
    material_type_id = Column(Integer, ForeignKey(MaterialType.material_type_id), nullable=False)

    MaterialType = relationship("MaterialType", back_populates="Material")
    FoodToMaterial = relationship("FoodToMaterial", back_populates="Material")


class FoodToMaterial(Base):
    __tablename__ = 'food_to_material'

    food_id = Column(Integer, ForeignKey(Food.food_id), primary_key=True, nullable=False)
    material_id = Column(Integer, ForeignKey(Material.material_id), primary_key=True, nullable=False)

    Food = relationship("Food", back_populates="FoodToMaterial")
    Material = relationship("Material", back_populates="FoodToMaterial")
