"""
qn
sampledict = {
"class : {"student:{"name :"mike","marks : {"physics":70,"history":80}}}}
"""

sampleDict = {
    "class": {
        "student":{
            "name": "Mike","marks":{
                "physics":70,"history":80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])

sample_dict = {
    "dict1" :{"name":"chithra","age":12,"course":"python"},
    "dict2" :{"place":"abc","qualification":"btech"},
    "dict3" :{"job":"pythondev","salary":25000}
}

x = sample_dict['job']="softwaredev"
print(x)