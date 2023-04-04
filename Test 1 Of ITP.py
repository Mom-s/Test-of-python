# Mihirs Test 1
def takeInput():
  Month = int(input("Enter the month in a numeric form.: "))
  Day = int(input("Enter the day in numeric form.: "))
  Year = int(input("Enter the two numerical digit(For example:98,20,21)"))
  return (Month, Day, Year)


def displayResult(Month, Day, Year):
  check = 1

  if Month > 1 or Month <= 12:

    print(Month, "/", end='')
  else:
    check = 0
    print("Error: Invalid Month Input")

  if Day > 1 and Day <= 31:

    print(Day, "/", end='')
  else:
    check = 0
    print("Error: Invalid Month Input")
  if Year > 1 or Year <= 100:

    print(Year)
  else:
    check = 0
    print(("Error: Invalid Month Input"))
  if check == 1:
    print(":Success: Congratulations! you entered the correct date.")


(Month, Day, Year) = takeInput()
displayResult(Month, Day, Year)
