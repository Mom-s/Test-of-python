# Part 3 of ITP

salary = float(input("Please enter your salary in Germany:"))
country = input("Enter the country you want to migrate to:")


def convertSalary(salary, ):

  if (country == "canada"):
    final_salary = salary * 1.55
    if (final_salary > 64000):
      print("You will be rich in canada with a salery of", final_salary, "CAD")
    else:
      print("You will be poor in canada with a salery of", final_salary, "CAD")

  elif (country == "united states"):
    final_salary = salary * 2.5
    if (final_salary > 56516):
      print("You will be rich in united states with a salery of", final_salary,
            "USD")
    else:
      print("You will be poor in united states with a salery of", final_salary,
            "USD")

  elif (country == "cambodiya,CAMBODIYA"):
    final_salary = salary * 4555
    if (final_salary > 5, 649, 856):
      print("You will be rich in cambodiya with a salery of", final_salary,
            "Cambodian Riel")
    else:
      print("You will be poor in cambodiya with a salery of", final_salary,
            "Cambodian Riel")

  elif (country == "United kingdom,UNITED KINGDOME"):
    final_salary = salary * 1.2
    if (final_salary > 35423):
      print("You will be rich in united kingdom with a salery of",
            final_salary, "POUND")
    else:
      print("You will be poor in united kingdom with a salery of",
            final_salary, "POUND")
  else:
    print("Invalid country")


convertSalary(salary)