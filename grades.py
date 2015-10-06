while True:
  try:
    score = float(input("Enter your numerical score: "))
    if score > 1.00:
      print("Bad score; Please enter a score 0.00 and 1.00 only")
    elif score >= 0.9:
      print("A")
    elif score >= 0.8:
      print("B")
    elif score >= 0.7:
      print("C")
    elif score >= 0.6:
      print("D")
    elif score < 0.6:
      print("F")
    elif score <= 0:
      print("Bad score; Please enter a score between 0.00 and 1.00 only")
  except ValueError:
    print("Bad score; Please enter a numerical value between 0.00 and 1.00 only")
