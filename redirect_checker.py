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

target = open('output.txt', 'w')

base_url = "uvahealth.com"
i = 0
a = []
with open(filename) as f:
    for line in f:
        line = line.replace("\n", "")
        #print line
        path = base_url+line
        #print path
        #print type(path)
        x = get_status_code(base_url, line)
        if x != 301 :
            a.append(x)
            i += 1
        print str(x) + ' ' + path
        target.write(str(x) + ' ' + path + '\n')

print str(i) + " non-301 redirects found."
print a
target.write(str(i) + " non-301 redirects found.")
target.close()