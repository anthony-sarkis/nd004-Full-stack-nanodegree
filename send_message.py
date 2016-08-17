from twilio.rest import TwilioRestClient

account_sid = "ACbda06cd22d1458cede5c2ad4d7b55670" # Your Account SID from www.twilio.com/console
auth_token  = "28775eb64fc34b723fe68043ec5b7906"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+13067374298",    # Replace with your phone number
    from_="+13069939675") # Replace with your Twilio number

print(message.sid)
