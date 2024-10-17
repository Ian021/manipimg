import json

# Open and read the JSON file
with open('./in/comet.json', 'r') as file:
    data = json.load(file)

# Print the data
for layer in data["layers"]:
    output = []

    width = layer["width"]
    height = layer["height"]

    for y in range(height):
        output.append(layer["chunks"][0]["data"][y*width:y*width+width])

    with open('./map/{0}.json'.format(layer["name"]), 'w') as outfile:
        json.dump(output, outfile, indent=2)
    
