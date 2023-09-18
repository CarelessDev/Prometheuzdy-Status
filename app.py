from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse

app = FastAPI()

# Setup CORS
origins = [
    "https://status.prometheuzdy.cloud"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/ping", response_class=PlainTextResponse)
def ping():
    return "pong"


