input_Value = input("Phone: ")

digit_map = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}
for number in input_Value:
    print(digit_map.get(number, " ! "), end=" ")
