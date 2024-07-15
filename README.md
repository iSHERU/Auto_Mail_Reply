# Auto_Mail_Reply
This is a Python Program that fetched my unread emails from Google Account and then uses the integrated LLM Model to generate a suitable response to send to the user.


Email Automation Bot

Main Working Mechanism:
	The working mechanism of this Project involves certain steps which we have combined to make it a single working idea.
Following are the steps that are in the program.

1.	Accessing G-Mail Application in Python Programming Language:
Firstly, we must access the unread Emails from G-Mail App in our Browser. For which we have a built-in Python Library namely imapLib.
ImapLib helps us access mails from a specific Folder of our choice without downloading it. In this case we are accessing unread mails from Inbox folder. We have used different commands from ImapLib Library such as mail_login, search, fetch, logout etc.
For this purpose, after importing all the needed libraries we need to access the Gmail App using our G-Mail address and its password. We will do it by using the imap.google.com server as host. This Host allows us to access our Gmail account without the actual Gmail App Interface.

2.	Getting Relevant Data from Mails:
After accessing unread mails from the Inbox Folder, we must extract the needed data from the Mail and store it for further use. The data that we must extract in this case is the email, name of the sender and the message body i.e. what the sender’s message is.
To extract the data, we would use simple string slicing and indexing techniques on the header file that contains all the data related to the email that we’ve just read.

3.	Sending Automatic Reply:
After extracting email sender information from the unread emails then we must send an automated reply. To do so we will use multiple libraries for composing and sending the message to the correct destination.

SMTP library is used for sending emails via the SMTP protocol.

Connecting to SMTP Server: 
SMTP sets up a host server with the credentials provided, it establishes a secure connection to the Gmail app without the interface using the TLS security protocol.

Composing Email Headers:
To compose the email headers i.e. Sender, From, Subject, attachments (if any), 
we will have to use two libraries MIME-Text and MIME-MultiPart. MIME-Text will start composing the mail and Multi-Part will be used for defining the headers such as To, From, Subject etc. We use the email.mime.multipart.MIMEMultipart and email.mime.text.MIMEText classes to construct the email with the appropriate subject and body.

4.	USING CHAT-BOT TO REPLY:
We have used a Chat-Bot that will function when the Program is executed. The function of the chat bot is to take the body of the email that we just read, along the sender’s name and generate an appropriate.
The chat-bot has been integrated into the code as an API of LLAMA3 Generative AI Model using fireworks. The Model is available to everyone by META (formerly Facebook) to use in their own Projects.
Here the Model is already fed with a system Prompt which specifies the functionality of it in this Program. It will generate convincing replies regarding students asking a Teacher for rechecking their papers for any mistakes that might could have been made checking the first time.
