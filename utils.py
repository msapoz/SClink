#soundcloud utilities
import soundcloud
import oauth_me
import re
import os

SOURCE_PATH = os.path.expanduser('~/Music/')
VALID_SUFFIX = '.mp3';

class SoundCloud:

	def __init__( self ):
		self.client = oauth_me.get_auth()

	def upload_track( self, newTrack ):
		track = self.client.post('/tracks', track={
    			'title': get_title(newTrack),
    			'sharing': 'private',
    			'asset_data': open(os.path.expanduser( newTrack ), 'rb')
		})
		print track.title + ' has been posted!'
		print 'URL: ' + track.permalink_url + '/' + track.secret_token

sc = SoundCloud()

#fsevents class wrapper
from fsevents import Observer, Stream

class Monitor:

	def __init__( self ):
		self.obs = Observer()
		self.stream = Stream ( self.callback, SOURCE_PATH, file_events=True )

	def callback( self, event ): #file event callback function
		if event.name.endswith( VALID_SUFFIX ) and os.path.isfile( event.name ):
			sc.upload_track ( event.name )

	def start( self ):
		print "Starting monitor..."
		self.obs.start()
		self.obs.schedule( self.stream )

	def stop( self ):
		print "Stopping monitor..."
		self.obs.unschedule( self.stream )
		self.obs.stop()

monitor = Monitor()

def get_title( newTrack ):
	exp = re.compile( '[\w-]*\.' )
	return exp.search( newTrack ).group().strip('.')
