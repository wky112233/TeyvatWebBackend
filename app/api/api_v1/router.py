from fastapi import APIRouter
from .endpoints import character, material, living_being, nation

api_router = APIRouter()
api_router.include_router(character.router, prefix="/characters", tags=["Characters"])
api_router.include_router(material.router, prefix="/materials", tags=["Materials"])
api_router.include_router(living_being.router, prefix="/living_being", tags=["Living Being"])
api_router.include_router(nation.router, prefix="/nation", tags=["Nation"])
