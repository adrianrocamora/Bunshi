import os

class Config(object):
    SECRET_KEY = os.urandom(24) # or "acetate"
