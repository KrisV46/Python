class Email:
    def __init__(self, sender,receiver,content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False
    def send(self):
        self.is_sent = True
    
    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'
emails = []
line = (input("Input: "))  # Peter John Hello
while line != 'Stop':
    tokens = line.split(" ")  #We split the user input with space, so we can access each element(argument) 
    sender = tokens[0]   # dostupva purvata stoinost(Peter) 
    receiver = tokens[1]   # dostupva vtorata stoinost(John)
    content = tokens[2]    # dostupva tretata stoinost(Hello)
    #We create an object of the Email class and apply all user inputs as arguments 
    email = Email(sender, receiver, content)
    #print(email.get_info())
    emails.append(email)  #append obekta email kum lista
    line = (input("Input: "))
print(" ")

send_emails = list(map(lambda x: int(x), input("Index of sent emails: ").split(", ")))
for x in send_emails:
    emails[x].send()
    print(send_emails)

for email in emails:
    print(email.get_info())
