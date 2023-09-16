data = {}  # {player: {position: skill}}

while True:
    command = input()
    if command == 'Season end':
        break

    if ' -> ' in command:
        player, position, skill = command.split(' -> ')

        if player not in data:
            data[player] = {position: int(skill)}

        elif position not in data[player].keys():
            data[player][position] = int(skill)

        else:
            data[player][position] = max(data[player][position], int(skill))

    elif ' vs ' in command:
        p1, p2 = command.split(' vs ')

        if p1 in data.keys() and p2 in data.keys():
            for p1_position in data[p1].keys():
                if p1_position in data[p2].keys():
                    p1_skill = sum(data[p1].values())
                    p2_skill = sum(data[p2].values())
                    if p1_skill < p2_skill:
                        data.pop(p1)
                    elif p2_skill < p1_skill:
                        data.pop(p2)
                    break

player_points = [(p, sum(data[p].values())) for p in data.keys()]
player_ranking = [rank for rank in sorted(player_points, key=lambda item: (-item[1], item[0]))]

for rank in player_ranking:
    player, skill = rank
    print(f"{player}: {skill} skill")
    position_ranking = [rank for rank in sorted(data[player].items(), key=lambda item: (-item[1], item[0]))]
    output = [f'- {pos} <::> {skill}' for pos, skill in position_ranking]
    print(*output, sep='\n')
