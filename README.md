# drewmich_twitter
Command line python module that visualizes related terms on twitter using a wordcloud.

This script relies on a file called twitter_cred.py that contains four variables which 
store the user twitter API keys and tokens in order to access the API. Users should place a file in the same 
directory called twitter_cred.py in the format:
    API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxx"
    API_SECRET = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ACCESS_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ACCESS_SECRET = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
These variables are abstracted away in order to keep these values private.

When running the script, the first argument is either "save" or "show". 
    save: saves the wordcloud to the current working directory
    show: saves the wordcloud to the current working directory, and displays the image
    
The second argument is the term to be searched. It is important NOT to start your term with a hashtag (\#). 
This breaks the program.




