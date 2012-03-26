import oauth_me
import upload
import os
from utils import monitor

client = oauth_me.get_auth()

#upload.upload_track( client, 'Pirates.mp3' )
monitor.start()
monitor.stop()
