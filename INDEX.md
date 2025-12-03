# Project Index - Quick Navigation

## STEP 1: START HERE
Read this first to understand the project structure:
- **README.md** - Overview with quick links
- **STRUCTURE_EXPLAINED.md** - How folders are organized

---

## STEP 2: GET INSTRUCTIONS
Learn exactly what you need to do:
- **01_SETUP/TEAM_INSTRUCTIONS.md** - Your specific tasks based on your role
- **01_SETUP/COMPLETION_CHECKLIST.txt** - Check off tasks as you complete them

---

## STEP 3: UNDERSTAND GRADING
Know what you're being graded on:
- **03_DOCUMENTATION/GRADING_RUBRIC.txt** - Point breakdown for each section

---

## STEP 4: CODE YOUR SECTION
Edit your code in the main program:
- **02_CODE/payroll.py** - Main program (only edit your section)

### Find your role:
- **Allen**: Edit `get_employee_data()` function
- **Alexander**: Edit `get_pay_rate()` and `calculate_payroll()` functions
- **Armando**: Edit `save_and_display_results()` and `write_results_to_file()` functions
- **Aniya**: Edit `run_tests()` function

---

## STEP 5: TEST YOUR CODE
Run the program and verify it works:
```bash
python3 02_CODE/payroll.py
```

---

## STEP 6: DOCUMENT YOUR TESTS
Fill in test results and get evidence your code works:
- **04_TESTING/TEST_RESULTS.txt** - Document all 10 test cases

---

## STEP 7: UNDERSTAND YOUR WORK
Read about what each person did:
- **03_DOCUMENTATION/PROJECT_PLAN.txt** - Team roles and responsibilities

---

## REFERENCE DOCUMENTS

### For Security Understanding:
- **03_DOCUMENTATION/SECURITY_EXPLANATION.txt** - How we prevent bad data

### For Progress Tracking:
- **01_SETUP/COMPLETION_CHECKLIST.txt** - Check your progress

---

## FOLDER PURPOSES

| Folder | Contains | Purpose |
|--------|----------|---------|
| **01_SETUP** | Instructions | What to do and how to track progress |
| **02_CODE** | Program | The actual Python code |
| **03_DOCUMENTATION** | Plans & Explanations | Why things work the way they do |
| **04_TESTING** | Test Results | Evidence that your program works |
| **05_SUBMISSION** | Final Files | Files to turn in (copy here at the end) |

---

## BY ROLE

### Allen Poston (Input & Validation)
1. Read: 01_SETUP/TEAM_INSTRUCTIONS.md
2. Read: 03_DOCUMENTATION/SECURITY_EXPLANATION.txt (you write this)
3. Edit: 02_CODE/payroll.py - `get_employee_data()` function
4. Test: Run `python3 02_CODE/payroll.py` and verify validation works
5. Track: 01_SETUP/COMPLETION_CHECKLIST.txt - PHASE 2

### Alexander Mansfield (Payroll Calculations)
1. Read: 01_SETUP/TEAM_INSTRUCTIONS.md
2. Edit: 02_CODE/payroll.py - `get_pay_rate()` and `calculate_payroll()` functions
3. Test: Verify calculations are correct with sample data
4. Track: 01_SETUP/COMPLETION_CHECKLIST.txt - PHASE 3

### Armando Ochoa (Output & File)
1. Read: 01_SETUP/TEAM_INSTRUCTIONS.md
2. Edit: 02_CODE/payroll.py - `save_and_display_results()` and `write_results_to_file()` functions
3. Test: Verify results display on screen and save to file
4. Track: 01_SETUP/COMPLETION_CHECKLIST.txt - PHASE 4

### Aniya Howell (Testing & QA)
1. Read: 01_SETUP/TEAM_INSTRUCTIONS.md
2. Fill: 04_TESTING/TEST_RESULTS.txt - All 10 test cases
3. Edit: 02_CODE/payroll.py - `run_tests()` function
4. Track: 01_SETUP/COMPLETION_CHECKLIST.txt - PHASE 5

---

## RUNNING THE PROGRAM

After everyone has finished their sections:

```bash
cd 02_CODE
python3 payroll.py
```

Then enter employee data for 10 employees. Results will:
- Print to screen
- Save to `results.csv`

---

## CHECKLIST FOR SUBMISSION

Before submitting, verify ALL of these are done:

### Code (02_CODE/)
- [ ] payroll.py runs without errors
- [ ] All functions have your name and comments
- [ ] Program accepts valid data
- [ ] Program rejects invalid data

### Testing (04_TESTING/)
- [ ] TEST_RESULTS.txt has all 10 test cases
- [ ] Each test case shows: input, expected, actual, pass/fail
- [ ] All tests pass

### Documentation (03_DOCUMENTATION/)
- [ ] PROJECT_PLAN.txt is filled in
- [ ] SECURITY_EXPLANATION.txt is completed (Allen)
- [ ] GRADING_RUBRIC.txt is available

### Deliverables
- [ ] Copy all files to 05_SUBMISSION/ folder
- [ ] Include example results.csv showing actual output
- [ ] Include README explaining how to run
- [ ] All team members names are listed

---

## COMMON QUESTIONS

**Q: Where do I edit my code?**
A: 02_CODE/payroll.py - Find your function and edit only that

**Q: How do I know what to do?**
A: Read 01_SETUP/TEAM_INSTRUCTIONS.md and 01_SETUP/COMPLETION_CHECKLIST.txt

**Q: How do I run the program?**
A: `python3 02_CODE/payroll.py`

**Q: What are the grading points?**
A: Read 03_DOCUMENTATION/GRADING_RUBRIC.txt

**Q: How do I document tests?**
A: Fill in 04_TESTING/TEST_RESULTS.txt with all 10 test cases

**Q: What if I'm stuck?**
A: Ask your team. Check 01_SETUP/COMPLETION_CHECKLIST.txt for your phase.

---

## CONTACTS & ROLES

**Allen Poston** - Input & Validation Lead
- Main file: `get_employee_data()` in 02_CODE/payroll.py
- Documentation: SECURITY_EXPLANATION.txt

**Alexander Mansfield** - Payroll Calculations Lead
- Main files: `get_pay_rate()` and `calculate_payroll()` in 02_CODE/payroll.py

**Armando Ochoa** - Output & File Lead
- Main files: `save_and_display_results()` and `write_results_to_file()` in 02_CODE/payroll.py

**Aniya Howell** - Testing & QA Lead
- Main file: `run_tests()` in 02_CODE/payroll.py
- Documentation: TEST_RESULTS.txt

---

## Last Updated
December 3, 2025
