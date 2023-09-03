happiness = [int(coefficient) for coefficient in input().split()]
factor_happiness = int(input())

average_empl_happiness = sum([single_happiness * factor_happiness
                              for single_happiness in happiness]) / len(happiness)

happy_list = [single_happiness * factor_happiness
              for single_happiness in happiness
              if single_happiness * factor_happiness >= average_empl_happiness]

if len(happy_list) >= len(happiness) / 2:
    print(f"Score: {len(happy_list)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_list)}/{len(happiness)}. Employees are not happy!")
