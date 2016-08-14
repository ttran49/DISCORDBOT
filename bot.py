import discord
import sys,hashlib

###############################################################
#
#	BOT FOR DISCORD
#	music and shet
#	
###############################################################

#Compare has value for UserSetting to see if user change it.
# if left -> first run
# if change -> can read info for

#checking both MD5 and SHA1 hash

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

MD5hash="a91c0066275651b0a42e1d0dfc153d26"
SHA1hash="c8435a4ff311e43857a278eeaf70ce0613e77ecf"

#default hash value for the file
md5 = hashlib.md5()
sha1 = hashlib.sha1()

#getting current hash value for the file
with open("UserSetting.txt", 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)

#default token, login if wrong username, pwd, token provided
defaultToken="MjExMjAyNzMyOTEwOTY4ODMy.CoZ5aw.CTxXxFf6-ZxnWhLi9hRRSyJp5nM"

#Globals are gross, let's pass information with an object
#
#UserSettings object, manages our settings information
#
class UserSettings(object):
#Gets and sets for the fields
	def _setLoginMethod(self, method):
		self._LoginMethod = method
	def _getLoginMethod(self):
		return self._LoginMethod
	def _setToken(self, token):
		self._Token = token
	def _getToken(self):
		return self._Token
	def _setUsername(self, username):
		self._Username = username
	def _getUsername(self):
		return self._Username
	def _setPassword(self, password):
		self._Password = password
	def _getPassword(self):
		return self._Password
	def _setInvite(self, invite):
		self._Invite = invite
	def _getInvite(self):
		return self._Invite
#Property definitions

	loginMethod = property(_getLoginMethod, _setLoginMethod)
	token = property(_getToken, _setToken)
	username = property(_getUsername, _setUsername)
	password = property(_getPassword, _setPassword)
	invite = property(_getInvite, _setInvite)

#Method definitions

#We can read in the settings a little more dynamically or we can manually set them with properties
	def readUserSetting(settingsFile): #UserSetting.txt
		settingFile= open(settingsFile, 'r')
		for text in settingFile.readlines():
			things = text.split()
			if things[0] == 'Login_Method=':
				if things[1].lower() == 'token':
					UserSettings.loginMethod = "token"
				elif things[1].lower() == 'username':
					UserSettings.loginMethod = "username"
			elif things[0] == 'Token=' and UserSettings.loginMethod == "token":
				UserSettings.token = things[1]
			elif things[0] == 'Username=' and UserSettings.loginMethod == "username":
				UserSettings.username = things[1]
			elif things[0] == 'Password=' and UserSettings.loginMethod == "username":
				UserSettings.password = things[1]
			elif things[0] == 'Invite=':
				UserSettings.invite = things[1]
		settingFile.close()
###################################################################
#
#	Running first time set up, get infor from user. update fields
#	write it to UserSetting for future use
#
###################################################################
def firstTimeSetup(settings):
	print("First time running the bot, required information. Would you like to run the setup? Y/N")
	userInput = None
	while True:
		userInput=input()
		if userInput.lower() == 'y' or userInput.lower() == 'n':
			break
		else:
			print("Invalid input, please enter Y/N")
			
	#getting information
	if userInput.lower()=='y':
		print ("Login method: token or username and password?- T/U")
		while True:
			userInput=input()
			if userInput.lower() == 't':
				settings.loginMethod = "token"
				break
			elif userInput.lower() == 'u':
				settings.loginMethod = "username"
				break
			else:
				print ("Invalid input, T/U")
		if settings.loginMethod == "token":
			settings.token = input("Enter the token: ")
		elif settings.loginMethod == "username":
			settings.username= input("Enter Username: ")
			settings.password= input("Enter Password: ")
			
		settings.invite= input("Copy and Paste the Server Invite: ")
		
		#writtng the settings to the user file for future use
		settingFile= open('UserSetting.txt', 'w')
		if settings.loginMethod == "token":
			settingFile.write('Login_Method= token\n')
			settingFile.write('Token= ' + settings.token + '\n')
			settingFile.write('Username= \n')
			settingFile.write('Password= \n')
		else:
			settingFile.write('Login_Method= username\n')
			settingFile.write('Token= \n')
			settingFile.write('Username= '+ settings.username+'\n')
			settingFile.write('Password= '+ settings.password+'\n')
		settingFile.write('Invite= ' + settings.invite)
		settingFile.close()
	elif userInput.lower() =='n':
		try:
			settings.readUserSetting(UserSetting.txt)
		except:
			print("ERROR ---- make sure to put correct information in UserSetting.txt ")
###################################################################
#
#	Join a channel or server by invite
#
#	Exception:	HTTPException -  Accepting the invite failed.
#				NotFound  - The invite is invalid/expired
#	Exit when exception occurs
#				
###################################################################
def join_by_invite(Invite):
	try:
		print(Invite)
		bot.accept_invite(Invite)
		bot.send_message(message.channel, "The bot has joined!")
	except (discord.HTTPException, discord.NotFound):
		print("Failed to accept the invite, please check the invite URL, if the bot can join the channel or not")
		sys.exit(0)
###################################################################
#
#	Display in chat all the options for the bot
#
###################################################################	
def display_option():
	option= "Options for the bot: \n	!join: join a server or channel url that given by user\n		Ex: !join INVITE_URL\n	!help: displaying all options"
	bot.send_message(message.channel, option)
#check hash value
settings = UserSettings()
if MD5hash == md5.hexdigest() and SHA1hash==sha1.hexdigest():
	firstTimeSetup(UserSettings)
else:
	print("Reading those settings")
	UserSettings.readUserSetting("UserSetting.txt")

#creating an instance of a bot
bot=discord.Client()
#logging in
try:
	if UserSettings.loginMethod == "token":
		bot.login(UserSettings.token)
		print(UserSettings.token)
	else:
		bot.login(UserSettings.username, UserSettings.password)
except discord.LoginFailure:
	print("Failed to login -- Wrong Token or Username/Password")
	print("Logining in with default token ....")
	bot.login(defaultToken)
except discord.HTTPException:
	print(" An unknown HTTP related error occurred, usually when it isn’t 200 or the known incorrect credentials passing status code.")
	bot.close()
	sys.quit(0)
#joining a channel
try:
	join_by_invite(UserSettings.invite)
except:
	print("[-] Looks like we had some issues with the invite... Exiting")
	exit(0)

#####################################################################
#
#	Listen to user message to see if user give the bot any command
#	Command rule: start with ! and a action
#	Command:  	!join +"INVITE_URL"  - tell the bot to join a different channel or server
#				!help - displaying all the option, commands, and syntax
#
######################################################################
@client.event
def on_message(message):
	if message.content.startwith("!join"):
		join_by_invite(message.content.strip("!join "))
	if message.content.startswith("!help"):
		display_option()
bot.run()




