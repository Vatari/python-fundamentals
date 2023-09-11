class Party:
    def __init__(self):
        self.people = []

    def get_info(self):
        return f"Going: {', '.join(self.people)}\nTotal: {len(self.people)}"


name = input()
party = Party()
while name != "End":
    party.people.append(name)
    name = input()
print(party.get_info())
