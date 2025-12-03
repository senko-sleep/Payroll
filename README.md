# START HERE - Project Overview

## Quick Links

### Setup & Instructions
- [Team Instructions](01_SETUP/TEAM_INSTRUCTIONS.md) - **READ THIS FIRST**
- [Completion Checklist](01_SETUP/COMPLETION_CHECKLIST.txt) - Step by step task list

### Code
- [payroll.py](02_CODE/payroll.py) - Main program file (everyone edits their section)

### Documentation
- [Project Plan](03_DOCUMENTATION/PROJECT_PLAN.txt) - What each person is doing
- [Security Explanation](03_DOCUMENTATION/SECURITY_EXPLANATION.txt) - How we prevent bad data
- [Grading Rubric](03_DOCUMENTATION/GRADING_RUBRIC.txt) - Scoring breakdown

### Testing
- [Test Results](04_TESTING/TEST_RESULTS.txt) - Document your 10 test cases here

---

## What This Project Is

You are building a payroll program for 10 employees. The program:
1. Asks for employee information (name, ID, hours worked, etc.)
2. Checks the data is valid (rejects bad data)
3. Calculates gross pay, overtime, and taxes
4. Displays results on screen
5. Saves results to a file

---

## Team Roles

**Allen Poston** - Input & Validation
- Collects employee data
- Validates all data is correct
- Rejects bad data with error messages

**Alexander Mansfield** - Payroll Calculations
- Calculates pay rates
- Calculates gross pay and overtime
- Calculates state and federal taxes
- Calculates net pay

**Armando Ochoa** - Output & File
- Displays results on screen
- Saves results to CSV file

**Aniya Howell** - Testing & QA
- Creates 10 test cases
- Tests the entire program
- Documents all test results

---

## How to Get Started

1. **Everyone** reads [Team Instructions](01_SETUP/TEAM_INSTRUCTIONS.md)
2. **Everyone** reads [Grading Rubric](03_DOCUMENTATION/GRADING_RUBRIC.txt)
3. **Everyone** opens [payroll.py](02_CODE/payroll.py)
4. Each person edits ONLY their assigned functions (marked with their name)
5. Use [Completion Checklist](01_SETUP/COMPLETION_CHECKLIST.txt) to track progress

---

## Running the Program

```bash
python3 payroll.py
```

Then enter employee data for up to 10 employees. Results print to screen and save to `results.csv`.

---

## Key Files to Know

| File | Purpose | Owner |
|------|---------|-------|
| payroll.py | Main program | Everyone (edit your section only) |
| results.csv | Output file | Created by program |
| TEST_RESULTS.txt | Test documentation | Aniya |
| PROJECT_PLAN.txt | Team plan | All (read) |
| SECURITY_EXPLANATION.txt | How we validate data | Allen |
| GRADING_RUBRIC.txt | Scoring | Instructors |

---

## Communication

- If you're stuck, ask your team immediately
- Check variable names match between sections
- Test often, don't wait until the end
- Run the full program frequently to catch problems early

---

## Submission

When you're done, make sure you have:
- payroll.py (runs without errors)
- results.csv (example output)
- TEST_RESULTS.txt (all 10 tests documented)
- PROJECT_PLAN.txt (filled in)
- SECURITY_EXPLANATION.txt (filled in)
- All code has comments explaining what it does
