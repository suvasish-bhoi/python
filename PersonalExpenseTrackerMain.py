import re

def mainMenu():
    print('----------------------------------------------------')
    print('1 > Add expense')
    print('2 > View expenses')
    print('3 > Track budget')
    print('4 > Save expenses')
    print('5 > Exit')

def menuConfirmation(value):
    if value == 1:
        return input("You have selected 'Add expense'. If Yes Y or N for Main Menu : ")
    elif value == 2:
        return input("You have selected 'View expenses'. If Yes Y or N for Main Menu : ")
    elif value == 3:
        return input("You have selected 'Track budget'. If Yes Y or N for Main Menu : ")
    elif value == 4:
        return input("You have selected 'Save expenses'. If Yes Y or N for Main Menu : ")
    elif value == 5:
        return input("Do You Want To Exit. If Yes Y or N  for Main Menu : ")


def is_valid_date(date_str):
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    if(bool(re.match(pattern, date_str))):
       return ''
    else:
        return 'Enter date in YYYY-MM-DD format only.And check DATE and MONTH properly'

def validate_expense(inputDate, inputCategory, inputAmount, inputNote):
    date_validation_result = is_valid_date(inputDate)
    if date_validation_result != '' :
        print(date_validation_result)
        return False
    if inputCategory == '':
        print('Category Empty')
        return False
    if inputAmount < 0:
        print('Amount should be greater than zero')
        return False
    return True

#draft expense
draft_expense = []

def add_expense_to_list(inputDate, inputCategory, inputAmount, inputNote):
    current_expense = {'DATE' : inputDate , 'CATEGORY' : inputCategory, 'AMOUNT' : inputAmount, 'NOTE' : inputNote}
    draft_expense.append(current_expense)

#persist expense in file
try:
    open('expense.csv', "r")
except FileNotFoundError:
    expense_db = open('expense.csv','w')
    expense_db.close()

def persist_expense():
    expense_db = open('expense.csv', 'a')
    for i in draft_expense:
        expense_db.write(i['DATE'] + ',' + i['CATEGORY'] + ',' + str(i['AMOUNT']) + ',' + i['NOTE'] + '\n')
    expense_db.close()

def add_expense():
    print('Adding Expense')
    print('---------------')
    date = input('Please enter Date in YYYY-MM-DD format : ')
    category = input('Please category of Expense : ').upper()
    amount = float(input('Enter Amount : '))
    note = input("Enter Description : ")
    if validate_expense(date,category,amount,note) :
        print('Saving to Draft')
        add_expense_to_list(date,category,amount,note)
        repeat_task = input('Do you want to add more expense. If Yes Y or N : ')
        if repeat_task == 'Y' :
            add_expense()
        elif repeat_task == 'N' :
            main_function()


def append_remaining_space(text,max_length):
    current_length = len(text)
    if current_length >= max_length:
        return text
    return text + ' ' * (max_length - current_length)

def view_expense():
    print('-----------------------------------------------------------------------------------')
    print('     DATE      |        CATEGORY         |    AMOUNT    |             NOTE        |')
    print('---------------|-------------------------|--------------|-------------------------|')
    expense_db = open('expense.csv','r')
    content = expense_db.readlines()
    for line in content:
        date, category, amount, note = line.split(',')
        print(append_remaining_space(date,15)+"|"+append_remaining_space(category,25)+"|"+
              append_remaining_space(amount,14)+"|"+append_remaining_space(note,25))
    print('-----------------------------------------------------------------------------------')
    expense_db.close()

def track_budget():
    budget = float(input('Enter your Budget : '))
    if budget < 0.0:
        print('Budget can\'t be less than 0')
        track_budget()
    else:
        expense_db = open('expense.csv', 'r')
        content = expense_db.readlines()
        total_expense = 0
        for line in content:
            total_expense = total_expense + float(line.split(',')[2])
        expense_db.close()
        if total_expense > budget:
            print('You have exceeded your budget!')
        else:
            print('Your have '+ str(budget - total_expense) + ' left for the month')
        main_function()

def save_expense():
    print('-------------------------------------')
    for i in draft_expense:
        print(i)
        print('-------------')
    print('-------------------------------------')
    save_input = input('Above is the draft expense.Do you want to Save. If Yes Y or Discard N : ')
    if save_input == 'Y':
        persist_expense()
        print('Saved....')
        draft_expense.clear()
        main_function()
    elif save_input == 'N':
        draft_expense.clear()
        print('Draft Cleared')
        main_function()

def main_function():
    print('____________Personal Expense Tracker________________')
    i = 0
    while (i == 0):
        mainMenu()
        inputValue = int(input('Enter desired input : '))
        confirmationValue = menuConfirmation(inputValue)
        if (confirmationValue == 'Y'):
            if inputValue == 1:
                add_expense()
            elif inputValue == 2:
                view_expense()
            elif inputValue == 3:
                track_budget()
            elif inputValue == 4:
                save_expense()
            elif inputValue == 5:
                print('Exiting App. Thank You')
                break
        else:
            continue


main_function()