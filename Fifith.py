name = input("Enter your name: ")
grade1 = float(input("Enter your grade for the first exam: "))
grade2 = float(input("Enter your grade for the second exam: "))
average = (grade1 + grade2) / 2
print(f"Hello student {name}, your average is {average:.2f}")
if average >= 6:
    print("You have passed!!")
else:
    print("You have failed!!")

exit()
