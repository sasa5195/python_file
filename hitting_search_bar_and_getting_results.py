####import requests
####
####url = "http://duckduckgo.com/html"
####payload = {'q':'python'}
####r = requests.post(url, payload)
####print r.content
####with open("requests_results.html", "w") as f:
####    f.write(r.content)
####f=open("requests_results.html", "r")
####print f.read()
####f.close()
##import urllib
##import urllib2
##import webbrowser
##
##url = "http://duckduckgo.com/html"
##data = urllib.urlencode({'q': 'Python'})
##results = urllib2.urlopen(url, data)
####with open("results.html", "w") as f:
####    f.write(results.read())
####
####webbrowser.open("results.html")
##print results.read()
#import mechanize #sudo pip install python-mechanize
username=raw_input("Username: ")
email=raw_input("Email: ")
password=raw_input("Password: ")
##name=raw_input("Name: ")
##phn=raw_input("Phone: ")
##c_name=raw_input("Co_name: ")
##desc=raw_input("Desc: ")
##userfile=raw_input("Image loc: ")
##
##br = mechanize.Browser() #initiating a browser
##
##br.set_handle_robots(False) #ignore robots.txt
##
##br.addheaders = [("User-agent","Mozilla/5.0")] #our identity
##
##gitbot = br.open("http://startupsuccess.pe.hu/ci/index.php/verifylogin/signup") #requesting the github base url
##
##br.select_form(nr=0) #the sign up form in github is in third position(search and sign in formscome before signup)
##
##br["name"] = name #username for github
##br["phn"] = phn
##br["email"] = email #email for github
##br["c_name"] = c_name
##br["description"] = desc #password for github
##br["username"] = username
##br["password"] = password
##
##sign_up = br.submit()

import mechanize #sudo pip install python-mechanize

br = mechanize.Browser() #initiating a browser

br.set_handle_robots(False) #ignore robots.txt

br.addheaders = [("User-agent","Mozilla/5.0")] #our identity

gitbot = br.open("https://github.com") #requesting the github base url

br.select_form(nr=1) #the sign up form in github is in third position(search and sign in formscome before signup)

br["user[login]"] = username #username for github

br["user[email]"] = email #email for github

br["user[password]"] = password #password for github

sign_up = br.submit()
