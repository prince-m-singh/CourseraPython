try:
    score=float(raw_input("Enter Score:"))
    if score>=0.9 and score<1.0:
                print("A")
    elif score>=0.8 and score< 0.9:
                      print("B")
    elif score>=0.7 and score< 0.8:
                      print("C")
    elif score>=0.6 and score< 0.7:
                      print("D")
    elif score<0.6 and score< 0.5:
                        print("F")
    else:
        print("Bad Score")
except:
                      print("BAD Score")
