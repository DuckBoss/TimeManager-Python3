import time
import sys
import TimeManager

class Interface:
	showUI = True
	program = TimeManager.TimeManager()

	def __init__(self):
		print("Interface Initialized")

	def MainUI(self):
		while(self.showUI):
			print("-----------------------------------")
			print("\t==== MENU ====")
			print("-----------------------------------")
			print("\t### Commands ###\n"
				"\tStart Session - [Start/start]\n"
				"\tEnd Session - [End/end]\n"
				"\tQuit - [Quit/quit]\n")
			inp = input("Input - ").upper().strip()

			if(inp == "START"):
				print("Starting Session...\n")
				self.program.startSession()
				self.showUI = False

			if(inp == "END"):
				print("Ending Session...\n")
				self.program.closeSession()
				self.showUI = False

			if(inp == "QUIT"):
				self.program.closeSession()
				print("Closing Program...\n")
				sys.exit(0)

def main():
	print("Program Started - {}".format(time.strftime("%d-%m-%Y[%H:%M:%S]")))
	interface = Interface()
	while(True):
		print("Press any key to open menu")
		input()
		interface.showUI = True
		interface.MainUI()



if __name__ == "__main__":
	main()