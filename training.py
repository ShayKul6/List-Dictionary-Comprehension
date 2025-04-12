import random

# --- Double lists' values --- #
# new_list = [num*2 for num in range(1, 5)]
# print(new_list)

# --- Create list of less than 4 letters names --- #
# --- Create list of uppercase names with more than 4 letters names --- #
# names_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names_list if len(name) < 5]
# print(short_names)
# uppercase_names = [name.upper() for name in names_list if len(name) > 4]
# print(uppercase_names)

# --- Data Overlap --- #
# with open("file1.txt") as file1:
#     numbers_1 = [int(line.strip()) for line in file1]
# with open("file2.txt") as file2:
#     numbers_2 = [int(line.strip()) for line in file2]
# result = [num for num in numbers_1 if num in numbers_2]
# print(result)


# --- Create dictionary generating random scores for students --- #
# --- Create dictionary contains students with scores above 60 --- #
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
# passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

# --- Dictionary Comprehension 1 --- #
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}

# --- Dictionary Comprehension 2 --- #
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day: (temp_c*9/5)+32 for (day, temp_c) in weather_c.items()}

# --- Iteration over a Pandas DataFrame --- #
# {new_key: new_value for (index, row) in df.iterrows()}