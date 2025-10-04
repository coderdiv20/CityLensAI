from fastapi import FastAPI

app = FastAPI(title="Vision Service (stub)")

@app.get("/health")
async def health():
    return {"status": "ok"}
