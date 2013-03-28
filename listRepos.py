#!/usr/bin/env python

import sys,urllib2,json

for user in sys.argv:
	
	if user != sys.argv[0]:
		
		try:
			
			## Fetch user repositories from GitHub
			apiResults = urllib2.urlopen('https://api.github.com/users/' + user + '/repos')
			jsonData = apiResults.read()
			
			## Parse the json object
			data = json.loads(jsonData)
			
			for repo in data:
				
				## Print repo info
				print user + ";" + repo['name'] + ";" + repo["git_url"]
					
		except:
			
			continue