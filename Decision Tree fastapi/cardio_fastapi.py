import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
from Cardio import cardio

app = FastAPI()

pi_in = open("cardio_deci.pkl","rb")
dec_tree = pickle.load(pi_in)

@app.get('/')
def index():
  return {'message:Welcome to the Machine Learning Projects'}

@app.post('/predict')
def pred_cardio(data:cardio):
  data = data.dict()
  age = data['age']
  gen = data['gender']
  hei = data['height']
  wei = data['weight']  
  aph = data['ap_hi']
  apl = data['ap_lo']
  cho = data['cholestrol']
  glu = data['gluc']
  smo = data['smoke']
  alc = data['alco']
  act = data['active']

  pred = dec_tree.predict([[age, gen, hei, wei, aph, apl, cho, glu, smo, alc, act]])
  res = int(pred[0])
  #print(pred)

  if res==0:
    pre = "Patient has no cardiovascular disease"
  else:
    pre = "Patient has cardiovascular disease"

  return {'predict': pre}

if __name__ == '__main__':
  uvicorn.run(app, host='127.0.0.1', port=8000)
