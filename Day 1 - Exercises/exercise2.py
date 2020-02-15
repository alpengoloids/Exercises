grade=0
while True:
    grade = int(input("Enter a grade: "))
    if grade <= 100:
            if grade <= 100 and grade >= 90:
                print("Grade: A")
                break
            elif grade < 90 and grade >= 80:
                print("Grade: B")
                break
            elif grade < 80 and grade >= 70:
                print("Grade: C")
                break
            elif grade < 70 and grade >= 60:
                print("Grade: D")
                break
            else:
                print("Grade: E")
                break

