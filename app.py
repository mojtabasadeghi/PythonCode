constant = 0.45359237

weight = float(input("your weight please: "))
kilo_or_lb_flag = input("in lb(L) or Kilo(K) ").upper()

if kilo_or_lb_flag == "L":
    print("your weight in Lb is:" + str(weight / constant))
else:
    print("your weight in kilo is: " + str(weight * constant))