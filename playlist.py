from discord.ext import commands
import discord, pafy
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
	__songs__=[]
	
	def __init__(self):
		pass
		

	def addsong(song_name):
		#adding song to the playlist, check if there is a same song, if song
		#already in do not add.
		if !isinstance(song_name, basestring)
			raise NotValidNameOrURL()
			return None 
		#empty list
		if len(songs) == 0:	
			songs[0]=song_name
		else:
			if checkduplicate(song_name):
				raise DuplicateSongURL()
			else:
				songs[len(songs)]=song_name
		return song_name

	def nextsong():
		#empty playlist will add default playlist later
		if len(songs) == 0:
			raise PlaylistIsEmpty()
			output = songs[0]
			move()
			return output

	def move(start, end):
		#after getting the some, remove the song and move all the other songs up
		if len(songs) == 0:
			raise PlaylistIsEmpty()
			return False
		else:
			for i in (end-1):
				#skipping the first song or the starting index
				if i == 0 or i <= start:
					continue
				temp=songs[i]
				songs[i-1]=temp
			
			#clean up for space, delete the last song
			del songs[-1]
		return True

	def checkduplicate(song_name):
	#check for duplicate song that is already existed in the playlist
	#False if there is not, True is there is a duplicate
		if len(songs)==0:
			return False
		for i in songs:
			if i is song_name:
				return True
		return False

	def currentsong():
		#return the current song as a string. url
		if lens(songs)==0:
			return None
		return songs[0]

	def printallsong():
		#print out all the songs that are in the playlist
		for i in songs:
			print i
		return 
	
	def size():
		#return the current number of songs in the playlist
		return len(songs)
		
	def removethsong(index):
		#removing the xTH song from the list.
		if len(songs)== 0:
			return None
		else 
			del songs[index]
			move(index,len(songs))
	
	def removelastsong():
		#remove the lastest or last song that was added to the playlist
		if len(songs) == 0:
			raise PlaylistIsEmpty()
		else
			del songs[-1]
	
	def clear():
		#remove all songs and clear the playlist
		del songs[:]