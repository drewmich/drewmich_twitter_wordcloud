# twitter_wordcloud
Command line python module that visualizes related terms on Twitter using a wordcloud.

I wrote this to explore what other words are on average often associated with hashtags, trends, or words on Twitter. 

This script relies on a file called twitter_cred.py that contains four variables which 
store the user twitter API keys and tokens in order to access the API. Users should place a file in the same 
directory called twitter_cred.py in the format:

    API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxx"
    API_SECRET = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ACCESS_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ACCESS_SECRET = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

These variables are abstracted away in order to keep these values private.

The user should download the .py file and naviagate in their terminal to the same directory the file is saved in.

When running the script, the first argument is the file name: "./twitter_proj.py"

The second argument is either "save" or "show". 
    save: saves the wordcloud to the current working directory
    show: saves the wordcloud to the current working directory, and displays the image
    
The third argument is the term to be searched. It is important NOT to start your term with a hashtag (\#). 
This breaks the program.

For example, a user could run: `./twitter_proj.py show baseball`,
This produces the following output:
![image](https://user-images.githubusercontent.com/47374581/91736395-9619cf00-eb7b-11ea-8bc8-55c3f7258fe8.png)


