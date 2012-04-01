#fsevents class wrapper
from fsevents import Observer, Stream

class Monitor:

	def __init__( self ):
		self.obs = Observer()
		self.stream = Stream ( self.callback, 'test', file_events=True )

	def callback( event ): #file event callback function
		print event.name + ' changed'

	def start( self ):
		print "in start"
		self.obs.start()
		self.obs.schedule( self.stream )

	def stop( self ):
		print "in stop"
		self.obs.unschedule( self.stream )
		self.obs.stop()

monitor = Monitor() 

#soundcloud utilities
import soundcloud
import re
import os

class SoundCloud:

	def __init__( self, dir ):
		self.dir = dir #specified music directory
		
	def upload_track( self, client, newTrack ):
		print dir + newTrack
		track = client.post('/tracks', track={
    			'title': get_title( newTrack ) ,
    			'sharing': 'private',
    			'asset_data': open(os.path.expanduser(dir + newTrack), 'rb')
		})
		print track.title + ' has been posted!'
		print 'The secret URL is ' + track.permalink_url + '/' + track.secret_token

	def get_title( self, newTrack ):
		exp = re.compile( '[\w-]*\.' )
		print exp.search( newTrack ).group().strip('.')

sc = SoundCloud( '~/Music/' ) 
