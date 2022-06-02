import json
with open ('input.json','w') as f:
    
#writing data to the json file
 employee='{"id":"DV004", "name":"Joshua","role":"Developer","company":"Swahilipot Hub"}'
 employee_dict=json.loads(employee)
 print(employee_dict['name'])
print("Hello Joshua!! You have successfully created a json file")
    