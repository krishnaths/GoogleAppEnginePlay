import datetime
import sys
class ChatRoom(object):
	"""A chatroom"""
	rooms= {}
	
	def __init__(self, name):
		self.name = name
		self.users = []
		self.messages = []
		ChatRoom.rooms[name] = self #Adding the name of itself to its variable called rooms

	def addSubscriber(self, subscriber):
		self.users.append(subscriber)
		subscriber.sendMessage(self.name, "User %s has entered ." % subscriber.username)
	
	def removeSubscriber(self, subscriber):
		if subscriber in self.users:
			subscriber.sendMessage(self.name, "User % is leaving." % subscriber.username)
			self.users.remove(subscriber)
	
	def addMessage(self, msg):
		self.messages.append(msg)
	
	def printMessage(self, out):
		print >> out, "Chat transcript for : %s" % self.name
		for i in self.messages:	
			print >> out, i
	


class ChatUser(object):
	"""A user participating in chats"""
	
	def __init__(self, username):
		self.username = username
		self.rooms = {}

	def subscribe(self, roomname):
		if roomname in ChatRoom.rooms:
			room = ChatRoom.rooms[roomname]
			self.rooms[roomname] = room
			room.addSubscriber(self)
		else:
			raise ChatError("No such room %s" % roomname)

	def sendMessage(self, roomname,text):
		if roomname in self.rooms:
			room = self.rooms[roomname]
			cm = ChatMessage(self, text)
			room.addMessage(cm)
		else:
			raise ChatError("User %s not subscribed to chat %s" % (self.username, roomname))
	
	def displayChat(self, roomname, out):
		if roomname in self.rooms:
			room = self.rooms[roomname]
			room.printMessage(out)
		else:
			raise ChatError("User %s not subscribed to chat %s" % (self.username, roomname))


class ChatMessage(object):
	"""A single message sent by a user to a chatroom"""
	def __init__(self, user, text):
		self.sender = user
		self.msg = text
		self.time = datetime.datetime.now()


	def __str__(self):
		return "From %s at %s : %s" % (self.sender.username, self.time, self.msg)



def main():
	room = ChatRoom("Main")
	
	markcc = ChatUser("MarkCC")	
	
	markcc.subscribe("Main")
	prag = ChatUser("Prag")
	prag.subscribe("Main")
	
	markcc.sendMessage("Main", "Hello is there anybody out there?")
	prag.sendMessage("Main", "Yes, I'm out here.")
	markcc.displayChat("Main", sys.stdout)


if __name__ == "__main__":
	main()						
		
						
		
