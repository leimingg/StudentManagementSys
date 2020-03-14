import time
import os

# define a list to store all student information (every student is a dictionary)
info_list = []


def print_menu():
    print("-----------------------------------------")
    print("      Student Management System V1.0")
    print(" 1:Add Student")
    print(" 2:Delete Student")
    print(" 3:Modify Student")
    print(" 4:Search Student")
    print(" 5:Display Student")
    print(" 6:Save Data")
    print(" 7:Exit System")
    print("-----------------------------------------")


def add_new_info():
    # Add student information
    global info_list

    new_name = input("Enter name:")
    new_tel = input("Enter phone number:")
    new_email = input("Enter email:")

    for temp_info in info_list:
        if temp_info['name'] == new_name:
            print("Your name has been used, please enter a new one")
            return
    # define a dictionary to store student information
    info = {}
    # add data to dictionary
    info["name"] = new_name
    info["tel"] = new_tel
    info["email"] = new_email
    # add dictionary to list
    info_list.append(info)


def del_info():
    global info_list

    del_num = int(input("Enter ID# you want to delete: "))
    if 0 <= del_num < len(info_list):
        del_flag = input("Are you confirm to delete? yes or no")
        if del_flag == "yes":
            del info_list[del_num]
    else:
        print("Entered wrong ID, please enter again.")


def modify_info():
    global info_list
    modify_num = int(input("Enter ID# you want to modify:"))
    if 0 <= modify_num < len(info_list):
        print("You want to modify: ")
        print("name:%s, tel:%s, email:%s" % (info_list[modify_num]['name'],
                                             info_list[modify_num]['tel'], info_list[modify_num]['email']))
        info_list[modify_num]['name'] = input("Enter name:")
        info_list[modify_num]['tel'] = input("Enter phone number:")
        info_list[modify_num]['email'] = input("Enter email:")
    else:
        print("Enter wrong ID, please enter again.")


def search_info():
    search_name = input("Enter student name you want to search:")
    for temp_info in info_list:
        if temp_info['name'] == search_name:
            print("Searched information:")
            print("name:%s, tel:%s, email:%s" % (temp_info['name'],
                                                 temp_info['tel'], temp_info['email']))
            break
    else:
        print("No information found")


def print_all_info():
    print("ID\tName\t\tPhone\t\tEmail")
    i = 0
    for temp in info_list:
        print("%d\t%s\t\t%s\t\t%s" % (i, temp['name'], temp['tel'], temp['email']))
        i += 1


def save_data():
    f = open("info_data.txt", "w")
    f.write(str(info_list))
    f.close()


def load_data():
    global info_list
    f = open("info_data.txt")
    content = f.read()
    info_list = eval(content)
    f.close()


def main():
    load_data()

    while True:
        # print out main menu
        print_menu()
        # take user input
        num = input("Enter your choice(integer):")
        # call function based on user input
        if num == "1":
            # Add student
            add_new_info()
        elif num == "2":
            # Delete student
            del_info()
        elif num == "3":
            # Modify student
            modify_info()
        elif num == "4":
            # search student
            search_info()
        elif num == "5":
            # traverse all info
            print_all_info()
        elif num == "6":
            # save data into text file
            save_data()
        elif num == "7":
            # ext system
            exit_flag = input("Are you confirm to exit?~~~~(>_<)~~~~(yes or no) ")
            if exit_flag == "yes":
                break
        else:
            print("Enter wrong information. please enter again......")

        input("\n\n\nEnter....")
        os.system("cls")  # clear cml

    # program start
main()
