import json

with open(r'C:\Users\306\Downloads\Ingles_Estrucutra_datos\muscle_groups.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for group in data['muscle_groups']:
    print(f"\nMuscle group: {group['name']}")
    for ex in group['exercises']:
        print(f" - {ex['name']} ({ex['type']}, {ex['equipment']}, Reps: {ex['reps_for_hypertrophy']})")
