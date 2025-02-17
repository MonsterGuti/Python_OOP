class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    command = input()
    if command == "End":
        break
    party.people.append(command)

party_to_string = ", ".join(party.people)
print(f"Going: {party_to_string}")
print(f"Total: {len(party.people)}")
