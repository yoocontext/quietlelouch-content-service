from fastapi import FastAPI

from application.lifespan import lifespan
from application.api.v1.handlers import router as user_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="User service",
        docs_url="/docs",
        description="",
        root_path="/api",
        debug=False,
        lifespan=lifespan,
    )

    app.include_router(user_router)

    return app
