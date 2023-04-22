from flask import Flask                     # from the flask module import the Flask class

app = Flask(__name__)                       # create an instance of Flask into our variable app
                                            # from here on out, "app" is now an "object"

@app.get("/")                               # we can now user or object's method "get" as a decorator.
def index():                                # a decorator wraps a function (more on this in a bit)
    me = {                                  # create a new dictionary with key/value pairs.
        "first_name": "Fernanda",           
        "last_name": "Murillo",
        "hobbies": "Something",
        "is_active": True
    }

    return me                               # when  you return a dictionary from a view function,
                                            # flask automatically converts in to JSON fon compatibility. 
