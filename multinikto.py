#argument should be a .txt file with a list of IPs or URLS seperated by a new line

import sys
import subprocess

file = sys.argv[1]

f = open(file,"r")

for x in f:
    subprocess.call(["nikto","-host",x])