import time
import os

class TimeManager:
	"The time manager class"
	
	sessionActive = False
	sessionStart = ''
	sessionEnd = ''

	def __init__(self):
		print("Time Manager Initialized") 

	
	
	def saveDataOpen(self):
		fileName = 'Logs/{}'.format(time.strftime("%d-%m-%Y"))+'.txt'
		if os.path.exists(fileName):
			fileOpenType = 'a'
		else:
			fileOpenType = 'w'

		try:
			newFile = open(fileName, fileOpenType)
			newFile.write("\n---------------------\n")
			title = str("Session - {}".format(time.strftime("%d-%m-%Y")))
			content = str("\nSession Opened - {}\n".format(time.strftime("%H:%M:%S")))
			newFile.write(title)
			newFile.write(content)
			newFile.close()
			self.sessionStart = time.time()
		except:
			raise Exception("An error occurred opening a new session.")
		finally:
			print("Session Opened!")

	def saveDataClose(self):
		fileName = 'Logs/{}'.format(time.strftime("%d-%m-%Y"))+'.txt'
		if os.path.exists(fileName):
			fileOpenType = 'a'
		else:
			print("\nAn error occurred saving the session. This usually occurs when a session starts without the system acknowledging it.")
			print("Please contact the developer about this issue!\n")


		try:
			newFile = open(fileName, 'a')
			content = str("Session Closed - {}\n".format(time.strftime("%H:%M:%S")))
			newFile.write(content)
			
			self.sessionEnd = time.time()
			totalElapsedTime = self.sessionEnd - self.sessionStart
			newFile.write("Total Time: {0:.2f} minutes\n".format(totalElapsedTime/60))

			newFile.write("---------------------\n")
			newFile.close()
		except:
			raise Exception("An error occurred saving the current session.")
		finally:
			print("Session Saved!")
		
	def startSession(self):
		if(self.sessionActive == False):
			self.sessionActive = True
			self.saveDataOpen()
		else:
			print("\nSession is already active!\n")

	def closeSession(self):
		if(self.sessionActive == True):
			self.sessionActive = False
			self.saveDataClose()
		else:
			print("\nThere is no active session available!\n")