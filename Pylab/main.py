import random
from random import randint
from src.module import Module
from src.student import Student 
import csv

courses = Module()

record = []

def main():

    print('='*40)
    print('     WELCOME TO TEESSIDE UNIVERSITY')
    print('='*40)
    print('\n1: Register New Student\n2: List all Modules\n3: List all Profiles\n4: Search by Student Name\n5: Search by Student ID\n6: Search by Join Date\n7: Update Profile\n8: Delete Profile\n9: Quit \n' )
    while True:
    
        option = input('Select Option Number:').strip()

        if option.isdigit() == True:
            if option == '1':
                register()
                break
            elif option == '2':
                courses.printer()
            else:
                print('Enter Valid Option Number')
                continue
        else:
            print('Enter a Valid Option Number')
            continue
        break
      


def register():
    while True:
        course = input('Are you Registering for CS/DS..?:').strip().upper()
        if course not in ['CS','DS']:
            print('Invalid Course, Please Choose from CS or DS')
            continue
        else:
            break
            
    while True:

        f_name = input('First Name:').strip().lower()
        m_name = input('Middle Name(Optional):').strip().lower()
        l_name = input('Last Name:').strip().lower()

        if f_name.isalpha() == False or (m_name != '' and m_name.isalpha()==False) or l_name.isalpha() == False:
            print('--Enter a Valid Name -- Only Alphbets and Middle name is optional---')
            continue
        else:
            break

    
    s_id = (f'C{str(randint(1000000,9999999))}')
    s_mail = (f'{s_id}@tees.ac.uk')

# Gets and Validates Gender and Assigns Title
    while True:
        gender = input('Enter Gender M/F:').strip().upper()

        if gender not in ['M','F']:
            print('Invalid Gender, Choose from M/F')
            continue
        else:
            if gender == 'M':
                title = 'MR'
            elif gender == 'F':
                title = 'MS'
            break
    
#Adding Modules Codes to a list    
    
    for key in courses.com.keys():      
        record.append(key)
    
    get_gen_courses()

    if course == 'CS':
        get_cs_courses()
    else:
        get_ds_courses()
    
    labels = ['ID','First Name','Middle Name','Last Name','Title','Mail','Course','Com_Module1','Com_Module2','g_opt1','g_opt2','opt3','opt4']

    details = [s_id,f_name,m_name,l_name,title,s_mail,course] + record

  
    with open('records.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow(details)



        






def get_gen_courses():
    
    i = 1
    m = list(courses.gen.keys())

    for key,value in courses.gen.items():
        print(f'{i} {key}: {value}')
        i += 1
    
    for p in range(2):
        while True:
            choice = input('Enter the Course Number:').strip()

            if choice.isdigit() == True and int(choice) > 0 and int(choice) <= i-1:
                record.append(m[int(choice)-1])
                break
            elif choice == '':
                
                p = random.choice(m)

                while True:
                    if p in record:
                        p = random.choice(m)
                    else: 
                        break

                record.append(p)
                break
            else: 
                print('Invalid Input entered try again')
                pass

    print(record)
        

def get_cs_courses():
    
    i = 1
    m = list(courses.cso.keys())

    for key,value in courses.cso.items():
        print(f'{i} {key}: {value}')
        i += 1
    
    for p in range(2):
        while True:
            choice = input('Enter the Course Number:').strip()

            if choice.isdigit() == True and int(choice) > 0 and int(choice) <= i-1:
                record.append(m[int(choice)-1])
                break
            elif choice == '':
                p = random.choice(m)
                
                while True:
                    if p in record:
                        p = random.choice(m)
                    else: 
                        break

                record.append(p)
                break
            else: 
                print('Invalid Input entered try again')
                pass

    print(record)


def get_ds_courses():
    
    i = 1
    m = list(courses.dso.keys())

    for key,value in courses.dso.items():
        print(f'{i} {key}: {value}')
        i += 1
    
    for p in range(2):
        while True:
            choice = input('Enter the Course Number:').strip()

            if choice.isdigit() == True and int(choice) > 0 and int(choice) <= i-1:
                record.append(m[int(choice)-1])
                break
            elif choice == '':
                p = random.choice(m)
                
                while True:
                    if p in record:
                        p = random.choice(m)
                    else: 
                        break

                record.append(p)
                break
            else: 
                print('Invalid Input entered try again')
                pass

    print(record)
    
    
       

        

            

    

    







if __name__ == '__main__':
    main()


