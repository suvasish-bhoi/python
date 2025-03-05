#user registry
try:
    open('user.db', "r")
except FileNotFoundError:
    user_db = open('user.db','w')
    user_db.close()

#task manager persistent file
try:
    open('task.csv', "r")
except FileNotFoundError:
    task_db = open('task.csv','w')
    task_db.close()

current_user = []

def append_remaining_space(text,max_length):
    current_length = len(text)
    if current_length >= max_length:
        return text
    return text + ' ' * (max_length - current_length)

def add_task():
    if len(current_user) == 0:
        print('Please Login')
        login_prompt()
    task_details = input('Enter the task : ')
    if len(task_details) < 1 :
        add_task()
    else:
        task_db = open('task.csv', 'a')
        task_db.write(current_user[0]+","+task_details+","+"INCOMPLETE"+"\n")
        print('Task Added...')
        task_db.close()
        show_task_manager_menu()

def view_task():
    if len(current_user) == 0:
        print('Please Login')
        login_prompt()
    task_db = open('task.csv', 'r')
    lines = task_db.readlines()
    print('--------------------------------------------------------------------')
    print('|-----ID-----|------------TASK--------------|--------STATUS--------|')
    print('--------------------------------------------------------------------')
    count = 1
    for line in lines:
        userid = line.split(",")[0]
        if(userid == current_user[0]):
            print('|'+append_remaining_space(str(count),12)+'|'+append_remaining_space(line.split(',')[1],30)+"|"+append_remaining_space(line.split(',')[2],22)+'|')
            count = count+1
    print('-------------------------------------------------------------------')
    task_db.close()
    show_task_manager_menu()

def print_task():
    task_db = open('task.csv', 'r')
    lines = task_db.readlines()
    print('--------------------------------------------------------------------')
    print('|-----ID-----|------------TASK--------------|--------STATUS--------|')
    print('--------------------------------------------------------------------')
    count = 1
    for line in lines:
        userid = line.split(",")[0]
        if (userid == current_user[0]):
            print('|' + append_remaining_space(str(count), 12) + '|' + append_remaining_space(line.split(',')[1],
                                                                                              30) + "|" + append_remaining_space(
                line.split(',')[2], 22) + '|')
            count = count + 1
    print('-------------------------------------------------------------------')
    task_db.close()

def mark_task():
    if len(current_user) == 0:
        print('Please Login')
        login_prompt()
    print_task()
    task_id = int(input('Enter Task ID To Mark As Complete : '))
    task_db = open('task.csv', 'r')
    lines = task_db.readlines()
    count = 1
    new_file_lines = []
    for line in lines:
        userid = line.split(",")[0]
        if(userid == current_user[0]):
            if count == task_id:
                count = count + 1
                task_details = line.split(',')[1]
                new_file_lines.append(current_user[0]+","+task_details+","+"COMPLETE"+"\n")
        else:
            new_file_lines.append(line)
    task_db.close()
    task_db = open('task.csv', 'w')
    for line in new_file_lines:
        task_db.write(line)
    task_db.close()
    print('Task Deleted...')
    show_task_manager_menu()

def delete_task():
    if len(current_user) == 0:
        print('Please Login')
        login_prompt()
    print_task()
    task_id = int(input('Enter Task ID To Delete : '))
    task_db = open('task.csv', 'r')
    lines = task_db.readlines()
    count = 1
    new_file_lines = []
    for line in lines:
        userid = line.split(",")[0]
        if (userid == current_user[0]):
            if count == task_id:
                count = count + 1
                continue
            else:
                new_file_lines.append(line)
    task_db.close()
    task_db = open('task.csv', 'w')
    for line in new_file_lines:
        task_db.write(line)
    task_db.close()
    print('Task Deleted...')
    show_task_manager_menu()


def show_task_manager_menu():
    print('----------------------------------------------------')
    print('1 > Add Task')
    print('2 > View Task')
    print('3 > Mark Complete Task')
    print('4 > Delete Task')
    print('5 > Exit')
    task_menu_option = int(input('Enter desired input : '))
    if task_menu_option == 1:
        add_task()
    elif task_menu_option == 2:
        view_task()
    elif task_menu_option == 3:
        mark_task()
    elif task_menu_option == 4:
        delete_task()
    else:
        current_user.clear()
        print('Exiting.......')


def do_login(user_name, password):
    userdb = open('user.db', 'r')
    lines = userdb.readlines()
    user_found = False
    for line in lines:
        user = line.split('~')[1]
        passw = line.split('~')[2]
        if user_name == user and passw == password+"\n":
            user_found = True
            current_user.append(line.split('~')[0])
            break
    userdb.close()
    if user_found:
        print('Welcome user '+user_name)
        show_task_manager_menu()
    else:
        print('Username & Password not matching')
        main_menu()



def login_prompt():
    user_name = input('Enter your user name : ')
    password = input('Enter Password : ')
    do_login(user_name,password)


def find_total_user():
    userdb = open('user.db', 'r')
    lines = userdb.readlines()
    userdb.close()
    return len(lines)

def register_user(userName, password):
    userdb = open('user.db', 'a')
    id = find_total_user() + 1
    userdb.write(str(id)+"~"+userName+'~'+password+"\n")
    userdb.close()
    print('User Successfully Register.Please login...')

def registration_prompt():
    print('User Registration')
    print('-----------------')
    user_name = input('Enter your user name : ')
    password = input('Enter Password : ')
    if len(user_name) > 0 and len(password) > 0:
        register_user(user_name,password)
    else:
        print('User name or password can\'t be empty')
        registration_prompt()

def main_menu():
    print('Welcome to Task Manager')
    main_option = int(input('Press 1. For Login \nPress 2. For Registration : '))
    if main_option == 1:
        login_prompt()
    elif main_option == 2:
        registration_prompt()




main_menu()