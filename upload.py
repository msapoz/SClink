import soundcloud
import re
import os

dir = '~/Music/' #set this to your desired soundcloud dir

def upload_track( client, newTrack ):
	print dir + newTrack
	track = client.post('/tracks', track={
    		'title': get_title( newTrack ) ,
    		'sharing': 'private',
    		'asset_data': open(os.path.expanduser(dir + newTrack), 'rb')
	})
	print track.title + ' has been posted!'
	print 'The secret URL is ' + track.permalink_url + '/' + track.secret_token

def get_title ( newTrack ):
	exp = re.compile('\A[\w-]*') #extract track title from file name, remove dot extension, currently cannot use '.' in filename
	return exp.match(newTrack).group()
