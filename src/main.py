from fastapi import FastAPI

app = FastAPI()

app.state.counter = 0

@app.get("/")
async def root():
    app.state.counter += 1
    
    return {
        "message": "Hello World",
        "requests_count": app.state.counter
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)