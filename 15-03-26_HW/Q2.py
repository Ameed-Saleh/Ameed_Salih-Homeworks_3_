'''
Exercise 2 – Average grade
grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}

-> 82.5
Write a function that calculates the average grade of all students
'''

import statistics
def get_average_grade(grades: dict) -> float:
    '''
    :param grades: {<name>: <grade>}
    :return: average grade of all students
    '''
    _average = statistics.mean(grades.values())
    print(f"The average grade of all students is -> {_average}")
    return _average


grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}
get_average_grade(grades)