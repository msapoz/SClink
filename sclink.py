import oauth_me
import upload

client = oauth_me.get_auth()

upload.upload_track( client, 'Pirates.mp3' )


#Poll directory for new music

#if new music exists, upload music to directory
	#growl notification of new music uploaded to soundcloud	
