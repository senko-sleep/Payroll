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
# Instructions: Collect employee data and validate it
# Functions: get_employee_data()

def get_employee_data() -> Dict | str:
    """Collect and validate employee data."""
    # TODO: Implement this function
    # Ask for: first name, last name, employee ID, dependents, hours worked
    # Validate: no negative hours, no hours > MAX_HOURS_ALLOWED, no negative dependents, ID not blank
    # Return: dict with keys 'FIRSTNAME','LASTNAME','EMPID','DEPENDENTS','HOURSWORKED' if valid
    # Return: string 'invalid' if validation fails
    pass


# MODULE 2: PAYROLL CALCULATIONS
# ALEXANDER MANSFIELD
# Instructions: Calculate pay, overtime, and taxes
# Functions: get_pay_rate(), calculate_payroll()

def get_pay_rate(empid: str) -> float:
    """Look up pay rate by employee ID."""
    # TODO: Implement this function
    # Use payrate_map to look up rates
    # Return: hourly pay rate
    payrate_map = {
        'E001': 20.0,
        'E002': 22.5,
        'E003': 18.0,
    }
    pass


def calculate_payroll(hours_worked: float, pay_rate: float) -> Dict:
    """Calculate gross, overtime, taxes, and net pay."""
    # TODO: Implement this function
    # Calculate: regular hours (up to 40), overtime hours (over 40)
    # Calculate: gross pay, overtime pay (1.5x), state tax (5.6%), federal tax (7.9%), net pay
    # Return: dict with keys 'PAYRATE','GROSS','OVERTIME','STATE_TAX','FEDERAL_TAX','NET'
    pass


# MODULE 3: OUTPUT & FILE
# ARMANDO OCHOA
# Instructions: Display results and save to file
# Functions: save_and_display_results(), write_results_to_file()

def save_and_display_results(employee_data: Dict, payroll_data: Dict) -> None:
    """Store and display employee payroll results."""
    # TODO: Implement this function
    # Combine employee_data and payroll_data into one record
    # Add record to RESULTS list
    # Print results on screen in readable format
    pass


def write_results_to_file(filename: str = 'results.csv') -> None:
    """Write all results to CSV file."""
    # TODO: Implement this function
    # Check if RESULTS has data
    # Open file for writing
    # Write header row and all records
    # Close file
    pass


# MODULE 4: TESTING & QA
# ANIYA HOWELL
# Instructions: Create 10 test cases to verify program works
# Functions: run_tests()

def run_tests() -> None:
    """Run 10 test cases to verify program works."""
    # TODO: Implement this function
    # Create 10 test cases:
    #   - 3-4 normal cases (under 40 hours)
    #   - 3-4 overtime cases (over 40 hours)
    #   - 2-3 error cases (invalid data)
    # For each test: run calculation, verify output, report pass/fail
    # Document all tests in 04_TESTING/TEST_RESULTS.txt
    pass


# MAIN PROGRAM

def main():
    """Main program loop."""
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

