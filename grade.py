score = int(input("Score: "))

if 90<= score <= 100:
    print ("Grade: A")
elif score >= 80 and score < 90:
    print ("Grade: B") 
elif 70 <= score < 80:
    print ("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
