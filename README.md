# RSEMC - Rahul's Simple Email Client

The idea comes from the fact there is no Gmail client for MacOs. Personally, I hate using outlook for personal email because
it is very heavy for a minimal laptop. So, I decided to make my own using Python. 
I am gonna start with a simple interface using Python and using SMTP to connect to my account(s) in the backend. 

## Components 
1. Front End interactive UI with the following:
    1. Send button
    2. Recipnt placeholder
    3. cc placeholder
    4. bcc placeholder
    5. Body to write text
    6. Attachment button
    7. Switch between accounts

2. Back End with the following components:
    1. Connects to account
    2. Sends email
    3. Option for multiple accounts
