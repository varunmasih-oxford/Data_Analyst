# Pandas – Practical Hands-on Questions  

## Dataset Assumption

Assume you have:
- `data.csv`
- `data.xlsx` with **2 sheets**

Columns (example):
- `sno`
- `name`
- `course`
- `marks`
- `city`

---

## Section 1: Reading Data (Hands-on)

### Question 1  
Read the `data.csv` file using Pandas and display the full DataFrame.

---

### Question 2  
Read only the first **5 rows** from `data.csv`.

---

### Question 3  
Read `data.csv` and assign custom column names.

---

### Question 4  
Read only the columns `sno` and `name` from the CSV file.

---

### Question 5  
Read the Excel file `data.xlsx` and load **Sheet 1** into a DataFrame.

---

### Question 6  
Read **both sheets** from `data.xlsx` into two separate DataFrames.

---

---

## Section 2: Combining & Exploring Data

### Question 7  
Combine the two Excel sheet DataFrames into one DataFrame.

---

### Question 8  
Display the **first 3 rows** and **last 3 rows** of the combined DataFrame.

---

### Question 9  
Find the total number of rows and columns in the DataFrame.

---

### Question 10  
Display basic information about the dataset (data types, nulls).

---

---

## Section 3: Sorting & Filtering

### Question 11  
Sort the DataFrame by `sno` in **ascending order**.

---

### Question 12  
Sort the DataFrame by `marks` in **descending order**.

---

### Question 13  
Filter and display only students whose `marks` are greater than 70.

---

### Question 14  
Filter students who belong to a specific `course`.

---

---

## Section 4: Statistics & Analysis

### Question 15  
Find the **average marks** of all students.

---

### Question 16  
Find the **highest** and **lowest** marks.

---

### Question 17  
Count how many students are enrolled in each `course`.

---

### Question 18  
Find how many students belong to each `city`.

---

---

## Section 5: Exporting Data

### Question 19  
Export the statistical summary of the dataset to an Excel file.

---

### Question 20  
Export the filtered data (students with marks > 70) to a CSV file.

---

---

## Section 6: Challenge Questions

### Question 21  
Create a new column called `Result`:
- Marks ≥ 50 → **Pass**
- Marks < 50 → **Fail**

---

### Question 22  
Sort students by `Result` and then by `marks`.

---

### Question 23  
Display only students who have **missing values**, if any.

---

### Question 24  
Replace missing values in `marks` with the **average marks**.

---

---

## Final Task (Mini Project)

### Question 25  
Create a final Excel report that includes:
- Full cleaned data  
- Summary statistics  
- Sorted student list  

Save it as `final_report.xlsx`.

