from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )