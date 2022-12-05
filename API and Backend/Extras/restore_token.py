from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = 'AC73af0c2300b28f7cf1a1527b3137c7a0'
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Your appointment is coming up on July 21 at 3PM',
    to='whatsapp:+918826724387'
)

print(message.error_message)