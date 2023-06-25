# To initiate the API > uvicorn app.main:app -- reload
# python version 3.11.2 
# Libraries
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

# root message
@app.get("/")
async def root():
    return {"message": "This API designed to estimate a probability matrix for gas price changes in Ethereum transactions within next hour."}

# get probability matrix
@app.get("/prbmat")
async def probmat():
    ...

# train NN
@app.post("/train_nn")
async def trn():
    ...