import soundcloud

def get_auth():
	client = soundcloud.Client(
		client_id = 'YOUR_ID',
		client_secret = 'YOUR_SECRET',
		scope = 'non-expiring',
		username = 'YOU@EMAIL.COM',
		password = 'YOUR_PWD'
	)

	print 'Hello, ' + client.get('/me').username + '!'
	return client
