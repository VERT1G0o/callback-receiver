from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/callback/")
async def post_endpoint(request: Request):
    print("Body:", await request.json())
    print("Headers:", request.headers)
