# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from blog_bot import write_essay

# app = FastAPI()

# class Dto(BaseModel):
#     prompt: str | None = None
       
# @app.get("/")
# def read_root():
#     return {"message": "Hello, FastAPI"}

# @app.post("/write")
# async def write(dto: Dto):
#     result = write_essay(dto.prompt)
#     return {'result':result}