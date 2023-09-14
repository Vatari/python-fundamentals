result = {}
entry = input().split(' -> ')

while entry[0] != "End":
    company, empl_id = entry
    if company not in result:
        result[company] = []
    if empl_id not in result[company]:
        result[company].append(empl_id)

    entry = input().split(' -> ')
for company, employees in result.items():
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")
