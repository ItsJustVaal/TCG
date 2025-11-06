# from fastapi import FastAPI
# from app.api.middleware import add_cors
# # from app.api.v1.router import api_router
# from app.core.settings import get_settings
# from app.db.session import engine
# from app.db.base import Base

# def create_app() -> FastAPI:
#     settings = get_settings()
#     app = FastAPI(title=settings.APP_NAME)
#     add_cors(app)
#     app.include_router(api_router, prefix=f"{settings.API_PREFIX}/v1")

#     @app.on_event("startup")
#     async def _startup():
#         async with engine.begin() as conn:
#             await conn.run_sync(Base.metadata.create_all)

#     return app

# app = create_app()
