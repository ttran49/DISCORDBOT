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

#GLOBAL VARIABLE I GUESS, dont know python prob
LoginbyTok=None
#default token, login if wrong username, pwd, token provided
defaultToken="MjExMjAyNzMyOTEwOTY4ODMy.CoZ5aw.CTxXxFf6-ZxnWhLi9hRRSyJp5nM"
Username=None
Password=None
Token=None
Invite= None
	
#################################################################
#
#	Reading the settings from UserSetting.txt file
#
#################################################################
def readUserSetting():
	settingFile= open('UserSetting.txt', 'r')
	for text in settingFile.readlines():
		things = text.split()
		if things[0] == 'Login_Method=':
			if things[1].lower() == 'token':
				LoginbyTok=True
			elif things[1].lower() == 'username':
				LoginbyTok= False
		elif things[0] == 'Token=' and LoginbyTok:
			Token=things[1]
		elif things[0] == 'Username=' and not LoginbyTok:
			Username= things[1]
		elif things[0] == 'Password=' and not LoginbyTok:
			Password= things[1]
		elif things[0] == 'Invite=':
			Invite=things[1]
	settingFile.close()
	
###################################################################
#
#	Running first time set up, get infor from user. update fields
#	write it to UserSetting for future use
#
###################################################################
def fristTimeSetup():
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
				LoginbyTok=True
				break
			elif userInput.lower() == 'u':
				LoginbyTok=False
				break
			else:
				print ("Invalid input, T/U")
		if LoginbyTok:
			Token= input("Enter the token: ")
		elif not LoginbyTok:
			Username= input("Enter Username: ")
			Password= input("Enter Password: ")
			
		Invite= input("Copy and Paste the Server Invite: ")
		
		#writtng the settings to the user file for future use
		settingFile= open('UserSetting.txt', 'w')
		if LoginbyTok:
			settingFile.write('Login_Method= token\n')
			settingFile.write('Token= ' + Token + '\n')
			settingFile.write('Username= \n')
			settingFile.write('Password= \n')
		else:
			settingFile.write('Login_Method= username\n')
			settingFile.write('Token= \n')
			settingFile.write('Username= '+Username+'\n')
			settingFile.write('Password= '+Password+'\n')
		settingFile.write('Invite= ' + Invite)
		settingFile.close()
	elif userInput.lower() =='n':
		try:
			readUserSetting()
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
def join_by_invite(invite):
	try:
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
if MD5hash == md5.hexdigest() and SHA1hash==sha1.hexdigest():
	fristTimeSetup()
else:
	readUserSetting()

#creating an instance of a bot
bot=discord.Client()
#logging in
try:
	if LoginbyTok:
		await client.login(Token)
	else:
		await client.login(Username, Password)
except discord.LoginFailure:
	print("Failed to login -- Wrong Token or Username/Password")
	print("Logining in with default token ....")
	client.login(defaultToken)
except discord.HTTPException:
	print(" An unknown HTTP related error occurred, usually when it isn’t 200 or the known incorrect credentials passing status code.")
	sys.quit(0)
#joining a channel
join_by_invite(Invite)

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




