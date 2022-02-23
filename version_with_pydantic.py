from pydantic import BaseModel, Field
import json
from pprint import pprint

with open('annotell_1.json') as f:
    json_data = f.read() 


class Annotell(BaseModel):
    shapeProperties: dict 
    shapes: dict


annotell_parse = Annotell.parse_raw(json_data) 
shape_properties = (annotell_parse.shapeProperties)
objects = {}

for i in shape_properties.items():
    i = list(i)
    obj = {}
    obj[i[0]] = {"name": i[0], "type": i[1]['@all']['class']}
    objects.update(obj)
    
pprint (objects)






