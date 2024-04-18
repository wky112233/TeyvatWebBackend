from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .api.api_v1.router import api_router
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas
from .core.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix='/api/v1')


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 设置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 允许的域名或IP，这里以前端运行在localhost:3000为例
    allow_credentials=True,
    allow_methods=["*"],  # 允许的方法，['GET', 'POST', 'PUT', 'DELETE']也是常见配置
    allow_headers=["*"],  # 允许的头部
)

app.include_router(api_router, prefix='/api/v1')

# # Character
# # get character by region
# @app.get("/characters", response_model=list[schemas.CharactersBase])
# def read_characters(region: str, db: Session = Depends(get_db)):
#     characters = crud.get_characters_by_region(db, region=region)
#     if characters is None:
#         raise HTTPException(status_code=404, detail="Characters not found")
#     return characters


# # get all character
# @app.get("/characters", response_model=list[schemas.CharactersBase])
# def read_characters(db: Session = Depends(get_db)):
#     characters = crud.get_characters(db)
