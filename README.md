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

### Get Comments

URL: /<roseid>/comments

Method: GET

Returns: string list

Comment: A GET request to /<roseid>/comments returns a list of comments as strings associated with the particular roseid.

### Add Comment

URL: /<roseid>/addComment

Method: POST

Returns: bool

Comment: A POST request to /<roseid>/addComment must include a "comment" paramter in order to succeed. Failure to do so triggers a 400-level HTTP error. A valid request attempts to add the value of the "comment" parameter to the database for the particular roseid. It returns a bool describing whether the operation succeeded.