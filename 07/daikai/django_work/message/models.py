from django.db import models
import json


# Create your models here.
MESSAGE_FILE = 'messages.json'

def get_messages():
    fhandler = open(MESSAGE_FILE,'rt')
    cxt = fhandler.read()
    fhandler.close()
    return json.loads(cxt)

def save_messages(username, title, content, publish_date):
    messages = get_messages()
    messages.append({'username':username, 'title':title, 'content':content, 'publish_date':publish_date})
    fhandler = open(MESSAGE_FILE, 'wt')
    fhandler.write(json.dumps(messages))
    fhandler.close()
