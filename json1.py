import json

data = '''
{
  "name" : "Ahmed",
  "phone" : {
    "type" : "intl",
    "number" : "+92 324 0003300"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
