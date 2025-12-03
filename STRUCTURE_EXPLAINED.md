# Project Structure Explained

## Folder Organization

This project is organized into 5 main folders to make it easy for each team member to find what they need.

---

## Folder 1: 01_SETUP
**What it has:** Instructions for getting started

### Files in this folder:
- **TEAM_INSTRUCTIONS.md** - Exactly what each person needs to do. Start here.
- **COMPLETION_CHECKLIST.txt** - Step-by-step checklist. Check off tasks as you complete them.

### When to use:
- First day of project: Read TEAM_INSTRUCTIONS.md
- During project: Check COMPLETION_CHECKLIST.txt to know what to do next
- Need help: Check if your task is in the checklist

---

## Folder 2: 02_CODE
**What it has:** The actual program code

### Files in this folder:
- **payroll.py** - The main program. Everyone edits this file.

### How it works:
- Each person edits only their section (marked with their name)
- Allen edits `get_employee_data()`
- Alexander edits `get_pay_rate()` and `calculate_payroll()`
- Armando edits `save_and_display_results()` and `write_results_to_file()`
- Aniya edits `run_tests()`

### When to use:
- Daily: Open this file and edit your functions
- Before submitting: Make sure your code has comments
- Testing: Run `python3 payroll.py` from this folder

---

## Folder 3: 03_DOCUMENTATION
**What it has:** Plans and explanations

### Files in this folder:
- **PROJECT_PLAN.txt** - Who is doing what
- **SECURITY_EXPLANATION.txt** - How we prevent bad data (Allen writes this)
- **GRADING_RUBRIC.txt** - How the project will be graded

### How it works:
- PROJECT_PLAN.txt documents each person's work
- SECURITY_EXPLANATION.txt explains each security check
- GRADING_RUBRIC.txt shows how many points each section is worth

### When to use:
- Start of project: Read PROJECT_PLAN.txt to understand roles
- Understanding security: Read SECURITY_EXPLANATION.txt
- Before submitting: Check GRADING_RUBRIC.txt to make sure you hit all requirements

---

## Folder 4: 04_TESTING
**What it has:** Test cases and results

### Files in this folder:
- **TEST_RESULTS.txt** - All 10 test cases documented

### How it works:
- Aniya creates 10 test cases
- Each test has: expected output, actual output, pass/fail
- Shows proof that the program works correctly

### When to use:
- After program is done: Aniya fills in this file
- During testing: Everyone helps run tests

---

## Folder 5: 05_SUBMISSION
**What it has:** Files ready to turn in

### What goes here:
- Copy of payroll.py
- results.csv (example output)
- test_results.txt
- All documentation

### When to use:
- End of project: Copy everything here before submitting

---

## Main Folder (Root)
**What it has:** Overview and entry points

### Files:
- **README.md** - Quick overview and links to everything
- **main.txt** - Original assignment (for reference)
- **Todo.md** - Original todo list (for reference)

### When to use:
- First time: Read README.md for quick start
- Confused: Check README.md for folder descriptions

---

## File Organization at a Glance

```
Group-Project-Assignment-Ivy-Tech---Payroll/
├── README.md                          (START HERE)
├── main.txt                           (Original instructions - reference)
├── Todo.md                            (Original todo list - reference)
│
├── 01_SETUP/
│   ├── TEAM_INSTRUCTIONS.md           (What each person does)
│   └── COMPLETION_CHECKLIST.txt       (Task checklist)
│
├── 02_CODE/
│   └── payroll.py                     (Main program - everyone edits)
│
├── 03_DOCUMENTATION/
│   ├── PROJECT_PLAN.txt               (Who did what)
│   ├── SECURITY_EXPLANATION.txt       (Security checks)
│   └── GRADING_RUBRIC.txt             (Scoring)
│
├── 04_TESTING/
│   └── TEST_RESULTS.txt               (10 test cases)
│
└── 05_SUBMISSION/
    └── (Files to turn in go here)
```

---

## How to Use This Organization

### For Allen (Input & Validation):
1. Read: 01_SETUP/TEAM_INSTRUCTIONS.md
2. Edit: 02_CODE/payroll.py (function get_employee_data)
3. Write: 03_DOCUMENTATION/SECURITY_EXPLANATION.txt
4. Check: 01_SETUP/COMPLETION_CHECKLIST.txt

### For Alexander (Payroll Calculations):
1. Read: 01_SETUP/TEAM_INSTRUCTIONS.md
2. Edit: 02_CODE/payroll.py (functions get_pay_rate, calculate_payroll)
3. Test: Your calculations with sample data
4. Check: 01_SETUP/COMPLETION_CHECKLIST.txt

### For Armando (Output & File):
1. Read: 01_SETUP/TEAM_INSTRUCTIONS.md
2. Edit: 02_CODE/payroll.py (functions save_and_display_results, write_results_to_file)
3. Test: That results.csv is created and readable
4. Check: 01_SETUP/COMPLETION_CHECKLIST.txt

### For Aniya (Testing & QA):
1. Read: 01_SETUP/TEAM_INSTRUCTIONS.md
2. Fill in: 04_TESTING/TEST_RESULTS.txt (all 10 test cases)
3. Edit: 02_CODE/payroll.py (function run_tests)
4. Check: 01_SETUP/COMPLETION_CHECKLIST.txt

---

## Finding Things

**If you need to know:** What to do next
→ Check 01_SETUP/COMPLETION_CHECKLIST.txt

**If you need to know:** How to grade your work
→ Check 03_DOCUMENTATION/GRADING_RUBRIC.txt

**If you need to know:** How security works
→ Check 03_DOCUMENTATION/SECURITY_EXPLANATION.txt

**If you need to know:** What each person is doing
→ Check 03_DOCUMENTATION/PROJECT_PLAN.txt

**If you need to code:** Your part of the program
→ Edit 02_CODE/payroll.py

**If you need to test:** Your code works
→ Fill in 04_TESTING/TEST_RESULTS.txt

---

## Quick Start

1. Open README.md
2. Read 01_SETUP/TEAM_INSTRUCTIONS.md
3. Open 02_CODE/payroll.py
4. Find your name and function
5. Edit that function
6. Test your work
7. Check COMPLETION_CHECKLIST.txt
8. Repeat until all tasks are done
