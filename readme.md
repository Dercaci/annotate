The project has a simple structure, annotell.json --> server/converter --> openlabel.json;

*   First step is create a virtual environement and install requirements.txt
    For start the project you have to run "uvicorn main:app --reload" command in your terminal, with this command starts the server;
    The next step is to open Postman and send a POST request on "127.0.0.1:8000/convert" with the annotell.json file in body;
    You will recive as response an another json file in OpenLabel format.


  # The project is not ready, I have to fisnish the converter and build it in the pypi