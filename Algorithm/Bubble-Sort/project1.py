"""
One real project example where the bubble sort algorithm might be
used is in a program that sorts student records based on their test scores.
Suppose the program receives a CSV file containing the student records,
with each record containing the student's name and their test score.
The program needs to sort the records in descending order of the test scores,
so that the students with the highest scores appear first.
"""

import csv


def bubble_sort_ascending(records):
    n = len(records)
    for i in range(n):
        for j in range(0, n - i - 1):
            if float(records[j]['score']) < float(records[j + 1]['score']):
                records[j], records[j + 1] = records[j + 1], records[j]


# Read the CSV file into an array of records
with open('student_records.csv', 'r') as f:
    reader = csv.DictReader(f)
    records = [row for row in reader]

# Sort the records based on the test score
bubble_sort_ascending(records)

# Print the sorted records
for record in records:
    print(f"{record['name']}: {record['score']}")

print("\n================================")


def bubble_sort_descending(records):
    n = len(records)
    for i in range(n):
        for j in range(0, n - i - 1):
            if float(records[j]['score']) > float(records[j + 1]['score']):
                records[j], records[j + 1] = records[j + 1], records[j]


# Read the CSV file into an array of records
with open('student_records.csv', 'r') as f:
    reader = csv.DictReader(f)
    records = [row for row in reader]

# Sort the records based on the test score in descending order
bubble_sort_descending(records)

# Print the sorted records
for record in records:
    print(f"{record['name']}: {record['score']}")
