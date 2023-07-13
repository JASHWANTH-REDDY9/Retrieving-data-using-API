import requests
import json
import pprint
x=int(input('Enter your Hall Ticket number :  '))
url="http://teleuniv.in/netra/api.php"
attendence = json.dumps({"method": "314", "rollno": x})
data=json.dumps({"method": "32", "rollno": x})
res = requests.post(url, attendence)
res1=requests.post(url,data)
d={}
dict = json.loads(res.text)
dict1=json.loads(res1.text)
indent1=json.dumps(dict1,indent=4)
for i in range(len(dict["overallattperformance"]['overall'])):
    if (dict["overallattperformance"]['overall'][i]['percentage'])!='--':
        d[dict["overallattperformance"]['overall'][i]['subjectname']]=dict["overallattperformance"]['overall'][i]['percentage']
    else:
        d[dict["overallattperformance"]['overall'][i]['subjectname']]=dict["overallattperformance"]['overall'][i]['practical']
while True:
    print('What do you want to retrive ?\n 1. Attendence \n 2. Your data \n 3. Exit')
    choice=int(input('Enter your choice : '))
    if choice==1:         
        i=1
        s1=0
        s2=0
        sem1=[]
        sem2=[]
        for it,val in d.items():
            if i<=10:
                s1+=int(val)
                sem1.append((f'{it} --> {val} %'))
            else:
                s2+=int(val)
                sem2.append((f'{it} --> {val} %'))
            i+=1
        print('Sem 1 attendence :\n')
        for i in sem1:
            print(i)
        print()
        print(s1/10,'-> Total attendence of sem 1 \n')
        print('Sem 2 attendance :\n')
        for j in sem2:
            print(j)
        print()
        print(s2/10,'-> Total attendence of sem 2 \n')
    elif choice==2:
        print('Your data :\n')
        print(indent1)
    else:
        break 