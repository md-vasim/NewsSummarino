import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.views:app", port=8823, reload=True)