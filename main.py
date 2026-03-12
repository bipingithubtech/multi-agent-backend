from fastapi import FastAPI
import uvicorn

app = FastAPI(title="multi-agent-backend")


@app.get("/")
async def root():
    return {"message": "multi-agent-backend started"}


def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
