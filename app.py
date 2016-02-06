from twilio.rest import TwilioRestClient
from datetime import datetime
from datetime import date
from threading import Timer

#Twilio Creds
ACCOUNT_SID = "NA"
AUTH_TOKEN = "NA"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

x=datetime.today()
y=x.replace(day=x.day+1, hour=0, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1


def send():
            numbers = [] #Array Of Numbers
            d0 = date.today()
            d1 = date(2015, 12, 23) #End Date
            delta = d1 - d0
            print delta.days
            for element in numbers:
                client.messages.create(
                to=element,
                from_="NA", #Twilio #
                body=str(delta.days) + " Days Until Party Time",
                )


            print "text sent"
            t = Timer(secs, send)
            t.start()



t = Timer(secs, send)
t.start()