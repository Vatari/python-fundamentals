team_A = []
team_B = []

for i in range(1, 12):
    team_A.append(f"A-{i}")
    team_B.append(f"B-{i}")

cards = input().split(" ")

if len(cards) <= 0:
    team_A = []
    team_B = []
    print("asdsad")


for card in cards:
    if card in team_A:
        team_A.remove(card)
    elif card in team_B:
        team_B.remove(card)
    if len(team_A) < 7 or len(team_B) < 7:
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")

if len(team_A) < 7 or len(team_B) < 7:
    print("Game was terminated")
