from src.module import Module
from src.student import Student 


courses = Module()
student = Student()

def main():

    print('='*40)
    print('     WELCOME TO TEESSIDE UNIVERSITY')
    print('='*40)
    print('\n1: Register New Student\n2: List all Modules\n3: List all Profiles\n4: Search by Student Name\n5: Search by Student ID\n6: Search by Join Date\n7: Update Profile\n8: Delete Profile\n9: Quit \n' )
    while True:
    
        option = input('Select Option Number:').strip()

        if option.isdigit() == True:
            if option == '1':
                student.register()
                print('Successfully Registered...!')
            elif option == '2':
                courses.printer()
            elif option == '3':
                student.listout()
            elif option == '4':
                student.search_by_name()
            elif option == '5':
                student.search_by_id()
            elif option == '6':
                student.search_by_date()
            elif option == '7':
                pass
            elif option == '8':
                student.delete_profile()
            elif option == '9':
                exit('Sucessfully Exited')
        else:
            print('Enter a Valid Option Number')
            continue
        break
      



if __name__ == '__main__':
    main()


