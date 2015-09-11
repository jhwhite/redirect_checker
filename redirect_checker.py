import requests

from sys import argv
# -*- coding: utf-8 -*-

script, filename, output = argv

target = open(output, 'w')

print("What is the domain you want to check?")
base_url = input()
i = 0
non_301 = ""
with open(filename) as f:
    for line in f:
        line = line.replace("\n", "")
        path = base_url+line
        response = requests.head(path)
        status_code = response.status_code
        if status_code != 301 :
            non_301 = non_301 + str(status_code) + ' ' + path + '\n'
            i += 1

target.write(str(i) + " non-301 redirects found.\n")
target.write(non_301)
target.close()