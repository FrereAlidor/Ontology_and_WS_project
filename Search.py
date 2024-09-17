from tinydb import TinyDB,Query
import Preprocessing


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
with open("db.json", "w") as json_file:
    json_file.write(json_data)

print("Conversion completed successfully.")



db = TinyDB('db.json')
qr = Query()
def search(sentence):
    result={}
    words = Preprocessing.Clean(sentence)

    for word in words:
        q = db.search(qr.Word == word)
        rating =[]

        try:
            for i in range(len(q[0]['Count'])):
                rating.append(q[0]['Place'][i] - q[0]['Count'][i])
            documents=q[0]['Documents']
            rating, documents = (list(t) for t in zip(*sorted(zip(rating, documents))))
            result[word]=documents
        except:
            pass
    if  sentence.startswith('"') and sentence.endswith('"'):
        res=()
        if len(words)>1 and result:
            for r in result:
                if res:
                    res=res.intersection(result[r])
                else:
                    res=set(result[r])
            return{'result':list(res)}
        else:
            return result
    else:
        return result

