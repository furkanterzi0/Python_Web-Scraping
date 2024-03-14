import requests

class Github:
    def __init__(self):
        self.api_url='https://api.github.com'

    def getUser(self,username):
        response=requests.get(self.api_url+'/users/'+username)
        return response.json()
    def getRepositories(self,username):
        response=requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

github=Github()
while True:
    secim=input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSecim: ')
    
    if secim=='1':
        username=input('username: ')
        result= github.getUser(username)
        print(result["id"])
        break
    elif secim=='2':
        counter=1
        username=input('username: ')
        result=github.getRepositories(username)
        for x in result:
            print(str(counter)+'.repository name: ' + str(x['name'])+' || id: '+str(x['id']))
            counter+=1
        break
    elif secim=='3':
        break
    elif secim=='4':
        print("cikis")
        break
    else:
        print("hata")
        break
