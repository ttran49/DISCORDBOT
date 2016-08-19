from discord.ext import commands
import discord
import os, sys, logging
import asyncio

class EmptyPlaylist(Exception):
	pass

class Audio
	"Play music, stream music"
	###############################################
	#
	#	Constructor, must pass in the voice channel
	#
	###############################################
	
	#creating an instance of playlist
	__playlist= Playlist();
	__is_playing=False
	__Pausing==False
	__player=None
	
	#Constructor, get the client or bot object from bot.py
	def __init__(self, voice_channel, client_object):
		self.voice_channel = voice_channel
		self.client_object = client_object
	
	###################################################################
	#
	#	Adding a new song to playlist
	#	Expected exception:
	#		Playlist.DuplicateSongURL - Song/URL already exists
	#		Playlist.NotValidNameOrURL - Song/URL not in valid format aka String
	#
	######################################################################3
	def add_song_to_playlist(song_url):
		try:
			playlist.addsong(song_url)
		except Playlist.DuplicateSongURL:
			print("Song already exists in the playlist")
		except Playlist.NotValidNameOrURL:
			print("Not a valid input, must be a string of a song url")
	
	##########################################################
	#
	#	Create a stream for play(). 
	#	Return: None if the URL is not from youtube or soundcloud
	#	TODO: create one for soundcloud 
	#
	##########################################################
	def __create_a_stream(playlist):
		voice = client_object.join_voice_channel(voice_channel)
		player=None
		
		#YOUTUBE
		if "youtube" in playlist.currentsong():
			player= voice.create_ytdl_player(playlist.currentsong())
		#SOUNDCLOUD
		elif "soundcloud" in playlist.currentsong():
			#player=
		return player
	
	#########################################################
	#
	#	Start to play songs
	#
	#########################################################
	def play():
		if (playlist.size() == 0):
			raise EmptyPlaylist()
		#play the music
		for i in (playlist.size()-1):
			__player = __create_a_stream(__playlist)
			__player.start()
			__is_playing=True
			if player.is_done():
				__playlist.nextsong()
		__is_playing=False
		
	########################################################
	#
	#	Pause the current song if is playing
	#
	########################################################
	def pause():
		if not __is_playing and not (__player is None):
			__Pausing=True
			__player.pause()
		else:
			print("No song is currently playing")
	
	###################################################
	#
	#	Resume the song if paused or was playing	
	#
	###################################################
	def resume():
		if not __Pausingand not (__player is None):
			__Pausing=False
			__player.resume()
		else:
			print("Song is already paused")
			
	###################################################
	#
	#	Set the volume, must run play() once before run this
	#	1.0 = 100%, 2.0 = 200%. Default = 1.0/100%
	#	if pass in number which is negative or >2 => set to default volume
	#
	###################################################
	def set_volume(number):
		if __player is None:
			print ("Player does not exist, call play() before call set_volume")
			return None
		if number.is_interger():
			if number > 0 and number <= 2:
				__player.volume(float(number))
				return None
			else:
				__player.volume(1.0)
				return None
	
	####################################################
	#
	#	Skip the current song 
	#
	####################################################
	def skipsong():
		__playlist.removethsong(0)
		play()