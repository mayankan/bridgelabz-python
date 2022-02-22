import json

json_data = {
    "product": "Python book",
    "rating": "4.0",
    "about": "Nice book"
}


with open('test.json', 'w') as write_file:
    json.dump(json_data, write_file)
    write_file.close()


with open("test.json") as json_file:
    json_object = json.load(json_file)
    json_file.close()

product = json_object["product"]
rating = json_object["rating"]
about = json_object["about"]

print('Product: ', product)
print('Rating: ', rating)
print('About: ', about)
