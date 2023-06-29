# To initiate the API > uvicorn app.main:app --reload
# python version 3.11.2 
# Libraries
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from app.model import pred_nn
from app.model import train_nn

app = FastAPI()

# root message
@app.get("/")
async def root():
    return {"message": "This API designed to estimate a probability matrix for gas price changes in Ethereum transactions within next hour."}

# get probability matrix
@app.get("/probmat", status_code=status.HTTP_202_ACCEPTED)
async def prob_matrix():
    # output profile
    pred = pred_nn()
    pred_out = {
        'ranges': ['<25', '<50', '<75', '<100', '<125', '<150', '<175', '<200', 
                                    '<225', '<250', '<275', '<300'],
        '15s' : pred[:,0].tolist(),
        '30s' : pred[:,1].tolist(),
        '1min' : pred[:,3].tolist(),
        '2min' : pred[:,7].tolist(),
        '3min' : pred[:,11].tolist(),
        '5min' : pred[:,19].tolist(),
        '8min' : pred[:,31].tolist(),
        '15min' : pred[:,59].tolist(),
        '25min' : pred[:,99].tolist(),
        '30min' : pred[:,119].tolist(),
        '40min': pred[:,159].tolist(),
        '50min' : pred[:,199].tolist(),
        '55min' : pred[:,219].tolist(),
        '1hour' : pred[:,239].tolist()
    }
    return pred_out

# train shema
class train(BaseModel):
    train: bool

# train NN
@app.post("/train_nn", status_code=status.HTTP_201_CREATED)
async def trn(process:train):
    proceed = process.dict()
    if proceed['train'] == True:
        try:
            msg = train_nn()
            pred = pred_nn()
            pred_out = {
                'status' : msg,
                'ranges': ['<25', '<50', '<75', '<100', '<125', '<150', '<175', '<200', 
                                            '<225', '<250', '<275', '<300'],
                '15s' : pred[:,0].tolist(),
                '30s' : pred[:,1].tolist(),
                '1min' : pred[:,3].tolist(),
                '2min' : pred[:,7].tolist(),
                '3min' : pred[:,11].tolist(),
                '5min' : pred[:,19].tolist(),
                '8min' : pred[:,31].tolist(),
                '15min' : pred[:,59].tolist(),
                '25min' : pred[:,99].tolist(),
                '30min' : pred[:,119].tolist(),
                '40min': pred[:,159].tolist(),
                '50min' : pred[:,199].tolist(),
                '55min' : pred[:,219].tolist(),
                '1hour' : pred[:,239].tolist()
            }
            return pred_out
        except:
            return {"status" : "Neural Net was not updated."}
    else:
        pred = pred_nn()
        pred_out = {
            'status' : 'Neural Net was not updated',
            'ranges': ['<25', '<50', '<75', '<100', '<125', '<150', '<175', '<200', 
                                        '<225', '<250', '<275', '<300'],
            '15s' : pred[:,0].tolist(),
            '30s' : pred[:,1].tolist(),
            '1min' : pred[:,3].tolist(),
            '2min' : pred[:,7].tolist(),
            '3min' : pred[:,11].tolist(),
            '5min' : pred[:,19].tolist(),
            '8min' : pred[:,31].tolist(),
            '15min' : pred[:,59].tolist(),
            '25min' : pred[:,99].tolist(),
            '30min' : pred[:,119].tolist(),
            '40min': pred[:,159].tolist(),
            '50min' : pred[:,199].tolist(),
            '55min' : pred[:,219].tolist(),
            '1hour' : pred[:,239].tolist()
        }
        return pred_out