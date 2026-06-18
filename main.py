from fastapi import FastAPI
import uvicorn
from routes.agent_routes import a_router
from database.db_connection import db

db.get_connection()
db.create_database()
db.create_tables()

app = FastAPI()

app.include_router(a_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
