from fastapi import FastAPI
from mixer import Mixer

app = FastAPI()
mixer_list = []

@app.get("/")
def home():
    print("In side home page")
    return {"message": "Welcome to the Kiran's mixer shop!"}

@app.post("/addtmixer")
def add_new_mixer(mixer: Mixer):
    print(f"inside add new mixer method")
    mixer_list.append(mixer.dict())
    return mixer_list

@app.get("/mixers")
async def get_mixers():
    print(f"Inside get_mixer function...")
    return {"available_mixer": mixer_list}