from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from fastapi import FastAPI

from application.exceptions import register_exception_handlers
from application.lifespan import lifespan
from application.api.v1.base import router as v1_router
from application.otel_config import setup_tracer


def create_app() -> FastAPI:
    setup_tracer()

    app = FastAPI(
        title="User service",
        docs_url="/docs",
        description="",
        root_path="/api",
        debug=False,
        lifespan=lifespan,
    )
    register_exception_handlers(app=app)

    app.include_router(v1_router)

    FastAPIInstrumentor.instrument_app(app)

    return app
