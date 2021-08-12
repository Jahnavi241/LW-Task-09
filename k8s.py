#!/usr/bin/python3
import cgi
import subprocess
import time

from datetime import datetime
print("Content-type: text/html")
print()

f = cgi. FieldStorage ( )
cmd = f.getvalue ("x")

print(" <h2>Your Command is :-</h2>", cmd,"<h2> \n Output is :-</h2>")
print("<h3>Today's date and Time is {:%Y-%m-%d %H:%M}</h3>". format (datetime.now()))

output = subprocess.getoutput("kubctl" + cmd + " -- kubeconfig admin.conf")
print("*"*100)
print()
print (output)
pri
print("*"*100)
time. sleep (0)
print('<hi style="background-color: green"> thank you for using this Kubernetes UI Page</h1>')