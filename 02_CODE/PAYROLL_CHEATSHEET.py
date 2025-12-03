"""
PAYROLL PROGRAM - TEAM PAYMASTERS

Run: python3 payroll.py
Enter data for 10 employees. Results save to results.csv
"""

from typing import Dict, List
import csv


# CONFIGURATION

MAX_HOURS_ALLOWED = 80
STATE_TAX_RATE = 0.056
FEDERAL_TAX_RATE = 0.079
RESULTS: List[Dict] = []


# MODULE 1: INPUT & VALIDATION
# ALLEN POSTON

def get_employee_data() -> Dict | str:
    """Collect and validate employee data."""
    print("---- employee data entry ----")

    try:
        firstname = input("enter first name: ").strip()
        lastname = input("enter last name: ").strip()
        empid = input("enter employee id: ").strip()
        dependents_raw = input("enter number of dependents: ").strip()
        hours_raw = input("enter hours worked: ").strip()

        try:
            dependents = int(dependents_raw)
        except ValueError:
            print("error: dependents must be an integer.")
            return "invalid"

        try:
            hours_worked = float(hours_raw)
        except ValueError:
            print("error: hours worked must be a number.")
            return "invalid"

        if hours_worked < 0:
            print("error: negative hours not allowed.")
            return "invalid"

        if hours_worked > MAX_HOURS_ALLOWED:
            print("error: hours exceed maximum allowed.")
            return "invalid"

        if dependents < 0:
            print("error: dependents cannot be negative.")
            return "invalid"

        if empid == "":
            print("error: employee id required.")
            return "invalid"

        if hours_worked > 40:
            print("notice: overtime hours detected.")

        return {
            'FIRSTNAME': firstname,
            'LASTNAME': lastname,
            'EMPID': empid,
            'DEPENDENTS': dependents,
            'HOURSWORKED': hours_worked,
        }

    except KeyboardInterrupt:
        print("\nInput cancelled by user.")
        return "invalid"



# MODULE 2: PAYROLL CALCULATIONS
# ALEXANDER MANSFIELD

def get_pay_rate(empid: str) -> float:
    """Look up pay rate by employee ID."""
    payrate_map = {
        'E001': 20.0,
        'E002': 22.5,
        'E003': 18.0,
    }
    return payrate_map.get(empid, 20.0)


def calculate_payroll(hours_worked: float, pay_rate: float) -> Dict:
    """Calculate gross, overtime, taxes, and net pay."""
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(0.0, hours_worked - 40)

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross = regular_pay + overtime_pay

    state_tax = gross * STATE_TAX_RATE
    federal_tax = gross * FEDERAL_TAX_RATE
    net = gross - (state_tax + federal_tax)

    return {
        'PAYRATE': pay_rate,
        'GROSS': round(gross, 2),
        'OVERTIME': round(overtime_pay, 2),
        'STATE_TAX': round(state_tax, 2),
        'FEDERAL_TAX': round(federal_tax, 2),
        'NET': round(net, 2),
    }



# MODULE 3: OUTPUT & FILE
# ARMANDO OCHOA

def save_and_display_results(employee_data: Dict, payroll_data: Dict) -> None:
    """Store and display employee payroll results."""
    record = {
        'FIRSTNAME': employee_data['FIRSTNAME'],
        'LASTNAME': employee_data['LASTNAME'],
        'EMPID': employee_data['EMPID'],
        'HOURSWORKED': employee_data['HOURSWORKED'],
        'PAYRATE': payroll_data['PAYRATE'],
        'GROSS': payroll_data['GROSS'],
        'OVERTIME': payroll_data['OVERTIME'],
        'STATE_TAX': payroll_data['STATE_TAX'],
        'FEDERAL_TAX': payroll_data['FEDERAL_TAX'],
        'NET': payroll_data['NET'],
    }
    RESULTS.append(record)

    print("\n=== Payroll Result ===")
    print(f"Employee: {record['FIRSTNAME']} {record['LASTNAME']} (ID: {record['EMPID']})")
    print(f"Hours Worked: {record['HOURSWORKED']}")
    print(f"Pay Rate: ${record['PAYRATE']}/hr")
    print(f"Gross Pay: ${record['GROSS']}")
    print(f"Overtime Pay: ${record['OVERTIME']}")
    print(f"State Tax: ${record['STATE_TAX']}")
    print(f"Federal Tax: ${record['FEDERAL_TAX']}")
    print(f"Net Pay: ${record['NET']}")


def write_results_to_file(filename: str = 'results.csv') -> None:
    """Write all results to CSV file."""
    if not RESULTS:
        print("No results to write.")
        return

    fieldnames = ['FIRSTNAME', 'LASTNAME', 'EMPID', 'HOURSWORKED', 'PAYRATE', 'GROSS', 'OVERTIME', 'STATE_TAX', 'FEDERAL_TAX', 'NET']
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for r in RESULTS:
                writer.writerow(r)
        print(f"Results written to {filename}")
    except Exception as e:
        print(f"Error writing file: {e}")



# MODULE 4: TESTING & QA
# ANIYA HOWELL

def run_tests() -> None:
    """Run 10 test cases to verify program works."""
    print("Running test suite...")
    print("Test 1: Basic calculation (40 hours at $20/hr)")
    result = calculate_payroll(40, 20.0)
    print(f"  Gross: ${result['GROSS']} (expected $800)")
    
    print("\nTest 2: Overtime calculation (50 hours at $20/hr)")
    result = calculate_payroll(50, 20.0)
    print(f"  Gross: ${result['GROSS']} (expected $900)")
    print(f"  Overtime: ${result['OVERTIME']} (expected $300)")
    
    print("\nAdd 8 more test cases here...")



# MAIN PROGRAM

def main():
    print("Payroll system initializing...\n")
    employee_count = 0
    
    while employee_count < 10:
        employee_data = get_employee_data()
        if employee_data == "invalid":
            print("Please re-enter the employee record.\n")
            continue

        pay_rate = get_pay_rate(employee_data['EMPID'])
        payroll_data = calculate_payroll(employee_data['HOURSWORKED'], pay_rate)
        save_and_display_results(employee_data, payroll_data)

        employee_count += 1

    write_results_to_file()
    print("\nProcessing complete.")


if __name__ == '__main__':
    main()

