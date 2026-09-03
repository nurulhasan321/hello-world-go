import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World from GitHub in GCP using Python FastAPI!🐍"

if __name__ == "__main__":
    # Get port from environment variable, defaulting to 8080
    port = int(os.getenv("PORT", 8080))
    
    # Run the server
    uvicorn.run("main:app", host="0.0.0.0", port=port, log_level="info")
