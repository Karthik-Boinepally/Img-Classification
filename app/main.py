from fastapi import FastAPI
from app.routes import router

app = FastAPI()
# Include routes
app.include_router(router)


# Welcome route
@app.get("/")
def welcome():
    return {"message": "This is SVM Text Classification API"}
