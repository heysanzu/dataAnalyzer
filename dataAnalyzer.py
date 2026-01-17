# Create data as a list of dictionaries
data = [
    {'Name': 'Sanzu', 'Age': 20, 'Score': 99},
    {'Name': 'Bob', 'Age': 25, 'Score': 90},
    {'Name': 'Charlie', 'Age': 23, 'Score': 88}
]
# Show the whole table
for row in data:
    print(row)

# Get basic statistics for Age and Score
ages = [row['Age'] for row in data]
scores = [row['Score'] for row in data]

print("Age - min:", min(ages), "max:", max(ages), "mean:", sum(ages)/len(ages))
print("Score - min:", min(scores), "max:", max(scores), "mean:", sum(scores)/len(scores))

# Access the Age column
print("Ages:", ages)

# Filter rows (e.g., Age > 21)
filtered = [row for row in data if row['Age'] > 21]
print("People with Age > 21:", filtered)

# Find the person with the highest score
highest = max(data, key=lambda x: x['Score'])
print("Person with highest score:", highest)

# Sort data by Age (ascending)
sorted_by_age = sorted(data, key=lambda x: x['Age'])
print("Sorted by Age:", sorted_by_age)

# Add a new person
data.append({'Name': 'Amit', 'Age': 22, 'Score': 91})
print("After adding Amit:", data)

# Average score for people older than 21
scores_over_21 = [row['Score'] for row in data if row['Age'] > 21]
if scores_over_21:
    print("Average score (Age > 21):", sum(scores_over_21)/len(scores_over_21))
else:
    print("No one over 21.")
