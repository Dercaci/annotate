This app is composed from 3 parts:
    1. Client
    2. Server
    3. Converter

1. The client is an installable package from pypi, to install it run "pip3 install  client_dercaci"   
    The client becoms an annotell.json file, opens it and send to server his body like a POST body request,
    recives a response with converted text to openlabel format, and creates in its own repository a file openlabel.json
    * the file annotell_1.json have to be in the client repository like in my example

2. The server is a simple FastAPi route, he recives the body json text in format annotell, converted it to openlabel and give the 
    response to the client with the openlabel format

3. The converter is imported in server and he converted the recived annotell format to openlabel


To run the project:
    1. run "pip3 install requirements.txt"
    2. run the server "uvicorn main:app "
    3. run the client 

