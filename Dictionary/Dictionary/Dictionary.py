#key-value

plakalar= {'kocaeli': 41,'istanbul':34}
print(plakalar['kocaeli'])

plakalar['Ankara']=6

print(plakalar)
print('-------------')

users={
        'furkan':{
            'age':36,'email':['f@gmilc.m','es']
        },
         'erkan':{
            'age':36,'email':'f@gmilc.m'
        }
    }
print(users)
print('------------------')

print("furkanin yasi: " + str(users['furkan']['age']))
print("furkanin 1. emaili: " + str(users['furkan']['email'][0]))
print("furkanin 2. emaili: " + str(users['furkan']['email'][1]))