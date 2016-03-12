from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import datetime

class WelcomePage(webapp.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = "text/html"
		self.response.out.write("""<html>
						<head>
						  <title> Welcome to Krishnath chat service </title>
						</head>
						 <body>
						  <h1>Welcome to the chat Service of Krishnath Sankaran</h1>
						  <p1>The current date is : %s</p1>
						</body>
						</html>""" %(datetime.datetime.now()))


chatapp = webapp.WSGIApplication([('/',WelcomePage)])
def main():
	run_wsgi_app(chatapp)


if __name__ == "__main__":
	main()

