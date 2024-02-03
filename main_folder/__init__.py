from fastapi import FastAPI

def create_app():
    app = FastAPI(description="Demo APi", version="1.0.1")
    return app
