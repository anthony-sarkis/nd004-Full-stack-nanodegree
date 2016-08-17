
"""
Goals 
1. Define profane words and data access
2. Compare words in the document against profanity database
3. Display results to user
"""

import urllib.request

def read_text():
    #Create object
    data = open(r"C:\Users\Anthony\Documents\GitHub\nd004\movie_quotes.txt")
    contents = data.read()
    print(contents)
    data.close()
    check_profanity(contents)

def check_profanity(text):
    url = "http://www.wdylike.appspot.com/?q="
    q = {'q':text}
    t = url+urllib.parse.urlencode(q)
    connection = urllib.request.urlopen(t)
    output = connection.read()

    """
    if "true" in output:
        print("true apples")
    elif "false" in output:
        print("false apples")
    """
    
    print(output)
    connection.close()

read_text()
    
