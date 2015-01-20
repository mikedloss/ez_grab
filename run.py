import urllib
import urllib2
import lxml.html
import os
import pdb
from bs4 import BeautifulSoup

def go(dom, main_url, type):
	website_name = main_url.split('/')[2].split('.')[1]
	basic_url = main_url.split('/')[2]
	upperfolder = main_url.split('/')[-1]
	
	# get list of links for given type
	link_list = []
	transcription_list = []
	print "Starting search for files"
	for link in dom.xpath('//a/@href'):
		if link.find("." + type) != -1:
			link_list.append(link)
		if link.find("defenders-2-podcast/transcript") != -1:
			transcription_list.append(link)
	print " >> Found " + str(len(link_list)) + " links with file type " + type
	
	# create / move to directories in current folder
	if not os.path.exists(website_name):
		os.makedirs(website_name)
		os.chdir(website_name)
	else:
		os.chdir(website_name)
		
	if not os.path.exists(upperfolder):
		os.makedirs(upperfolder)
		os.chdir(upperfolder)
	else:
		os.chdir(upperfolder)
		
	if not os.path.exists(type):
		os.makedirs(type)
		os.chdir(type)
	else:
		os.chdir(type)
	
	# download
	if len(link_list) != 0:
		for each in link_list:
			file_name = each.split('/')[-1]
			if each[0] == "/":
				each = "http://" + basic_url + each
			
			if os.path.isfile(file_name):
				size = long(urllib.urlopen(each).info().getheaders("Content-Length")[0])
				if not size == os.path.getsize(file_name):
					# unfinished file, delete and start over
					print " - " + file_name + " is incomplete, starting over..."
					os.remove(file_name)
					print " + Downloading " + file_name
					urllib.urlretrieve(each, file_name)
				else:
					# already exists, matches size, moving on
					print " - " + file_name + " already exists, skipping..."
			else:
				print " + Downloading " + file_name
				urllib.urlretrieve(each, file_name)
	os.chdir(os.pardir)
	os.chdir(os.pardir)
	os.chdir(os.pardir)
	print " !! Finished downloading all " + type + " files"
	
# gets a list of urls to download from
with open('urls.txt') as f:
	urls = [x.strip('\n') for x in f.readlines()]
	
# gets the list of filetypes the user wants to download
with open('filetypes.txt') as f:
	filetype_list = [x.strip('\n') for x in f.readlines()]

for url in urls:
	print "          ------------------------------------------------------------"
	print "                               Working with:"
	print "{0}".format(url)
	print "          ------------------------------------------------------------"
	connection = urllib.urlopen(url)
	dom = lxml.html.fromstring(connection.read())
	go(dom, url, "mp3")
	go(dom, url, "doc")
	go(dom, url, "pdf")
	print "!!! Finished working with " + url
