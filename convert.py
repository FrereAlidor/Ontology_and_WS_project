from owlready2 import *
import json

# Load the OWL ontology
onto_path.append("path/to/your/ontology")
onto = get_ontology("file://path/to/your/ontology.owl").load()

# Convert the OWL ontology to a Python dictionary
def convert_to_dict(entity):
    result = {}

    for prop in entity.get_properties():
        values = []
        for value in prop[entity]:
            if isinstance(value, Entity):
                values.append(convert_to_dict(value))
            else:
                values.append(value)
        result[prop.python_name] = values

    return result

ontology_dict = convert_to_dict(onto)

# Convert the dictionary to JSON
json_data = json.dumps(ontology_dict, indent=4)

# Write the JSON to a file
with open("path/to/your/output.json", "w") as json_file:
    json_file.write(json_data)

print("Conversion completed successfully.")