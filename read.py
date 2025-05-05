import json

# Load the JSON file
with open('muscle_groups.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Print the data
for group, exercises in data.items():
    print(f"\nMuscle group: {group}")
    for exercise in exercises:
        print(f" - {exercise}")
