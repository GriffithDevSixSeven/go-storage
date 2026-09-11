from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/auth/new_user")
async def new_user(user) -> dict[str,str]:
    pass

@app.post("/auth/login")
async def login(creds) -> dict[str,str]:
    pass



@app.post("/secret{secret_id}")
async def get_secret(secret_id : str) -> dict[str,str]:
    pass

if __name__ == "__main__":
    uvicorn.run(app,port=8080,host="0.0.0.0")

