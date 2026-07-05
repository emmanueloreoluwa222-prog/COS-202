print("=== PERSONAL POCKET CGPA CALCULATOR (PPC) ===\n")

def get_grade_point(grade):
if grade >= 70:
return 5.0
elif grade >= 60:
return 4.0
elif grade >= 50:
return 3.0
elif grade >= 45:
return 2.0
elif grade >= 40:
return 1.0
else:
return 0.0

def calculate_cgpa():
print("Enter number of courses:")
num_courses = int(input())

total_points = 0  
total_units = 0  
  
for i in range(num_courses):  
    print(f"\nCourse {i+1}:")  
    units = int(input("Enter credit units: "))  
    score = float(input("Enter score (0-100): "))  
      
    gp = get_grade_point(score)  
    total_points += gp * units  
    total_units += units  
  
if total_units > 0:  
    cgpa = total_points / total_units  
    print(f"\nYour CGPA is: {cgpa:.2f}")  
      
    # Classification  
    if cgpa >= 4.5:  
        print("First Class Honours 🎉")  
    elif cgpa >= 3.5:  
        print("Second Class Upper")  
    elif cgpa >= 2.5:  
        print("Second Class Lower")  
    elif cgpa >= 1.5:  
        print("Third Class")  
    else:  
        print("Pass")  
else:  
    print("No courses entered!")

Run the calculator

if name == "main":
while True:
calculate_cgpa()
again = input("\nCalculate again? (y/n): ").lower()
if again != 'y':
print("Goodbye!")
break