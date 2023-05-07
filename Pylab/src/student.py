import os
import csv
from src.module import Module
from random import randint
import datetime
import csv
import random
from tabulate import tabulate


courses = Module()
record = []

class Student():
    def __init__(self):
        pass

    #Lists out all provfiles in the record
    def listout(self):
        if os.path.isfile('records.csv') is False:
            print('Records does not exists yet..!')
        else:
            with open('records.csv') as csv_file:
                csv_reader = csv.reader(csv_file)
                headers = next(csv_reader)  # read the first row as headers
                rows = list(csv_reader)
                selected_columns = [row[:14] for row in rows]
                print(tabulate(selected_columns, tablefmt='fancy_grid'))
    
    #Registers a New Student into records
    def register(self):
        while True:
            course = input('Are you Registering for CS/DS..?:').strip().upper()
            if course not in ['CS','DS']:
                print('Invalid Course, Please Choose from CS or DS')
                continue
            else:
                break
                
        while True:

            f_name = input('First Name:').strip().upper()
            m_name = input('Middle Name(Optional):').strip().upper()
            l_name = input('Last Name:').strip().upper()

            if f_name.isalpha() == False or (m_name != '' and m_name.isalpha()==False) or l_name.isalpha() == False:
                print('--Enter a Valid Name -- Only Alphbets and Middle name is optional---')
                continue
            else:
                break

        
        s_id = (f'C{str(randint(1000000,9999999))}')
        s_mail = (f'{s_id}@tees.ac.uk')
        date = datetime.date.today()

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
        
        self.get_gen_courses()

        if course == 'CS':
            self.get_cs_courses()
        else:
            self.get_ds_courses()
        
        labels = ['ID','Date','First Name','Middle Name','Last Name','Title','Mail','Course','Com_Module1','Com_Module2','g_opt1','g_opt2','opt3','opt4']

        details = [s_id,date,f_name,m_name,l_name,title,s_mail,course] + record 

        if os.path.isfile('records.csv') is False:
            with open('records.csv','w') as file:
                writer = csv.writer(file)
                writer.writerow(labels)


        with open('records.csv','a') as file:
            writer = csv.writer(file)
            writer.writerow(details)




    def get_gen_courses(self):
        
        i = 1
        print('-'*20)
        print('General Modules: Select Two from the below options')
        print('-'*20)
        m = list(courses.gen.keys())

        for key,value in courses.gen.items():
            print(f'{i}. {key}: {value}')
            i += 1
        
        print('\n')

        for p in range(2):
            while True:
                choice = input('Enter the Course Number (or) Press "ENTER" for a random Module:').strip()

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

        
        

    def get_cs_courses(self):
        
        i = 1
        print('-'*20)
        print('Computer science Modules: Select Two from the below options')
        print('-'*20)
        m = list(courses.cso.keys())

        for key,value in courses.cso.items():
            print(f'{i}. {key}: {value}')
            i += 1
        
        print('\n')
        for p in range(2):
            while True:
                choice = input('Enter the Course Number (or) Press "ENTER" for a random Module:').strip()

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

        


    def get_ds_courses(self):
        
        i = 1
        print('-'*20)
        print('Data Science Modules: Select Two from the below options')
        print('-'*20)
        m = list(courses.dso.keys())

        for key,value in courses.dso.items():
            print(f'{i}. {key}: {value}')
            i += 1
        
        print('\n')

        for p in range(2):
            while True:
                choice = input('Enter the Course Number (or) Press "ENTER" for a random Module:').strip()

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

    def search_by_name(self):
        search_term = input('Enter First Name:').strip().upper()
        results =[]
        with open('records.csv','r') as file:
            rows = csv.reader(file)

            for row in rows:
                if search_term in row:
                    results.append(row)
            
            print(tabulate(results, tablefmt='fancy_grid'))
    

    def search_by_id(self):
        search_term = input('Enter Student ID:').strip().upper()
        results =[]
        with open('records.csv','r') as file:
            rows = csv.reader(file)

            for row in rows:
                if search_term in row:
                    results.append(row)
            
            print(tabulate(results, tablefmt='fancy_grid'))

    

    def search_by_date(self):
        try:
            year = int(input('Enter Year(YYYY):').strip())
            month = int(input('Enter Month(MM):').strip())
            day = int(input('Enter Day(DD):').strip())
            

        except ValueError as e:
            print(e)
            self.search_by_date()
        
        results =[]
        search_term = str(f'{year:04d}-{month:02d}-{day:02d}')
        with open('records.csv','r') as file:
            rows = csv.reader(file)

            for row in rows:
                if search_term in row:
                    results.append(row)
            
            print(tabulate(results, tablefmt='fancy_grid'))

    
    def update_profile(self):
        search_term = input('Enter Student ID:').strip().upper()
        
    

    def delete_profile(self):
        search_term = input('Enter Student ID:').strip().upper()

        with open('records.csv','r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            i = 0
            for row in rows:
                if search_term in row:
                    break
                i += 1
            
            rows.pop(i)

            with open('records.csv','w') as file:
                writer = csv.writer(file)

                for row in rows:
                    writer.writerow(row)
              
                
            print('Succesfully Deleted..!')