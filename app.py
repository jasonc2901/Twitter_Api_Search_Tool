from tkinter import *
from twitter_api import get_tweets
import tkinter.scrolledtext as scrolledtext

def getTweets():
    global user
    global startDate
    global endDate

    num_tweets_label.place(x=100,y=350)
    num_tweets_box.place(x=250,y=350)
    tweets_box.place(x=90, y=400)
    newSearchBtn.place(x=230, y=550)

    #prevent user from pressing search button
    runSearchBtn.config(state="disabled")
    
    user = usernameBox.get()
    start = startDateBox.get()
    end = endDateBox.get()

    tweets = get_tweets(user,start,end)
    
    num_tweets_box.insert(0,len(tweets))

    for tweet in tweets:
        char_list = [tweet[j] for j in range(len(tweet)) if ord(tweet[j]) in range(65536)]
        tweet=''
        for j in char_list:
            tweet=tweet+j
        tweets_box.insert(END, "-----------------------------------------\n" + tweet + "\n-----------------------------------------\n\n")


def start_over():
    #clears the previous results preventing duplicated numbers
    num_tweets_box.delete(0, 'end')
    tweets_box.delete(1.0, END)

    #allows user to press search button again
    runSearchBtn.config(state="normal")

    num_tweets_label.place_forget()
    num_tweets_box.place_forget()
    tweets_box.place_forget()
    newSearchBtn.place_forget()

    #clears the values from original search 
    usernameBox.delete(0,'end')
    startDateBox.delete(0,'end')
    endDateBox.delete(0,'end')

root = Tk()
root.title("Twitter Date Checker - GUI")
root.resizable(False, False)
root.configure(background='#262626')

title = Label(root, text="Twitter Date Checker - GUI", bg="#262626", fg="white", font="none 32 bold")
title.pack()

c = Canvas(root,bg="#262626", height=700, width=700, bd=0, highlightthickness=0, relief='ridge')
c.pack()

frame = Frame(root, bg="grey")
frame.place(relwidth=0.8,relheight=0.8, relx=0.1, rely=0.1)

Label(frame, text = "Enter Username:", bg="grey", fg="white").place(x=100,y=100)
Label(frame, text = "Enter Start Date:", bg="grey", fg="white").place(x=100,y=150)
Label(frame, text = "Enter End Date:", bg="grey", fg="white").place(x=100,y=200)

usernameBox = Entry(frame,bd=0, highlightthickness=0, relief='ridge')
usernameBox.place(x=250,y=100)
startDateBox = Entry(frame,bd=0, highlightthickness=0, relief='ridge')
startDateBox.place(x=250,y=150)
endDateBox = Entry(frame,bd=0, highlightthickness=0, relief='ridge')
endDateBox.place(x=250,y=200)

#create the button for running the twitter api search
runSearchBtn = Button(frame, padx=10, pady=10, highlightbackground="#262626", fg="white", text="Search Tweets!", command=getTweets)
runSearchBtn.place(x=215, y=250)

#create the output boxes for displaying the tweet data
num_tweets_label = Label(frame, text = "Number of tweets:", bg="grey", fg="white")
num_tweets_box = Entry(frame,bd=0, highlightthickness=0, relief='ridge')
num_tweets_box.config(state=NORMAL)

tweets_box = scrolledtext.ScrolledText(frame, width=50, height=10, bg="#262626", fg="white",bd=0, highlightthickness=0, relief='ridge')
tweets_box.config(state=NORMAL)
#create the button for running a new tweet
newSearchBtn = Button(frame, padx=10, pady=10, highlightbackground="#262626", fg="white", text="Start Over!", command=start_over)

root.mainloop()