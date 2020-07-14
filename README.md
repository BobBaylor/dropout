# dropout - Is your ISP dropping out sometimes?
This script periodically opens a socket to a DNS server. When it fails, it prints a timestamp and a description of the failure.

## Why do this?
To keep a running list of service dropouts. 

## No, really. Why do this?
I'm switching providers. Mostly because my cable TV conusmption has dropped to zero and comcast really doesn't know how to price broadband without cable TV. 
They know how to make lots of money, though. Good for them. Now that I'm WFH, I notice that comcast seems to dropout for about a minute a couple of times in the middle of the day.
Now that I have two ISPs running into the house, I would like to compare their dropout performance before I switch to ATT fiber.

## Is this hard to setup?
Not if you already have python installed. It doesn't use any libraries beyond the standard lib. Install python from https://www.python.org/downloads/

Then clone this repo, open a terminal or DOS window and run it
```
python dropout.py
```

that's it. 

It will print a signon date & time. Then it will slowly spin until it detects a dropout. Dropouts will show a date, time, and details of the dropout.

## It doesn't work. I hate you!
dropout uses f-strings so it won't work with python older than 3.6, I think. Feel free to contact me. Don't be surprised if I don't respond. 
