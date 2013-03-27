#!/usr/bin/env python
import sys
import urllib2
import json

DEBUG=False

def do_debug(debugString):
    if DEBUG:
        print (debugString)
        
def fetch_repo_list(user):
    """
    Fetch user repositories from GitHub.
    """

    try:
        endpoint = "https://api.github.com/users/%s/repos" % user
        apiResults = urllib2.urlopen(endpoint)
        jsonData = apiResults.read()
        parse_json(jsonData)
    except Exception as e:
        do_debug("Error in Repo Fetch: %s" % e)
	
def parse_json(jsonData):	
    """
    Parse and print the incomming json.
    """
   
    try:
        data = json.loads(jsonData)
        for repo in data:
            print ( "%s;%s;%s" % (repo['owner']['login'], repo['name'], repo["git_url"]))
    except Exception as e:
        do_debug("Error in Json Parse: %s" % e)

def main():
    for user in sys.argv[1:]:
        fetch_repo_list(user)

if __name__ == "__main__":
	main()

				
