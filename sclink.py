import oauth_me
import upload
import os
from utils import monitor, sc
import upload

client = oauth_me.get_auth() #implement your own oauth_me or change to ouath with your own creds

#upload.upload_track( client, 'Pirates.mp3' )
#monitor.start()
#monitor.stop()

sc.get_title('~/Music/song.mp3')
