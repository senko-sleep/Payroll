"""
payroll program - team paymasters

run: python3 payroll.py
enter data for 10 employees. results save to results.csv
"""

import csv
import os

# config
max_hours_allowed = 80
state_tax_rate = 0.056
federal_tax_rate = 0.079
results = []

# module 1: input & validation
# allen poston
# collect employee data and validate it

def get_employee_data():
    """get employee info and validate inputs strictly.

    - firstname / lastname: non-empty, letters only
    - hoursworked: float 0..max_hours_allowed
    - payrate: float > 0

    returns dict or 'invalid'
    """
    try:
        firstname = input("Enter first name (letters only, e.g., John, Mary): ").strip()
        lastname = input("Enter last name (letters only, e.g., Smith, ONeill): ").strip()

        if not firstname or any(not part.isalpha() for part in firstname.split()):
            print("Invalid first name.")
            return "invalid"

        if not lastname or any(not part.isalpha() for part in lastname.split()):
            print("Invalid last name.")
            return "invalid"

        hoursworked = float(input(
            f"Enter hours worked (0-{max_hours_allowed}). Example: 40, 35.5: "
        ).strip())
        if hoursworked < 0 or hoursworked > max_hours_allowed:
            print(f"Hours must be between 0 and {max_hours_allowed}.")
            return "invalid"

        payrate = float(input(
            "Enter hourly pay rate in USD. Example: 15.00, 22.50: "
        ).strip())
        if payrate <= 0:
            print("Pay rate must be greater than 0.")
            return "invalid"

        return {
            "firstname": firstname,
            "lastname": lastname,
            "hoursworked": hoursworked,
            "payrate": payrate,
        }

    except:
        print("Invalid input; try again.")
        return "invalid"


# module 2: payroll calculations
# alexander mansfield
# calculate pay, overtime, taxes

def calculate_payroll(hours_worked, pay_rate):
    """calculate gross pay, overtime, taxes, and net pay.

    - hours_worked: float, must be >= 0
    - pay_rate: float, must be > 0

    returns dict with keys:
        - payrate
        - gross
        - overtime
        - state_tax
        - federal_tax
        - net

    raises ValueError on invalid inputs
    """
    if hours_worked < 0 or pay_rate <= 0:
        raise ValueError("invalid payroll inputs")

    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5

    gross = regular_pay + overtime_pay
    state_tax = gross * state_tax_rate
    federal_tax = gross * federal_tax_rate
    net = gross - state_tax - federal_tax

    return {
        "payrate": pay_rate,
        "gross": round(gross, 2),
        "overtime": round(overtime_pay, 2),
        "state_tax": round(state_tax, 2),
        "federal_tax": round(federal_tax, 2),
        "net": round(net, 2),
    }


# module 3: output & file
# armando ochoa
# display results and save to file

def save_and_display_results(employee_data, payroll_data):
    """merge employee and payroll data, store in results list, print record.

    - employee_data: dict from get_employee_data()
    - payroll_data: dict from calculate_payroll()
    """
    record = {}
    record.update(employee_data)
    record.update(payroll_data)
    results.append(record)
    print(record)
    write_results_to_file()  # save to CSV immediately after each entry


def write_results_to_file(filename="02_CODE/results.csv"):
    """write accumulated results to csv file.

    - filename: string, output CSV filename
    """
    if not results:
        return

    fieldnames = list(results[0].keys())
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow(r)


# module 4: testing & qa
# aniya howell
# run test cases to check program works

def run_tests():
    """run predefined test cases to validate payroll logic.

    writes results to '04_testing/test_results.txt'
    """
    os.makedirs("04_testing", exist_ok=True)
    outfile = open("04_testing/test_results.txt", "w")

    test_cases = [
        # normal cases
        (30, 20.0),
        (40, 18.0),
        (25, 22.5),
        (10, 15.0),
        # overtime cases
        (45, 20.0),
        (50, 18.0),
        (60, 22.5),
        # edge cases
        (0, 20.0),
        (80, 15.0),
        # invalid case (should fail)
        (40, 0),
    ]

    passed = 0

    for i, (hours, rate) in enumerate(test_cases, start=1):
        try:
            calculate_payroll(hours, rate)
            if rate <= 0 or hours < 0:
                outfile.write(f"test {i}: fail (invalid input not caught)\n")
            else:
                outfile.write(f"test {i}: pass\n")
                passed += 1

        except ValueError:
            outfile.write(f"test {i}: pass (caught invalid input)\n")
            passed += 1

        except:
            outfile.write(f"test {i}: fail (unexpected exception)\n")

    outfile.write(f"\npassed {passed} / {len(test_cases)} tests\n")
    outfile.close()


# main program
def main():
    """main loop to collect 10 employee records and process payroll."""
    print("Payroll system initializing...\n")
    employee_count = 0

    while employee_count < 10:
        employee_data = get_employee_data()
        if employee_data == "invalid":
            print("Please re-enter the employee record.\n")
            continue

        payroll_data = calculate_payroll(
            employee_data["hoursworked"],
            employee_data["payrate"],
        )

        save_and_display_results(employee_data, payroll_data)
        employee_count += 1

    print("\nProcessing complete.")


if __name__ == "__main__":
    # run tests automatically first
    run_tests()
    # then run interactive payroll
    main()
