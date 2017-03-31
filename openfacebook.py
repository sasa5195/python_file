import mechanize
import cookielib

def login(br, url):
	page = br.open(url)#Get the form used by normal user to logon
	#br.select_form(nr=0)
	print br.title()
	br.select_form(nr=0)
    #send login information
	br['email'] = "baidsahil@gmail.com"
	br['pass'] = "$@#IL5195"
	br.submit()
	
# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
#br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')] #Now browser instance is created

login(br, "https://www.facebook.com/login/")
print br.title()
for link in br.links():
    print link.text, link.url       
    br.open('https://www.facebook.com/baidsahil5195')
