from discord.ext import commands
import discord
import os, sys, logging

############################
#
#	Creating custom exception
#
############################

class NotValidNameOrURL(Exception):
    pass

class DuplicateSongURL(Exception):
	pass
	
class PlaylistIsEmpty(Exception):
	pass
	

#
#	queue structures for storing music link
#	sone request/ and song queue/ playlist
#
class Playlist():
	__songs=[]
	
	__default_songs=['https://www.youtube.com/watch?v=zadjWitPrOs','https://www.youtube.com/watch?v=ws0PG-DYaHU','https://www.youtube.com/watch?v=a52Ul2AM92c','https://www.youtube.com/watch?v=szj59j0hz_4','https://www.youtube.com/watch?v=Vc8m6JLGgrc','https://www.youtube.com/watch?v=fZC-apS2ZrU','https://www.youtube.com/watch?v=VSk5JOg6nQQ','https://www.youtube.com/watch?v=s8XIgR5OGJc','https://www.youtube.com/watch?v=tmPm5iYOklg','https://www.youtube.com/watch?v=Ybmmys4nJOk','https://www.youtube.com/watch?v=PMUt0lShZfs','https://www.youtube.com/watch?v=0t2tjNqGyJI','https://www.youtube.com/watch?v=Z7CTnA3dTU0','https://www.youtube.com/watch?v=Ewr86bQB8Lc','https://www.youtube.com/watch?v=tdvpP21gNeM']
	__default_songs_index=0
	
	def __init__(self):
		pass	

	def addsong(song_name):
		#adding song to the playlist, check if there is a same song, if song
		#already in do not add.
		if !isinstance(song_name, basestring)
			raise NotValidNameOrURL()
			return None 
		#empty list
		if len(__songs) == 0:	
			__songs[0]=song_name
		else:
			if checkduplicate(song_name):
				raise DuplicateSongURL()
			else:
				__songs[len(__songs)]=song_name
		return song_name

	def nextsong():
		#empty playlist will add default playlist later
		if len(__songs) == 0:
			print ("empty playlist, switching to default playlist.....")
			output=__default_songs[__default_songs_index]
			__default_songs_index++
			return output
			
		output = __songs[0]
		move()
		return output

	def move(start, end):
		#after getting the some, remove the song and move all the other songs up
		if len(__songs) == 0:
			raise PlaylistIsEmpty()
			return False
		else:
			for i in (end-1):
				#skipping the first song or the starting index
				if i == 0 or i <= start:
					continue
				temp=__songs[i]
				__songs[i-1]=temp
			
			#clean up for space, delete the last song
			del __songs[-1]
		return True

	def checkduplicate(song_name):
	#check for duplicate song that is already existed in the playlist
	#False if there is not, True is there is a duplicate
		if len(__songs)==0:
			return False
		for i in __songs:
			if i is song_name:
				return True
		return False

	def currentsong():
		#return the current song as a string. url
		if lens(__songs)==0:
			return __default_songs[__default_songs_index]
		return __songs[0]

	def printallsong():
		#print out all the songs that are in the playlist
		for i in __songs:
			print i
		return 
	
	def size():
		#return the current number of songs in the playlist
		return len(__songs)
		
	def removethsong(index):
		#removing the xTH song from the list.
		if len(__songs)== 0:
			return None
		else 
			del __songs[index]
			move(index,len(__songs))
	
	def removelastsong():
		#remove the lastest or last song that was added to the playlist
		if len(__songs) == 0:
			raise PlaylistIsEmpty()
		else
			del __songs[-1]
	
	def clear():
		#remove all songs and clear the playlist
		del __songs[:]