"""
PAYROLL PROGRAM - TEAM PAYMASTERS

Group Members:
- Allen Poston (Input & Validation)
- Alexander Mansfield (Payroll Calculations)
- Armando Ochoa (Output & File)
- Aniya Howell (Testing & QA)

HOW TO RUN:
python3 payroll.py

THEN:
- Enter employee data for up to 10 employees
- Results print to screen
- Results save to results.csv

Each person edits their functions. Do not edit other people's functions.
See TEAM_INSTRUCTIONS.md for what each person needs to do.
"""

from typing import Dict, Optional, Tuple, List
import csv

# ---------------------------
# Config / Constants
# ---------------------------
MAX_HOURS_ALLOWED = 80  # team can change this if required
STATE_TAX_RATE = 0.056
FEDERAL_TAX_RATE = 0.079
RESULTS: List[Dict] = []  # in-memory results store (Armando will extend)


def get_employee_data() -> Dict | str:
    """
    ALLEN POSTON: Collect and validate employee data.
    
    Ask the user for:
    - First name
    - Last name
    - Employee ID
    - Number of dependents
    - Hours worked
    
    Verify all data:
    - Hours cannot be negative
    - Hours cannot be more than MAX_HOURS_ALLOWED
    - Dependents cannot be negative
    - Employee ID cannot be blank
    - Show notice if hours are over 40
    
    Return:
    - Dict with keys: 'FIRSTNAME','LASTNAME','EMPID','DEPENDENTS','HOURSWORKED'
    - String 'invalid' if data fails validation (caller will ask user to retry)
    """
    print("---- employee data entry ----")

    try:
        firstname = input("enter first name: ").strip()
        lastname = input("enter last name: ").strip()
        empid = input("enter employee id: ").strip()
        dependents_raw = input("enter number of dependents: ").strip()
        hours_raw = input("enter hours worked: ").strip()

        # Basic parsing
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

        # Security checks
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

        # Package validated data for next module (keys in UPPERCASE per roadmap)
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


# ---------------------------
# ALEXANDER MANSFIELD: Payroll Calculations
# Do not edit anything else in this file. Only edit get_pay_rate() and calculate_payroll()
# ---------------------------
def get_pay_rate(empid: str) -> float:
    """
    ALEXANDER: Look up the pay rate for an employee based on their ID.
    
    Input: empid (employee ID like 'E001')
    Output: pay_rate (hourly rate like 20.0)
    
    For now, use the payrate_map below. Later you can add database lookup.
    If employee ID not found, return 20.0 as default.
    """
    # Placeholder pay-rate map (team can expand)
    payrate_map = {
        'E001': 20.0,
        'E002': 22.5,
        'E003': 18.0,
    }
    return payrate_map.get(empid, 20.0)


def calculate_payroll(hours_worked: float, pay_rate: float) -> Dict:
    """
    ALEXANDER: Calculate gross pay, overtime, taxes, and net pay.
    
    Inputs:
    - hours_worked (number of hours, like 45.0)
    - pay_rate (hourly rate, like 20.0)
    
    Calculate:
    - Regular hours: up to 40 hours
    - Overtime hours: any hours over 40
    - Regular pay: regular_hours * pay_rate
    - Overtime pay: overtime_hours * pay_rate * 1.5
    - Gross pay: regular_pay + overtime_pay
    - State tax: gross * 5.6%
    - Federal tax: gross * 7.9%
    - Net pay: gross - state_tax - federal_tax
    
    Return: Dict with keys 'PAYRATE','GROSS','OVERTIME','STATE_TAX','FEDERAL_TAX','NET'
    """
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


# ---------------------------
# ARMANDO OCHOA: Output & File
# Do not edit anything else in this file. Only edit save_and_display_results() and write_results_to_file()
# ---------------------------
def save_and_display_results(employee_data: Dict, payroll_data: Dict) -> None:
    """
    ARMANDO: Store each employee record and display it on screen.
    
    Input:
    - employee_data: dict with FIRSTNAME, LASTNAME, EMPID, DEPENDENTS, HOURSWORKED
    - payroll_data: dict with PAYRATE, GROSS, OVERTIME, STATE_TAX, FEDERAL_TAX, NET
    
    Do:
    1. Combine both dicts into one record
    2. Add the record to the RESULTS list
    3. Print the record nicely on screen
    
    The current display is simple. You can improve it with better formatting.
    """
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

    # Simple display (Armando can replace with nicer table printing)
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
    """
    ARMANDO: Write all results to a CSV file.
    
    Input:
    - filename: name of the file (default is 'results.csv')
    
    Do:
    1. Check if RESULTS list has any data
    2. Open a file for writing
    3. Write header row with column names
    4. Write each employee record as a new row
    5. Close the file
    6. Print message confirming the file was saved
    
    The CSV file should be readable in Excel or other programs.
    """
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


# ---------------------------
# ANIYA HOWELL: Testing & QA
# Do not edit anything else in this file. Only edit run_tests()
# ---------------------------
def run_tests() -> None:
    """
    ANIYA: Create and run 10 test cases to verify the program works.
    
    Create tests for:
    - 3-4 normal cases (under 40 hours) - should work fine
    - 3-4 overtime cases (over 40 hours) - should calculate overtime correctly
    - 2-3 error cases (negative hours, too many hours, missing data) - should be rejected
    
    For each test:
    1. Create test data (name, ID, hours, etc.)
    2. Run the calculation function with that data
    3. Check if the output matches what you expect
    4. Record pass or fail
    
    Document all tests in TEST_RESULTS.txt
    
    This function currently has one example. You should add 9 more tests.
    """
    print("Running example test: calculate_payroll()")
    sample = calculate_payroll(45, 20.0)
    expected_gross = round((40 * 20.0) + (5 * 20.0 * 1.5), 2)
    print(f"Expected gross: {expected_gross}, got: {sample['GROSS']}")
    print("Extend this function with full 10-case suite (see TODO).")


# ---------------------------
# Main integration loop
# ---------------------------
def main():
    print("Payroll system initializing...")
    employee_count = 0
    while employee_count < 10:
        employee_data = get_employee_data()
        if employee_data == "invalid":
            print("Please re-enter the employee record.\n")
            continue

        # Get pay rate (Alexander)
        pay_rate = get_pay_rate(employee_data['EMPID'])

        # Calculate payroll (Alexander)
        payroll_data = calculate_payroll(employee_data['HOURSWORKED'], pay_rate)

        # Save & display (Armando)
        save_and_display_results(employee_data, payroll_data)

        employee_count += 1

    # After loop finishes, write results to file (Armando)
    write_results_to_file()

    # Run tests if desired (Aniya)
    print("Processing complete. Team members: run `run_tests()` to execute test suite.")


if __name__ == '__main__':
    main()
