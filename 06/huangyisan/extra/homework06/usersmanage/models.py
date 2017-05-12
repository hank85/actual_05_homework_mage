from django.db import models
import json
MESSAGE_FILE = 'user_db'
def get_messages():
    fhandler = open(MESSAGE_FILE,'rt')
    context = fhandler.read()
    fhandler.close()
    return json.loads(context)

