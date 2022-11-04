from time import sleep
from firebase import firebase
firebase =firebase.FirebaseApplication('https://abcd-d446c-default-rtdb.firebaseio.com',None)
for i in range(1,6):
    office=firebase.get('/'+str(i),None)
    sleep(1)
    office=str(office)
    if office=="1":
        Data=input("enter 999")
        firebase.patch('/',{str(i):Data})
        sleep(1)
        Receiver=firebase.get('/'+'R'+str(i),None)
        sleep(1)
        Receiver =str(Receiver)
        while Receiver=="0":
            Receiver=firebase.get('/'+'R'+str(i),None)
        print("ok ,Done")
        Data=input("enter 999")
        firebase.patch('/',{'R'+str(i):Data})
        sleep(2)
        firebase.patch('/',{'R'+str(i):"0"})
        firebase.patch('/',{str(i):"0"})
        Data=""