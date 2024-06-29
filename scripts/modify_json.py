import json

# read in data with old json format
with open('data/OLDworkouts.json', 'r') as file:
    data = json.load(file)

# transform the "sets" part
for entry in data:
    for exercise in entry['exercises']:
        exercise['sets'] = [{'reps': s[0], 'load': s[1]}
                            for s in exercise['sets']]

# save modified json data
with open('data/workouts_new_format.json', 'w') as file:
    json.dump(data, file, indent=4)
