from fastapi import FastAPI, Query
from router import api_router

app = FastAPI(title="Visited links",
              description="""Это тестовое задание""",
              )

app.include_router(api_router)

