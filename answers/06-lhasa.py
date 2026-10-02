# sadservers.com/newserver/lhasa

summa = 0

with open("scores.txt", "r", encoding="utf-8") as file:
  lines = file.readlines()
  count = len(lines)

  for i in lines:
    i = i.rstrip()
    values = i.split()
    number = float(values[-1])

    summa += number

avg = summa / count
to_list = str(avg).split(".")

print(to_list[0] + "." + to_list[1][:2])
