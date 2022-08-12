# Example using http_cli

This folder contains a node.js application and an example python script that uses http_cli to start it, run one request/response, then stop it.

First build the node.js application:

    npm install

Put http_cli on your PYTHONPATH, eg

     $Env:PYTHONPATH = "C:\Users\Administrator\workspace\http_to_cli\"

run the python script:

    python example_usage.py

This should produce output like this:

    starting Example Application on url http://localhost:49408
    starting server
    found http method GET for url /
    stopping server

It should also create three files in the current working directory: response_status_code.txt, response_headers.txt and response_body.txt

