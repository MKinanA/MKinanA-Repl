from flask import make_response

def textify(text, mimetype='text/plain', code=200):
    toreturn = make_response(text, code)
    toreturn.mimetype = mimetype
    return toreturn