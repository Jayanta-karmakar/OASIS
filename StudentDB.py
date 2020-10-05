students = {"id":[],"name":[],"address":[],"ph_no":[]}
id=1
def AddData(num):
    global id
    for i in range(num):
        students['id'].append(id)
        students['name'].append(input("Enter the name: "))
        students['address'].append(input("Enter the address: "))
        students['ph_no'].append(input("Enter the contact no.: "))
        print()
        id += 1

def DelData(idno):
    indx=students['id'].index(idno)
    print("All information has been deleted for id",students['id'].pop(indx))
    students['name'].pop(indx)
    students['address'].pop(indx)
    students['ph_no'].pop(indx)
    print()

def ModData(idno):
    indx=students['id'].index(idno)
    students['name'][indx]=input("Enter new name: ")
    students['address'][indx]=input("Enter new address: ")
    students['ph_no'][indx]=input("Enter new ph_no: ")
    print("Data successfully updated")
    print()

def ShowData():
    print("{:^14}|{:^14}|{:^14}|{:^14}".format("ID","NAME","ADDRESS","PHONE NO."))
    print("{:-^14}|{:-^14}|{:-^14}|{:-^14}".format("--","----","-------","---------"))
    count=0
    while count<len(students['id']):
        print("{:^14}".format(students['id'][count]),end="|")
        print("{:^14}".format(students['name'][count]),end="|")
        print("{:^14}".format(students['address'][count]),end="|")
        print("{:^14}".format(students['ph_no'][count]))
        count+=1
    print()

while[1]:
    print("Press 1 for INSERT")
    print("Press 2 for DELETE")
    print("Press 3 for UPDATE")
    print("Press 4 for SHOWING DATA")
    print("Press 5 for EXIT")
    choice=int(input("Enter your choice: "))
    if choice==1:
        num=int(input("Enter the number of Students to be added: "))
        AddData(num)
    elif choice==2:
        idnod=int(input("Enter ID no.: "))
        DelData(idnod)
    elif choice==3:
        idnom=int(input("Enter ID no.: "))
        ModData(idnom)
    elif choice==4:
        ShowData()
    elif choice==5:
        print('Prgram closed successfully')
        break
    else:
        print("Wrong Choice")
        print()
    
