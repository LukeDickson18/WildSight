from fastapi import FastAPI

app = FastAPI(
    title = "WildSight API",
    version = "0.1.0",
)

@app.get("/")
def root():
    return {"message": "Welcome to the WildSight API!"}
