# Abstraction
# It aims to reduce complexity by hiding unnecessary details.

# In the followign example, the user of the class cna send emails without any 
# knowledge of the internal implementation details invovlved in sending an email.
# All those details are abstracted away.
class EmailService:
 def _connect(self):
   print("Connecting to email server")
 
 def _authenticate(self):
   print("Authenticating")
 
 def send_email(self):
   self._connect()
   self._authenticate()
   print("Sending email...")
   self._disconnect()
 
 def _disconnect(self):
   print("Disconnecting from email server...")

email = EmailService()
# The user only needs to use the provided method for sending the email, instead
# of directly handling the methods to take care of the specific steps sending an
# email involves.
email.send_email()

# Without abstraction, the user has to write much more complex code
class EmailService:
 def connect(self):
   print("Connecting to email server")
 
 def authenticate(self):
   print("Authenticating")
 
 def send_email(self):
   print("Sending email...")
 
 def disconnect(self):
   print("Disconnecting from email server...")

# Now the email has to take care of each step invovled in sending an email,
# which makes it much more complicated
email = EmailService()
email.connect()
email.authenticate()
email.send_email()
email.disconnect()

