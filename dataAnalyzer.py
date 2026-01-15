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
