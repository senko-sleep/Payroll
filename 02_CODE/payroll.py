"""
payroll program - team paymasters

run: python3 payroll.py
enter data for 10 employees. results save to results.csv
"""

from typing import Dict, List
import csv

# config
max_hours_allowed = 80
state_tax_rate = 0.056
federal_tax_rate = 0.079
results: List[Dict] = []

# module 1: input & validation
# allen poston
# collect employee data and validate it

def get_employee_data() -> Dict | str:
    """get employee info and check it's valid."""
    # TODO: ask for first name, last name, id, dependents, hours worked
    # no negative hours, no hours > max_hours_allowed, no negative dependents, id can't be blank
    # return dict with keys 'firstname','lastname','empid','dependents','hoursworked' if valid
    # return 'invalid' if data is bad
    pass

# module 2: payroll calculations
# alexander mansfield
# calculate pay, overtime, taxes

def get_pay_rate(empid: str) -> float:
    """look up pay rate by employee id."""
    payrate_map = {
        'E001': 20.0,
        'E002': 22.5,
        'E003': 18.0,
    }
    # TODO: return hourly pay rate from map
    pass

def calculate_payroll(hours_worked: float, pay_rate: float) -> Dict:
    """calc gross, overtime, taxes, net pay."""
    # TODO: split hours into regular (up to 40) and overtime (over 40)
    # gross pay = regular + overtime (1.5x)
    # state tax, federal tax, net pay
    # return dict with keys 'payrate','gross','overtime','state_tax','federal_tax','net'
    pass

# module 3: output & file
# armando ochoa
# display results and save to file

def save_and_display_results(employee_data: Dict, payroll_data: Dict) -> None:
    """save results and print them."""
    # TODO: merge employee_data and payroll_data
    # add to results list
    # print in readable format
    pass

def write_results_to_file(filename: str = 'results.csv') -> None:
    """write all results to a csv file."""
    # TODO: check if results list has data
    # open file, write header + all records, close file
    pass

# module 4: testing & qa
# aniya howell
# run test cases to check program works

def run_tests() -> None:
    """run 10 test cases to make sure everything works."""
    # TODO: 3-4 normal cases (under 40 hrs)
    # 3-4 overtime cases (over 40 hrs)
    # 2-3 error cases (invalid data)
    # run calculation, check output, report pass/fail
    # save results in 04_testing/test_results.txt
    pass

# main program
def main():
    """main loop for payroll system."""
    print("payroll system initializing...\n")
    employee_count = 0
    
    while employee_count < 10:
        employee_data = get_employee_data()
        if employee_data == "invalid":
            print("please re-enter the employee record.\n")
            continue

        pay_rate = get_pay_rate(employee_data['empid'])
        payroll_data = calculate_payroll(employee_data['hoursworked'], pay_rate)
        save_and_display_results(employee_data, payroll_data)

        employee_count += 1

    write_results_to_file()
    print("\nprocessing complete.")

if __name__ == '__main__':
    main()
