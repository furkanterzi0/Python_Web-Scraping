import json

person_string='{"name":"furkan","languages":["python","c#"]}'

#JSON string to dict
result=json.loads(person_string)
result=result["name"]

person_dict={
    "name":"ali",
    "langues":["c#","c++"]
    }
result=json.dumps(person_dict)#dic to string
print(result)
