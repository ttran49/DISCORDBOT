from discord.ext import commands
import discord, pafy
import os, sys, logging

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
	playlist= Playlist();
	
	def __init__(self, voice_channel):
		self.voice_channel = voice_channel
	
	
	def add_song_to_playlist():
		song_url=input("Please enter a song URL: ")
		try:
			playlist.addsong(song_url)
		except Playlist.DuplicateSongURL:
			print("Song already exists in the playlist")
		except Playlist.NotValidNameOrURL:
			print("Not a valid input, must be a string of a song url")
	
	def play():
		if (playlist.size() == 0):
			raise EmptyPlaylist()
		