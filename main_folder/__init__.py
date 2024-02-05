from fastapi import FastAPI
import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def create_app():
    app = FastAPI(description="Demo APi", version="1.0.1")
    return app
