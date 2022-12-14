from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from routes.user.userRoutes import userRouter


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(userRouter)

@app.get("/")
async def root():
    return {"message": "Hello World"}
    