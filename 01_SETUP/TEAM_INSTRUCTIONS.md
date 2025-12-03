# Team A - Step by Step Instructions

## Group Info
- **Group Name:** Team PayMasters
- **Members:** Allen Poston, Alexander Mansfield, Armando Ochoa, Aniya Howell

---

## What You're Building
A payroll program that takes employee information for 10 employees and calculates their pay with taxes.

---

## Step 1: Allen Poston - Input & Validation Module

**Your job:** Collect employee data and check it is correct.

**What to do:**
1. Ask for: first name, last name, employee ID, dependents, hours worked
2. Check the data is valid:
   - Hours cannot be negative
   - Hours cannot be more than 80 (your team's max)
   - Dependents cannot be negative
   - Employee ID cannot be blank
   - If hours are over 40, show a notice about overtime
3. If data is bad, reject it and ask again
4. If data is good, send it to the next step

**Code location:** Function `get_employee_data()` in `payroll.py`

**How to know you're done:**
- Run the program and enter valid data - it accepts it
- Run the program and enter bad data (like -5 hours) - it rejects it and asks again

---

## Step 2: Alexander Mansfield - Payroll Calculations Module

**Your job:** Calculate pay, overtime, and taxes.

**What to do:**
1. Get the hourly pay rate for each employee (use the pay rate map provided)
2. Calculate gross pay:
   - Regular pay = hours up to 40 × pay rate
   - Overtime pay = hours over 40 × pay rate × 1.5
   - Gross = regular pay + overtime pay
3. Calculate taxes:
   - State tax = gross × 5.6%
   - Federal tax = gross × 7.9%
4. Calculate net pay:
   - Net = gross - state tax - federal tax

**Code location:** Functions `get_pay_rate()` and `calculate_payroll()` in `payroll.py`

**How to know you're done:**
- Run the program and check the numbers are correct
- Example: 40 hours at $20/hr should give $800 gross
- Example: 50 hours at $20/hr should give $900 gross (40×20 + 10×20×1.5)

---

## Step 3: Armando Ochoa - Output & File Module

**Your job:** Save results and display them nicely.

**What to do:**
1. Store each employee's complete record (name, hours, pay, taxes, net)
2. Display results on screen in a clear format
3. Save all results to a CSV file (results.csv)

**Code location:** Functions `save_and_display_results()` and `write_results_to_file()` in `payroll.py`

**How to know you're done:**
- Run the program with employee data
- See results printed on screen
- Check that results.csv file is created with all the data

---

## Step 4: Aniya Howell - Testing & Quality Assurance

**Your job:** Test the entire program and report results.

**What to do:**
1. Create 10 test cases with fake employee data
2. Test cases should include:
   - 3-4 normal cases (under 40 hours)
   - 3-4 overtime cases (over 40 hours)
   - 2-3 error cases (negative hours, too many hours, missing ID, etc.)
3. For each test, run the program and record:
   - Test case name
   - Input data
   - Expected output
   - Actual output
   - Pass or Fail
4. Document all your tests in `test_results.txt`

**Code location:** Function `run_tests()` in `payroll.py`

**How to know you're done:**
- You have 10 documented test cases
- Each test shows pass or fail
- All normal cases pass
- All error cases are rejected properly

---

## How to Run the Program

From the terminal:
```
python3 payroll.py
```

Enter employee data when prompted. Repeat for all 10 employees. Results save to `results.csv`.

---

## Files You'll Create/Update

- `payroll.py` - Main program (everyone edits their section)
- `results.csv` - Output file (created when program runs)
- `test_results.txt` - Testing documentation (Aniya creates this)
- `SECURITY_EXPLANATION.txt` - Explain your security checks (Allen writes)
- `PROJECT_PLAN.txt` - Your development plan (everyone contributes)

---

## Final Submission Checklist

Before submitting, verify you have ALL of these:

- [ ] `payroll.py` runs without errors
- [ ] Program accepts valid employee data
- [ ] Program rejects invalid data (shows error messages)
- [ ] Calculations are correct (gross, overtime, taxes, net)
- [ ] Results display on screen
- [ ] Results save to `results.csv`
- [ ] `test_results.txt` with 10 test cases documented
- [ ] `SECURITY_EXPLANATION.txt` explaining all checks
- [ ] `PROJECT_PLAN.txt` describing how team divided the work
- [ ] Example `results.csv` file showing real program output

---

## Quick Reference: What Each Person Codes

**Allen:** Everything in `get_employee_data()` function
**Alexander:** Everything in `get_pay_rate()` and `calculate_payroll()` functions
**Armando:** Everything in `save_and_display_results()` and `write_results_to_file()` functions
**Aniya:** All of `run_tests()` function + create test documentation

---

## Communication Tips

- Use Discord or email to share updates
- Test your section before passing to the next person
- If something doesn't work, describe the problem clearly
- Check that variable names match what the previous person made
- Run the full program often to catch problems early
