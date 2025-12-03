# Team PayMasters – Payroll Project

## ✅ Project Overview
This project is a payroll management system for 10 employees.  
Team members are responsible for separate modules:

- **ALLEN POSTON** – Input & Validation
- **ALEXANDER MANSFIELD** – Payroll Calculations
- **ARMANDO OCHOA** – Output & File
- **ANIYA HOWELL** – Testing & QA

---

## 📝 To-Do Checklist

### Step 1 – Plan & Assign
- [x] Confirm team responsibilities
- [x] Project roadmap created (ALLEN POSTON)

---

### Step 2 – Input & Validation Module (ALLEN POSTON)
- [ ] Create `get_employee_data()` function
- [ ] Include prompts:
  - First Name
  - Last Name
  - Employee ID
  - Number of Dependents
  - Hours Worked
- [ ] Add security checks:
  - Reject negative values
  - Reject hours above MAX_HOURS_ALLOWED
  - Flag hours > 40
- [ ] Test input validation
- [ ] Save pseudocode / flowchart

---

### Step 3 – Payroll Calculations (ALEXANDER MANSFIELD)
- [ ] Create `get_pay_rate(empID)` function
- [ ] Create `calculate_payroll(hoursWorked, payRate)` function:
  - Gross pay (up to 40 hours)
  - Overtime pay (1.5x)
  - State tax 5.6%
  - Federal tax 7.9%
  - Net pay
- [ ] Verify unusual hours flagged by ALLEN
- [ ] Prepare pseudocode / flowchart

---

### Step 4 – Output & File Module (ARMANDO OCHOA)
- [ ] Create `save_and_display_results(employeeData, payrollData)`
  - Print formatted output
  - Store in lists/arrays
- [ ] Create `write_results_to_file()` function
  - Save results as CSV or TXT
- [ ] Test output formatting

---

### Step 5 – Testing Module (ANIYA HOWELL)
- [ ] Create at least 10 test cases with fake employee data
- [ ] Test full program flow:
  - Input validation
  - Payroll calculations
  - Output formatting
- [ ] Record test results
- [ ] Document testing procedure

---

### Step 6 – Integration
- [ ] Combine modules: Input → Payroll → Output → File
- [ ] Ensure variable names and structures match
- [ ] Run all test cases to verify integration

---

### Step 7 – Final Documentation & Submission
- [ ] Include project plan & roadmap
- [ ] Include pseudocode / flowchart
- [ ] Include testing results
- [ ] Include security checks explanation
- [ ] Include final combined program
- [ ] Confirm each module is complete and working

---

## ✅ Notes
- Work module by module
- Use fake data for testing first
- Communicate issues promptly to avoid blocking progress
