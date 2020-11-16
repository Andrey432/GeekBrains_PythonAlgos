from collections import defaultdict, namedtuple

QUARTERS = 4


comps_info = defaultdict(list)
n = int(input("Введите кол-во предприятий: "))
mid_income = 0

for _ in range(n):
    company = input("Введите имя предприятия: ")
    for i in range(QUARTERS):
        value = int(input(f"Прибыль за квартал {i + 1}: "))
        comps_info[company].append(value)
        mid_income += value

mid_income /= n
print(f"Средняя прибыль компаний: {mid_income:.3f}")

comp_stats = namedtuple("CompsStats", "more_av less_av")([], [])
for company, income_inf in comps_info.items():
    if sum(income_inf) >= mid_income:
        comp_stats.more_av.append(company)
    else:
        comp_stats.less_av.append(company)

print(f"Компании, чья прибыль выше среднего:", *comp_stats.more_av,
      f"Компании, чья прибыль меньше среднего:", *comp_stats.less_av, sep='\n')
