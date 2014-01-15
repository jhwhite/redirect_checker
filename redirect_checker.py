import httplib
from sys import argv
# -*- coding: utf-8 -*-

script, filename, output = argv

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

target = open(output, 'w')

print "What is the domain you want to check?"
base_url = raw_input()
i = 0
non_301 = ""
with open(filename) as f:
    for line in f:
        line = line.replace("\n", "")
        #print line
        path = base_url+line
        #print path
        #print type(path)
        status_code = get_status_code(base_url, line)
        if status_code != 301 :
            non_301 = non_301 + str(status_code) + ' ' + path + '\n'
            i += 1
        #print str(status_code) + ' ' + path
        target.write(str(status_code) + ' ' + path + '\n')

#print str(i) + " non-301 redirects found."
target.write(str(i) + " non-301 redirects found.\n")
target.write(non_301)
target.close()