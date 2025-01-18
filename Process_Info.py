#---------------------------------------------------
#------Created  : 09/01/2025 - Jesus Reynoso Bourdier
#------Modified : 04/02/2025
#------Description : Python program to process student data
#----------------------------------------------------

#-----Define Functions---------------
def calculate_average(scores: list) -> float:
    """
    Calculate the average of a list of scores.
    
    Args:
    scores (list): A list of integers representing scores.

    Returns:
    float: The average of the scores.
    """
    return sum(scores) / len(scores)


def assign_grade(average: int) -> str:
    """
    Assign a grade based on the average score.
    
    Args:
    average (int): The score to evaluate.

    Returns:
    str: The assigned grade ('A' to 'F').
    """
    if average >= 85:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 65:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'
#-----End Functions---------------


# Importing the csv module
import csv

# Initializing the students list
students = []

# Reading the CSV file and processing data
try:
    with open('Students.csv', 'r') as file:
        # Creating a CSV reader object
        reader = csv.reader(file)

        # Read the header (first row)
        header = next(reader)

        # Extracting field names through first row and processing each student
        for row in reader:
            # Assuming CSV structure: Name, Math, Science, English
            if len(row) == 4:
                name, math, science, english = row
                try:
                    # Convert scores to integers and assign grades
                    m_grade = assign_grade(int(math))
                    s_grade = assign_grade(int(science))
                    e_grade = assign_grade(int(english))

                    # Append the processed data to the students list
                    students.append([name, math, m_grade, science, s_grade, english, e_grade])
                except ValueError:
                    print(f"Skipping row due to invalid data: {row}")
                    continue  # Skip this row if data is invalid
            else:
                print(f"Skipping row due to incorrect number of columns: {row}")

    # Writing results to a new CSV file
    with open('Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Math', 'Math_Grade', 'Science', 'Science_Grade', 'English', 'English_Grade'])
        writer.writerows(students)

    print('Results saved to Results.csv')

except FileNotFoundError:
    print("Error: 'Students.csv' file not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")