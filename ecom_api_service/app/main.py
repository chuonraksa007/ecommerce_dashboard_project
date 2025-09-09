from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import route
from app.base.database import get_db
from app.base.seed import seed_data

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Run seed at startup
    async for session in get_db():
        await seed_data(session)

# Register the router
app.include_router(route.router)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
