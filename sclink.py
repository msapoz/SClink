import oauth_me
import upload
import os
from fsevents import Observer,Stream

client = oauth_me.get_auth()

#upload.upload_track( client, 'Pirates.mp3' )

def test_event( event ):
	 print "Mask: %s, Cookie: %s, Name: %s" % (event.mask, event.cookie, event.name)

obs = Observer()
obs.start()

stream = Stream( test_event, 'test', 


#Poll directory for new music

#if new music exists, upload music to directory
	#growl notification of new music uploaded to soundcloud	
