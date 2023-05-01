# the actual sms code in python

from twilio.rest import Client
from dotenv import load_dotenv
import os
import random

load_dotenv()

# phone_no=os.getenv("PHONE_NUMBER")
OTP=random.randint(1000,9999)
client=Client()
account_sid=os.getenv("TWILIO_ACCOUNT_SID")
auth_token=os.getenv("TWILIO_AUTH_TOKEN")
client=Client(account_sid,auth_token)

message=client.messages.create(
    body="Your OTP is"+str(OTP), from_="+19783961781",to="+916379126509"
    )
print(message.body)