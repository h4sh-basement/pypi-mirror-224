import socket, threading, time, sys, hashlib, json, base64, struct, io, multiprocessing, os, datetime
from pathlib import Path
import traceback

# important todo: wat ?
# (this library simply has to be a proper package)
sys.path.append(str(Path(__file__).parent))

from base_room import base_room
import jag_util

from easy_timings.mstime import perftest



# Path
# jag_util
# socket
# threading
# time
# sys
# hashlib
# json
# base64
# struct
# io
# multiprocessing
class pylib_preload:
	"""
	Precache python libraries.
	Cry all you want, but this reduces disk load
	"""
	def __init__(self):
		import socket
		import threading
		import time
		import sys
		import hashlib
		import json
		import base64
		import struct
		import io
		import multiprocessing
		import traceback
		import urllib
		import math
		import datetime

		from pathlib import Path

		import jag_util

		self.jag_util =  jag_util

		self.Path =      Path
		self.socket =    socket
		self.threading = threading
		self.time =      time
		self.sys =       sys
		self.hashlib =   hashlib
		self.json =      json
		self.base64 =    base64
		self.struct =    struct
		self.io =        io
		self.traceback = traceback
		self.urllib =    urllib
		self.math =      math
		self.datetime =  datetime




# sysroot         = Path-like pointing to the root of the jag package
# pylib           = A bunch of precached python packages
# mimes           = A dictionary of mime types; {file_ext:mime}
#                   | regular = {file_ext:mime}
#                   | signed =  {.file_ext:mime}
# response_codes  = HTTP response codes {code(int):string_descriptor}
# reject_precache = HTML document which sez "access denied"
# cfg             = Server Config
# doc_root        = Server Document Root
# list_dir        = List directory as html document
class server_info:
	"""
	Server info.
	This class contains the config itself,
	some preloaded python libraries,
	and other stuff
	"""
	def __init__(self, init_config=None):
		from mimes.mime_types_base import base_mimes
		from mimes.mime_types_base import base_mimes_signed
		from response_codes import codes as http_response_codes

		from pathlib import Path
		import jag_util, io, platform

		self.devtime = 0

		self.tstamp = None

		config = init_config or {}

		# root of the python package
		self.sysroot = Path(__file__).parent

		# extend python paths with included libs
		sys.path.append(str(self.sysroot / 'libs'))

		# mimes
		self.mimes = {
			'regular': base_mimes,
			'signed': base_mimes_signed,
		}

		# HTTP response codes
		self.response_codes = http_response_codes

		# Reject html document precache
		self.reject_precache = (self.sysroot / 'assets' / 'reject.html').read_bytes()




		#----------------
		# Base config
		#----------------
		self.cfg = {
			# Port to run the server on
			'port': 0,

			# Document root (where index.html is)
			'doc_root': None,

			# This path should point to a python file with "main()" function inside
			# If nothing is specified, then default room is created
			'room_file': None,

			# Could possibly be treated as bootleg anti-ddos/spam
			'max_connections': 0,

			# The amount of workers in the pool
			'pool_size': os.cpu_count()*2,

			# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Server-Timing
			'enable_web_timing_api': False,

			# The name of the html file to serve when request path is '/'
			'root_index': None,
			'enable_indexes': True,
			'index_names': ['index.html'],
		} | config

		self.doc_root = Path(self.cfg['doc_root'])


		#----------------
		# Directory Listing
		# ----------------
		self.cfg['dir_listing'] = {
			'enabled': False,
			'dark_theme': False,
		} | (config.get('dir_listing', {}))



		# ----------------
		# Advanced CDN serving (not implemented)
		# ----------------
		self.cfg['static_cdn'] = {
			# Path to the static CDN
			# can point anywhere
			'path': None,
			# Relieve the filesystem stress by precaching items inside this folder
			# only useful if folder contains a big amount of small files
			'precache': True,
			# An array of paths relative to the root cdn path
			# to exclude from caching
			'cache_exclude': [],
			# Glob pattern for caching files, default to '*'
			'pattern': None,
			# Wether to trigger the callback function
			# when incoming request is trying to access the static CDN
			'skip_callback': True,
		} | (config.get('static_cdn', {}))

		self.cdn_path = None
		self.cdn_cache = {}

		if self.cfg['static_cdn']['path']:
			self.cdn_path = Path(self.cfg['static_cdn']['path'])
			self.precache_cdn()



		# ----------------
		# Buffer sizes
		# ----------------
		self.cfg['buffers'] = {
			# Max file size when serving a file through built-in server services
			# Default to 8mb
			'max_file_len': (1024**2)*8,

			# Max size of the header buffer
			# Default to 512kb
			'max_header_len': 1024*512,

			# Default size of a single chunk when streaming buffers
			# Default to 5mb
			'bufstream_chunk_len': (1024**2)*5,
		} | (config.get('buffers', {}))



		# ----------------
		# Logging
		# ----------------

		# default log dirs
		logdir_selector = {
			'linux': Path('/var/log/jag'),
			'windows': Path(Path.home() / 'AppData' / 'Roaming' / 'jag' / 'log'),
		}
		self.cfg['logging'] = {
			# whether to enable file logging feature or not
			# this does not prevent the logging server from starting
			# log messages are simply not being sent to the server
			'enabled': True,

			# path to the folder where logs are stored
			# Linux default: /var/log/jag
			# Windows default: %appdata%/Roaming/jag/log
			'logs_dir': None,

			# The RPC port of the logger
			'port': None,
		} | (config.get('logging', {}))

		# ensure the de3fault folder exists
		if self.cfg['logging']['logs_dir'] == None:
			self.cfg['logging']['logs_dir'] = logdir_selector[platform.system().lower()]
			self.cfg['logging']['logs_dir'].mkdir(parents=True, exist_ok=True)



		# ----------------
		#    Websockets
		# ----------------
		self.cfg['websockets'] = {
			# WSS config.

			# What to do with a WSS request:
			# ! CASE SENSITIVE !
			#     - 'redirect': Respond with a HTTP redirect pointing to an
			#                   absolute URL specified in 'redirect_to',
			#                   e.g. '142.250.203.206:35852'
			#     - 'reject':   Terminate the connection immediately upon
			#                   discovering it's a WSS request.
			#     - 'accept':   Enable WSS.
			'action': 'reject',

			# Redirect WSS requests to this absolute URL.
			'redirect_to': None,

			# port to serve websockets on
			'wss_port': None,

			# just like room file in the base config, but 'main' function
			# should be designed to work with websockets
			'wss_file': None,

		} | (config.get('websockets', {}))





	def reload_libs(self):
		# preload python libraries
		self.pylib = pylib_preload()




_server_proc = '[Server Process]'
def sock_server(sv_resources):
	print(_server_proc, 'Binding server to a port... (5/7)')
	# Port to run the server on
	# port = 56817
	port = sv_resources.cfg['port']
	# Create the Server object
	skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind server to the specified port. 0 = Find the closest free port and run stuff on it
	# todo: is this really the only way to bind stuff to the current IP ?
	# update: there's some absolutely bizzare piece of code from a random website which does the trick
	# can it be trusted though ?
	"""
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _skt_get_ip:
		_skt_get_ip.connect(('8.8.8.8', 0))
		# _skt_get_ip.connect(('10.255.255.255', 1))
		current_ip = _skt_get_ip.getsockname()[0]
	"""

	skt.bind(
		(jag_util.get_current_ip(), port)
	)

	# Basically launch the server
	# The number passed to this function identifies the max amount of simultaneous connections
	# If the amount of connections exceeds this limit -
	# connections become rejected till other ones are resolved (aka closed)
	# 0 = infinite
	skt.listen(sv_resources.cfg['max_connections'])

	print(_server_proc, 'Server listening on port (6/7)', skt.getsockname()[1])

	print(_server_proc, 'Accepting connections... (7/7)')
	while True:
		conn, address = skt.accept()
		sv_resources.devtime = time.time()
		threading.Thread(target=base_room, args=(conn, address, sv_resources), daemon=True).start()



def logger_process(sv_resources, sock_obj):
	import jag_logging
	jag_logging.gestapo(sv_resources, sock_obj)


def wss_server(sv_resources):
	pass



_main_init = '[root]'
def server_process(launch_params, stfu=False):
	os.environ['_jag-dev-lvl'] = '1'

	# try overriding dev level
	try:
		os.environ['_jag-dev-lvl'] = str(int(launch_params['console_echo_level']))
	except Exception as e:
		pass

	# Preload resources n stuff
	print(_main_init, 'Initializing resources... (1/7)')
	sv_resources = server_info(launch_params)

	# logging
	os.environ['jag_logging_port'] = 'False'
	if sv_resources.cfg['logging']['enabled']:
		print(_main_init, 'Winding up logging (1.1/7)...')

		# reserve a port for the logger
		logging_socket = socket.socket()
		logging_socket.bind(('127.0.0.1', 0))
		sv_resources.cfg['logging']['port'] = logging_socket.getsockname()[1]
		os.environ['jag_logging_port'] = str(sv_resources.cfg['logging']['port'])
		
		# create and launch the logger process
		logger_ctrl = multiprocessing.Process(target=logger_process, args=(sv_resources, logging_socket))
		logger_ctrl.start()

	print(_main_init, 'Creating and starting the server process... (2/7)')
	# Create a new process containing the main incoming connections listener
	server_ctrl = multiprocessing.Process(target=sock_server, args=(sv_resources,))
	print(_main_init, 'Created the process instructions, launching... (3/7)')
	# Initialize the created process
	# (It's not requred to create a new variable, it could be done in 1 line with .start() in the end)
	server_ctrl.start()

	print(_main_init, 'Launched the server process... (4/7)')









