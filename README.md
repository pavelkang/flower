Rose Gram Facebook App - TartanHacks 2015
=========================================
Well played.

Local Installation
------------------

To run the app locally, install dependencies (ideally in a virtualenv) with

`pip install -r requirements.txt`

Then you can run the server with

`python main.py`

If you hate yourself or are named Heroku, use

`gunicorn main:app`

API
---
For internal use only...as if you're really going to listen to that.

### Create Rose

URL: /createRose

Method: POST

Returns: number

Comment: A POST request to /createRose creates a rose object in the database and returns the id of the object created for future requests to this API.