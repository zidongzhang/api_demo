#!/usr/bin/env python

import sys
import os
import time
import urllib
import urllib2
import json

class CommentServer():

	def __init__(self, host):

		self.__host = host

		return

	def add_comment(self, username, userid, userpic, usercomment, docid):
		url = "https://%s/v1/comment/action" % (self.__host)

		headers = {}
		headers["Content-Type"] = "application/json; charset=utf-8"
		headers["Authorization"] = "anonym=%s" % (userid)

		storge = {}
		storge["type"] = "inneradd"
		storge["refId"] = "d-%s" % (docid)
		storge["name"] = username
		storge["photo"] = userpic
		storge["content"] = usercomment

		data = json.dumps(storge)

		req = urllib2.Request(url, headers = headers, data = data)

		try:
			response = urllib2.urlopen(req)
			result = response.read()

		except Exception, ex:
			result = False
			print json
			print ex

                return result


if __name__ == "__main__":
	comment_server = CommentServer("")
	test_data_username = "Adam"
	test_data_userid = "fd8f9136-777d-3a0c-bd73-d6f9ea0655b1"
	test_data_userpic = "http://profile.egloos.net/f0303947_50.jpg"
	test_data_usercomment ="That was awesome"
	test_data_docid = "bd095ac1b7193d2fb662585597465f01"

	comment_server.add_comment(test_data_username, test_data_userid, test_data_userpic, test_data_usercomment, test_data_docid)
