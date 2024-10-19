import json

# Open and read the JSON file
with open('./in/comet.json', 'r') as file:
    data = json.load(file)

unique_ids = set()

# Print the data
for layer in data["layers"]:
    output = []

    for id in layer["chunks"][0]["data"]:
        if id != 0:
            unique_ids.add(id)

for id in unique_ids:
    print('mapAssets.addTexture({0}, "maps/tiles/tile_{0}.png", false);'.format(id))
    
