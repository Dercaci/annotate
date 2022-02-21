from fastapi import FastAPI, Body, File, Response
import json
from converter import Converter


c = Converter()
app = FastAPI()

@app.post("/convert")
def get_json_body(file : dict = Body(...)):
    return c.convert(file)



