from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def welcome():
    x={"message":"Hello world, welcome to fastAPI!"}
    return x
