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
	
	#Constructor, get the client or bot object from bot.py
	def __init__(self, voice_channel, client_object):
		self.voice_channel = voice_channel
		self.client_object = client_object
	
	#adding a new song to playlist
	#
	#	Expected exception:
	#		Playlist.DuplicateSongURL - Song/URL already exists
	#		Playlist.NotValidNameOrURL - Song/URL not in valid format aka String
	def add_song_to_playlist():
		song_url=input("Please enter a song URL: ")
		try:
			playlist.addsong(song_url)
		except Playlist.DuplicateSongURL:
			print("Song already exists in the playlist")
		except Playlist.NotValidNameOrURL:
			print("Not a valid input, must be a string of a song url")
	
	def __create_a_stream(playlist):
		voice = client_object.join_voice_channel(voice_channel)
		player=None
		if "youtube" in playlist.currentsong():
			player= voice.create_ytdl_player(playlist.currentsong())
		elif "soundcloud" in playlist.currentsong():
			#player=
		return player
		
	#Take the bot object create a stream to play music from youtube
	# TODO: create one for soundcloud
	def play():
		if (playlist.size() == 0):
			raise EmptyPlaylist()
		#play the music
		for i in (playlist.size()-1):
			player = __create_a_stream(__playlist)
			player.start()
			__is_playing=True
			if player.is_done():
				__playlist.nextsong()
		__is_playing=False
		
	# TODO: figure out how to implement pause and resume with the current
	# variable scope
	def pause():
		if not __is_playing:
			__Pausing=True
			
		else:
			print("No song is currently playing")
		
	def resume():
		if not __Pausing:
			__Pausing=False
			
		else:
			print("Song is already paused")
	
	def skipsong():
		__playlist.removethsong(0)
		play()
	
	