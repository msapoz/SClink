import oauth_me
import upload

client = oauth_me.get_auth()

upload.upload_track( client, 'Pirates.mp3' )

#tracks = client.get('/me/tracks/')
#for track in tracks:
#    print track.title + '-' + track.asset_data

#Poll directory for new music

#if new music exists, upload music to directory
	#growl notification of new music uploaded to soundcloud	
