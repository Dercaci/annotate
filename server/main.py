from fastapi import FastAPI, Body, File
from ast import literal_eval


app = FastAPI()


# @app.post("/convert")
# def get_json_body(file : dict = Body(...)):
#     # Convert this file 
#     return file



@app.post('/convert')
def get_json_file(file: bytes = File(...)):
    json_file = literal_eval(file.decode('utf8'))
    print (type(file))
    #file.convert
    return {"file_name": 1}




   

    