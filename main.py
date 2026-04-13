from data.student import Student
from data.database import load_data , save_data

def menu():
    print("\n =========== Smart Student Management System ==============")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. View Students")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Exit")


def main():

    data = load_data()
    
    while True :
        menu()

        choice = input("Enter the choice : ")

        if choice == "1" :
            sid = int(input("Enter Student ID : \n"))
            name = input("Enter the Student Name : \n")

            if sid in data : 
                print("Student already exists")
            else : 
                data[sid] = {
                    "name" : name,
                    "marks" : {}
                }  
                save_data(data)  
                print("Student added")

        elif choice == "2" :
            sid = int(input("Enter Student ID : \n"))

            if sid not in data :
                print("Student not found")
                continue

            subject = input("Enter Subject : \n")
            mark = int(input("Enter Marks : "))

            data[sid]["marks"][subject] = mark
            save_data(data)
            print("Marks added")
            
        elif choice == "3" :
            pass

        elif choice == "4" :
            pass

        elif choice == "5" :
            pass

        elif choice == "6" :
            print("Existing System!!! ")
            break

        else : 
            print("Invalid Choice!!! ")


if __name__ == "__main__" :
    main()