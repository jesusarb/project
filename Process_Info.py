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
    return sum(scores) / len(scores) if scores else 0


def assign_grade(score: int) -> str:
    """
    Assign a grade based on the score.
    
    Args:
    score (int): The score to evaluate.

    Returns:
    str: The assigned grade ('A' to 'F').
    """
    if score >= 85:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 65:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def get_country_abbreviation(country: str) -> str:
    """
    Get the abbreviation for a given country name.
    
    Args:
    country (str): The name of the country.

    Returns:
    str: The country abbreviation, or 'N/A' if not found.
    """
    country_abbreviations = {
        'United States': 'USA',
        'United Kingdom': 'UK',
        'Dominican Republic': 'DO',
        'Canada': 'CA',
        'Australia': 'AU',
        'India': 'IN',
        'Germany': 'DE',
        'France': 'FR',
        'Mexico': 'MX',
        'Brazil': 'BR',
        'Japan': 'JP'
    }
    return country_abbreviations.get(country, 'N/A')
#-----End Functions---------------

import csv

# Initialize the list to store processed student data
students = []

# Reading the CSV file and processing data
try:
    with open('Students.csv', 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Read the header (first row)
        header = next(reader)

        # Process each row in the CSV file
        for row in reader:
            # Ensure the row has the expected number of columns
            if len(row) == 6:
                name, surnames, country, math, science, english = row
                try:
                    # Convert scores to integers
                    math_score = int(math)
                    science_score = int(science)
                    english_score = int(english)

                    # Assign grades
                    math_grade = assign_grade(math_score)
                    science_grade = assign_grade(science_score)
                    english_grade = assign_grade(english_score)

                    # Get country abbreviation
                    country_abbreviation = get_country_abbreviation(country)

                    # Append the processed data to the students list
                    students.append([
                        name, surnames, country, country_abbreviation,
                        math_score, math_grade,
                        science_score, science_grade,
                        english_score, english_grade
                    ])
                except ValueError:
                    print(f"Skipping row due to invalid score data: {row}")
            else:
                print(f"Skipping row due to incorrect number of columns: {row}")

    # Write results to a new CSV file
    with open('Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header including 'Country Abbreviation'
        writer.writerow([
            'Name', 'Surnames', 'Country', 'Country Abbreviation',
            'Math Score', 'Math Grade',
            'Science Score', 'Science Grade',
            'English Score', 'English Grade'
        ])
        # Write the rows
        writer.writerows(students)

    print('Results saved to Results.csv')

except FileNotFoundError:
    print("Error: 'Students.csv' file not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")