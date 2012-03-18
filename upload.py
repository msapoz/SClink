import soundcloud
import re

dir = '~/Music/'

def upload_track( client, newTrack ):
	print dir + newTrack
	track = client.post('/tracks', track={
    		'title': get_title( newTrack ) ,
    		'sharing': 'private',
    		'asset_data': open(dir + newTrack, 'rb')
	})
	print track.title + ' has been posted!'

def get_title ( newTrack ):
	exp = re.compile('\A[\w-]*')
	return exp.match(newTrack).group()
