from fastapi import APIRouter
from .endpoints import character, material, living_being, nation, food, affiliation

api_router = APIRouter()
api_router.include_router(character.router, prefix="", tags=["Characters"])
api_router.include_router(material.router, prefix="", tags=["Materials"])
api_router.include_router(living_being.router, prefix="", tags=["Living Being"])
api_router.include_router(nation.router, prefix="", tags=["Nation"])
api_router.include_router(food.router, prefix="", tags=["Food"])
api_router.include_router(affiliation.router, prefix="", tags=["Affiliation"])
