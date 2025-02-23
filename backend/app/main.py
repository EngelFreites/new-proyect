from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import create_db_and_tables


app = FastAPI(lifespan=create_db_and_tables)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # Permite cualquier origen (puedes cambiarlo por ["http://localhost:3000"] por seguridad)
  allow_credentials=True,
  allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
  allow_headers=["*"],  # Permite todos los encabezados
)

@app.get("/hellow")
async def hellow():
  return {"message": "hellow world"}
