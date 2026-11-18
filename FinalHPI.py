# ==========================================
# INPUT DATA (Matrix with 3-grade tuples per cell)
# ==========================================
students = ["Ana", "Luis", "Carlos", "Elena"]  # Rows
subjects = ["Math", "Physics", "Programming"]  # Columns

# Each cell is a tuple containing 3 grades (e.g., (grade1, grade2, grade3))
# If the student is not enrolled, it is represented as: (-1, -1, -1)
grades_matrix = [
    [(9.0, 9.0, 9.0), (8.0, 8.0, 8.0), (8.5, 8.5, 8.5)],
    [(9.5, 9.5, 9.5), (9.0, 9.0, 9.0), (-1, -1, -1)],
    [(6.0, 6.0, 6.0), (7.0, 7.0, 7.0), (6.0, 6.5, 6.2)],
    [(8.0, 8.0, 8.0), (-1, -1, -1), (9.0, 9.0, 9.0)],
]

academic_data = (students, subjects, grades_matrix)
target_subject = "Programming"


# ==========================================
# 5-STEP PIPELINE FUNCTIONS
# ==========================================

# Member 1 (Adrián): Find the column index of the target subject
def find_subject_column(subjects: list, target_subject: str) -> int:
    """
    The function reads the subject that we want to search and it searches its index in a list of subjects
    Args:
        subjects(list): a list of strings with all the subjects in that degree
        target_subject(str): a string with the name of the subject you want to find
    Returns:
        col_index(int): position of the subject
    """
    col_index = 0  # Variable to search for the index
    for idx in range(len(subjects)):
        if subjects[idx] == target_subject:
            col_index = idx  # Replace the value that had at first with the index of the selected subject
            return col_index
    return -1  #  When we do not find the subject


# Member 2 (Javier): Get row indices of students enrolled in that subject (sum of tuple > 0) 
def get_enrolled_student_indexes(grades_matrix: list[list], col_index: int) -> list:
    """
    Receives a matrix of tuples of scores and the index of a column which corresponds to a
    subject and returns a list with the indexes of the students who are enrolled in that subject.
    Args:
        grades_matrix (list[list]): Matrix containing tuples of scores for each student and subject                
        col_index (int): Index of the column corresponding to the target 
    Returns:
        list: A list with the indexes of the students who are enrolled in that subject    
    """
    enrolled_indexes = []
    # The function goes over every row (student) of the matrix
    for idx in range(len(grades_matrix)):
        subject_tuple = grades_matrix[idx][col_index]
    # If the student is enrolled in the subject, it adds its index
        if subject_tuple != (-1, -1, -1):
            enrolled_indexes.append(idx)
    return enrolled_indexes

# Member 3 (Laura): Calculate the average of the 3 notes
def calculate_subject_average(subject_tuple: tuple[float]) -> float:
    """
    Calculate the average grade for a subject.
    Args:
        subject_tuple(tuple(float)): contains three different grades of one specific subject. (ex: (5.0, 8.5, 9.0))
    Returns:
        float: Returns the average grade for the subject.
    """
    total = 0.0
    count = 0
    # Iterates through the entire tuple by index, checking if each value is greater than 0.0; if so, adds its value. 
    for idx in range(len(subject_tuple)):
        if subject_tuple[idx] > 0.0:
            total += subject_tuple[idx]
            count += 1
    # If there are no grades greater than 0.0, it directly returns 0. 
    if count == 0:
        return 0.0
    return total / count


# Member 4 (Manuel): Build the Honor Roll list (subject average >= 8.0) from enrolled students
def build_honor_roll(students: list, grades_matrix: list[list], col_index: int, enrolled_indexes: list[int]):
    """
    Builds a list of enrolled students whose subject average is 8.0 or higher.

    Args:
        students (list): List of all students.
        grades_matrix (list[list]): Matrix containing each student's subject grades.
        col_index (int): Index of the subject to evaluate.
        enrolled_indexes (list[int]): Indexes of students enrolled in the subject.

    Returns:
        list: List of students who have an average grade of at least 8.0.
    """
    # Creates empty list which will include the honor roll students
    honor_list = []
    # Check each student enrolled in the subject
    for idx in range(len(enrolled_indexes)):
        student_idx = enrolled_indexes[idx]
        # Get the student's grades for the selected subject
        subject_tuple = grades_matrix[student_idx][col_index]
        # Calculate the student's average grade
        avg = calculate_subject_average(subject_tuple)
        if avg >= 8.0:
            # Add the student to the empty list
            honor_list.append(students[student_idx])
             # Return the final list
    return honor_list


# Member 5 (Daniel): Print the final report without f-strings
def print_honor_roll(target_subject: str, honor_list: list):
    print("--- HONOR ROLL REPORT ---")
    #Print the selected subject
    print("Target subject:", target_subject)
    # Print the students name in the list with a grade of 8 or more
    print("Qualifying Honor Roll students (Avg >= 8.0 in subject):", honor_list)

# ==========================================
# MAIN EXECUTION (Running the 5-step pipeline)
# ==========================================

def main_function(academic_data, target_subject):
    students_list, subjects_list, matrix = academic_data
    col = find_subject_column(subjects_list, target_subject)
    if col != -1:
        enrolled = get_enrolled_student_indexes(matrix, col)
        final_honor_roll = build_honor_roll(students_list, matrix, col, enrolled)
        print_honor_roll(target_subject, final_honor_roll)
    else:
        print("Subject not found:", target_subject)

# Execute the main programm
main_function(academic_data, target_subject)
