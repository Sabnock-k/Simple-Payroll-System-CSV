'''

© SIMPLE PAYROL SYSTEM

'''

import csv
import os
import time

EMPLOYEE_FILE = 'employee.csv'
PAYROLL_FILE = 'payroll.csv'

def load_employee_file():
    employees = []
    try:
        with open(EMPLOYEE_FILE, mode='r', newline='') as csvfile:
            csv_Ereader = csv.DictReader(csvfile)
            for row in csv_Ereader:
                employees.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{EMPLOYEE_FILE}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return employees

def create_payroll():
    os.system('cls')
    print()
    print(f"{'CREATE PAYROLL'.center(20)}")
    print(f"{'-'*20}")
    
    employees = load_employee_file()

    while True:
        try:
            id_no = int(input("IDNO: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid ID number.")
            
    e_no = next((e for e in employees if int(e['IDNO']) == id_no), None)     

    if e_no:
        print(f"LASTNAME: {e_no['LASTNAME']}")
        print(f"FIRSTNAME: {e_no['FIRSTNAME']}")
        print(f"DAILY RATE: {e_no['DAILYRATE']}")
        
        while True:
            try:
                w_day = float(input("DAYS WORK: "))
                if w_day < 0:
                    print("Days worked cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid days of work.")
            
        print(f"{'-'*20}")
        
        total_pay = str(float(e_no['DAILYRATE']) * w_day)

        try:
            with open(PAYROLL_FILE, mode='a', newline='') as csvfile:
                csv_Pwriter = csv.writer(csvfile)
                if os.stat(PAYROLL_FILE).st_size == 0:
                    csv_Pwriter.writerow(['IDNO', 'LASTNAME', 'FIRSTNAME', 'DAILY RATE', 'DAYS WORK', 'TOTAL PAY'])
                csv_Pwriter.writerow([e_no['IDNO'], e_no['LASTNAME'], e_no['FIRSTNAME'], e_no['DAILYRATE'], w_day, total_pay])
            print("\nPAYROLL ENTRY CREATED SUCCESFULLY.")
        except Exception as e:
            print(f"An error occurred while writing to payroll: {e}")
        time.sleep(1)
    else:
        print("\nEMPLOYEE NOT FOUND.")
        time.sleep(1.1)


def show_payroll():
    os.system('cls')
    print()
    try:
        with open(PAYROLL_FILE, mode='r', newline='') as csvfile:
            csv_Preader = csv.reader(csvfile)
            print(f"{'PAYROLL LIST'.center(70)}")
            print(f"{'-' * 70}")
            print(f"{'IDNO'.ljust(6)}  {'LASTNAME'.ljust(10)}  {'FIRSTNAME'.ljust(10)}  {'DAILY RATE'.ljust(10)}  {'DAYS WORK'.ljust(12)}  {'TOTAL PAY'.ljust(10)}")
            print(f"{'-' * 70}")
            #CHECK IF DI EMPTY ANG PAYROLL_FILE
            if os.stat(PAYROLL_FILE).st_size != 0:
                #GI SKIP ANG HEADER KAY ANG HEADER NA PRINT NA DAAN
                next((csv_Preader),None)
                #GET THE START ROW THEN PRINT THE REST
                start_row = next(csv_Preader, None)
                if start_row:
                    print(f"{start_row[0].ljust(6)}  {start_row[1].ljust(10)}  {start_row[2].ljust(10)}  {start_row[3].ljust(10)}  {start_row[4].ljust(12)}  {start_row[5].ljust(10)}")
                    for row in csv_Preader:
                        print(f"{row[0].ljust(6)}  {row[1].ljust(10)}  {row[2].ljust(10)}  {row[3].ljust(10)}  {row[4].ljust(12)}  {row[5].ljust(11)}")
            else:
                print(f"\n{'LIST EMPTY'.center(70)}\n")
    except FileNotFoundError:
            print(f"Error: The file '{PAYROLL_FILE}' does not exist or Doesn't have data.")
    except Exception as e:
            print(f"An error occurred while writing to payroll: {e}") 

    print(f"{'-' * 70}")
    input("Press any key to exit..")

def show_employees():
    os.system('cls')
    print()
    print(f"{'EMPLOYEE LIST'.center(50)}")
    print(f"{'-'*50}")
    print(f"{'IDNO'.ljust(6)}  {'LASTNAME'.ljust(10)}  {'FIRSTNAME'.ljust(10)}  {'DAILYRATE'.ljust(10)}")
    print(f"{'-'*50}")    
    employees = load_employee_file()
    for row in employees:
        print(f"{row['IDNO'].ljust(6)}  {row['LASTNAME'].ljust(10)}  {row['FIRSTNAME'].ljust(10)}  {row['DAILYRATE'].ljust(10)}")
    print(f"{'-'*50}")
    exit = input("Press any key to exit..")

def menu():
    while True:
        os.system('cls')
        print()
        print(f"{'-'*7} Main Menu {'-'*7}")
        print("1. CREATE PAYROLL")
        print("2. SHOW PAYROLL LIST")
        print("3. SHOW EMPLOYEES")
        print("0. QUIT/END")
        print(f"{'-'*25}")
        choice = input("ENTER OPTION(0..3): ")
        
        match choice:
            case '1':
                create_payroll()
            case '2':
                show_payroll()
            case '3':
                show_employees()
            case '0':
                print("\nExiting...")
                return

def main():
    menu()

if __name__ == "__main__":
    main()
