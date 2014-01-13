import httplib
from sys import argv
# -*- coding: utf-8 -*-

script, filename = argv

#This function comes from http://stackoverflow.com/questions/1140661/python-get-http-response-code-from-a-url
#author is Evan Fosmark
def get_status_code(host, path="/"):
    """ This function retreives the status code of a website by requesting
        HEAD data from the host. This means that it only requests the headers.
        If the host cannot be reached or something else goes wrong, it returns
        None instead.
    """
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None


initial_path = #"INSERT ROOT URL HERE"

#print get_status_code("uvahealth.com", "/Allergy")

with open(filename) as f:
	for line in f:
		line = line.replace("\n", "")
		#print line
		#path = initial_path+line
		#print path
		#print type(path)
		print get_status_code(initial_path, line)

