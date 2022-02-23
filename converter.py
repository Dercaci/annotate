import json
from math import sqrt
import os, binascii


class Converter:
    def convert(self, dict_data):


        # first block "elements"
        shapeProperties = dict_data['shapeProperties'] # take a teil of the dict
        id_obj = [elem for elem in shapeProperties.keys()] # take the id-s
        obj = {}
        objects = {}
        data = {}
        openlabel = {}
        for idd in id_obj:
            type_ob = shapeProperties[idd]['@all']['class']
            names = {"name" : idd, "type" :type_ob} # name : id, type: vehicle for ex
            na_ty = {}
            na_ty[idd] = names
            obj.update (na_ty) # add to a dict all name/type
        objects= obj # dict obj:all obj


        #first block "relations"
        relations = {}
        elements = {}
        for iddd in shapeProperties:
            if iddd in shapeProperties:
                if 'PushingOrPulling' in shapeProperties[iddd]["@all"]:
                    if shapeProperties[iddd]['@all']['PushingOrPulling'] != 'Nothing':
                        zero = {}
                        rdf_objects = []
                        rdf_subjects = []
                        rdf_o = {}
                        rdf_s = {}
                        a = (shapeProperties[iddd]['@all']['PushingOrPulling']['shape'])
                        rdf_o = {"type":"object", "uid": iddd}
                        rdf_s = {"type":"object", "uid": a}
                        rdf_objects.append(rdf_o)
                        rdf_subjects.append(rdf_s)
                        zero = {'name':'0',"rdf_objects":rdf_objects,"rdf_subjects":rdf_subjects, "type": "PushingOrPulling"}
                    else:    
                        one = {}
                        rdf_objects = []
                        rdf_subjects = []
                        rdf_o = {}
                        rdf_s = {}
                        rdf_o = {"type":"object", "uid": iddd}
                        rdf_s = {"type":"object", "uid": "Nothing"}
                        rdf_objects.append(rdf_o)
                        rdf_subjects.append(rdf_s)
                        one = {'name':'1',"rdf_objects":rdf_objects,"rdf_subjects":rdf_subjects, "type": "PushingOrPulling"}

        relations = {"0":zero, "1":one}              
        # relations['relations'] = zero, one
        
        elements = {"objects": objects, "relations": relations}           
        # elements['elements'] = objects, relations
        



        #Second block "frames"
        shapes = dict_data['shapes']
        shapeProperties = dict_data['shapeProperties']


        stream_name = dict_data['properties'].keys()
        stream_name = list(stream_name)
        stream_name = stream_name[1]

        frames = {}
        objects = {}

        for idd in shapes['CAM']['features']:
            maxX = idd['geometry']['coordinates']['maxX']['coordinates']
            maxY = idd['geometry']['coordinates']['maxY']['coordinates']
            minX = idd['geometry']['coordinates']['minX']['coordinates']
            minY = idd['geometry']['coordinates']['minY']['coordinates']
            c = []
            c.append(maxX)
            c.append(maxY)
            c.append(minX)
            c.append(minY)
            
            centerX = (c[0][0]+c[1][0]+c[2][0]+c[3][0])/4
            centerY = (c[0][1]+c[1][1]+c[2][1]+c[3][1])/4
            width = sqrt(((c[0][0]-c[2][0])**2)+((c[0][1]-c[2][1])**2))
            height = sqrt(((c[1][0]-c[3][0])**2)+((c[1][1]-c[3][1])**2))

            val =[]
            value = {}
            name = {}

            name_prefix = 'bbox-'
            rand = binascii.b2a_hex(os.urandom(4))
            rand = rand.decode("utf-8")

            val.append(centerX)
            val.append(centerY)
            val.append(width)
            val.append(height)
            value = {"val":val}
            
            
            name = {"name": (name_prefix+rand)}
            
            bbox_list = []
            box = {}
            obj = {}
            object_data = {}
            box = {'name': (name_prefix+rand), "stream": stream_name, "val":val}
            bbox_list.append(box)

            iddd = idd['id']
            obj = {iddd:{"object_data":{"bbox":bbox_list}}}
        
            txt = {}
            text_list = []
            text = {}

            if iddd in shapeProperties:
                if 'Unclear' in shapeProperties[iddd]["@all"]:
                    bol = {}
                    boolean_list = []
                    boolean = {}
                    bol = {"name":"Unclear", "val": shapeProperties[iddd]["@all"]["Unclear"]}
                    boolean_list.append(bol)
                    boolean = {"boolean":boolean_list}
                    obj.update (boolean)

                if 'ObjectType' in shapeProperties[iddd]["@all"]:
                    txt = {}
                    text_list = []
                    text = {}
                    txt = {"name":"ObjectType", "val": shapeProperties[iddd]["@all"]["ObjectType"]}
                    text_list.append(txt)
                    text = {"text":text_list}
                    obj.update (text)
            
            
            objects.update (obj)

        frames = {"":{"objects":objects}, "relations":{"0":{},"1":{}}}

        openlabel = {"elements":elements, "frames":frames}
        data = {"openlabel":openlabel}
        return data
       





