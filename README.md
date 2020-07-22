# Twitter_Api_Search_Tool
This is a tool I created using a combination of Pythons Tweepy module to access the Twitter API and also the tkinter module in order to create and design a simple GUI for this program. 

The main goal with this project was to simply be able to enter a username along with a start/end date and the tool would search that account between those dates and return the tweets.

Feel free to try this tool and make any adjustments/improvements to it where you see fit.

# Install the tool requirements

- Create a Virtual Environment by running following command:
     - virtualenv env

- Enter the virtual environment using following command:
     - source env/bin/activate
     
- batch install requirements
     - pip3 install -r requirements.txt
     

# IMPORTANT: 
Add TWITTER_API_KEY + TWITTER_API_KEY_SECRET as well as TWITTER_ACCESS_TOKEN AND TWITTER_ACCESS_TOKEN_SECRET into your own '.bash_profile' file.

- run command 'code .bash_profile' to open the file in vscode
- add 'export TWITTER_API_KEY='ENTER API KEY HERE' 
- repeat the above step for each of the four required keys
- save the file and run 'source .bash_profile' in your terminal to refresh the file 


# Run the program
- python app.py