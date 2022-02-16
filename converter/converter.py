import json

class Convert():
    def converter(self, file_open, file_write):
        with open(file_open) as f: # become the annotel_1.json and save/convert it to dict
            data = json.loads(f.read()) 
    

        #Parsing the dict and take the values for the new format OpenLABEL 

    
        obj = open(file_write, 'w')  # Create a OpenLABEL json file and write the values for the new format
        data_json = json.dumps(data)
        obj.write(data_json)
        obj.close



# Test
a = Convert()
a.converter('converter/annotell_1.json', 'converter/data.json')