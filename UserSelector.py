#!/usr/bin/python

"""
Funcion: Select a random user from the user pool while attching him/her with a given comment.

Usage: 

Author: 

Update: 2016-07-12 20:28:32

"""

import sys
import os
sys.path.append('../conf/')
reload(sys)
sys.setdefaultencoding('utf8')
from config import *

import random
import time
from CommentServer import CommentServer

class UserSelector:
	"""
	Select a random user from the user pool while attaching his/her information with a given comment.
	"""

	def __init__(self, file_name):
		"""
		Get information of a random user 
		"""
		openfile = open(file_name, "r")		
		self.__user_pool = openfile.readlines()
		openfile.close()

                self.__comment_server = CommentServer(COMMENT_SERVER)

		return


	def random_pick_user(self, commentlist,docid):
		"""
		Randomly pick an user and collect his/her information(including username, userid and profile picture).
		"""

		for comment in commentlist:
			user = random.choice(self.__user_pool)
			user_info = user.split()
			user_name = user_info[0]
			user_id = user_info[1]
			user_picture = user_info[2]

			self.__comment_server.add_comment(user_name, user_id, user_picture, comment, docid)
			"""
			user_info: user's information(including username, userid and profile picture)
			"""
			time.sleep(0.1)

		return

		
if __name__ == "__main__":
	"""
	Data testing section (Will not run if using UserSelector as a class).
	"""

	user_selector = UserSelector("writefilefinal02.txt")
	test_commentlist = ["commnet1", "comment2", "comment3"]
	docid = "bd095ac1b7193d2fb662585597465f01"

	user_selector.random_pick_user(test_commentlist,docid)
