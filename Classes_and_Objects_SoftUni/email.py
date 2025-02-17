class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


accounts = []
while True:
    command = input()
    if command == "Stop":
        break
    my_command = command.split()
    sender = my_command[0]
    receiver = my_command[1]
    content = my_command[2]
    email = Email(sender, receiver, content)
    accounts.append(email)

sent_indexes = list(map(int, input().split(", ")))

for index in sent_indexes:
    accounts[index].send()

for acc in accounts:
    print(acc.get_info())
