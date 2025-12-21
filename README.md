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
- All code has comments explaining what it does
