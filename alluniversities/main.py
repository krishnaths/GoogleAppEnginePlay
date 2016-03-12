import datetime
from Model import uni_usa
from Model import trigger
import time

print 'Content-Type: text/html'
print ''
print '<p> The time is %s</p>' % str(datetime.datetime.now())


query = uni_usa.all()
for result in query.run(limit=10):
	print '<p><a href="http://%s">%s</a></p>' % (result.website.encode('utf-8'), result.name.encode('utf-8'))
	print '----'


