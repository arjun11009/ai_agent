from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import llm, ping
import uvicorn



app = FastAPI()


# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(ping.router)
app.include_router(llm.router)

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000)