from fbchat import Client
from fbchat.models import *

# get credentials
with open("credentials.txt", "r") as f:
	lines = f.readlines()
	username = lines[0].rstrip()
	password = lines[1].rstrip()
	my_uid = lines[2].rstrip()
f.close()

# open client
client = Client(username, password)

# send message
client.send(Message(text='Time to drink water!'), thread_id=my_uid, thread_type=ThreadType.USER)
client.logout()