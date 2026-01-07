## PHASE 1: Pandas Basics & Data Structures (Foundation)

### 1. Introduction to Pandas

* What is Pandas?
* Why Pandas is used in Data Analysis
* Pandas vs Excel
* CSV vs Excel file differences
* Series (1‑D labeled array)
* DataFrame (2‑D labeled data structure)

```python
import pandas as pd
```

---

## PHASE 2: Reading Data from Different Sources

### 2. Reading CSV Files

* `read_csv()`
* `names`
* `skiprows`
* `usecols`
* `nrows`
* `parse_dates`
* Reading CSV from URL

```python
pd.read_csv('data.csv')
pd.read_csv('data.csv', names=['no','student','course'])
pd.read_csv('data.csv', skiprows=[0])
pd.read_csv('data.csv', usecols=['sno','Name'])
pd.read_csv('data.csv', nrows=3)
pd.read_csv(url)
```

---

### 3. Reading Excel Files

* `read_excel()`
* Reading single sheet
* Reading multiple sheets using `sheet_name`

```python
pd.read_excel('data.xlsx', sheet_name=0)
pd.read_excel('data.xlsx', sheet_name=1)
```

---

## PHASE 3: Combining & Reshaping Data

### 4. Concatenation (Stacking Data)

* `pd.concat()`
* Combining multiple DataFrames vertically

```python
pd.concat([df1, df2])
```

---

### 5. Merging & Joining Data (Project Critical)

* `merge()`
* `inner`, `left`, `right`, `outer` joins
* Alternative to Excel VLOOKUP

```python
pd.merge(df1, df2, on='id', how='left')
```

---

## PHASE 4: Exploring & Understanding Data

### 6. Data Inspection

* `head()`
* `tail()`
* `shape`
* `info()`
* `describe()`

```python
df.head()
df.info()
df.describe()
```

---

### 7. Sorting & Ranking

* `sort_values()`
* Ascending / descending order
* Ranking data

```python
df.sort_values('sno', ascending=False)
df['rank'] = df['marks'].rank(ascending=False)
```

---

## PHASE 5: Data Cleaning (Most Important Phase)

### 8. Handling Missing Values

* `isna()`
* `sum()`
* `dropna()`
* `fillna()`

```python
df.isna().sum()
df.fillna(0)
df.dropna()
```

---

### 9. Handling Duplicate Data

* `duplicated()`
* `drop_duplicates()`

```python
df.drop_duplicates()
```

---

### 10. Renaming & Reformatting Columns

* `rename()`
* Standardizing column names

```python
df.rename(columns={'Name':'student_name'})
```

---

## PHASE 6: Data Selection & Filtering

### 11. Column Selection

```python
df['sno']
df[['sno','Name']]
```

---

### 12. Conditional Filtering

* Single condition
* Multiple conditions

```python
df[df['marks'] > 60]
df[(df['marks'] > 60) & (df['course'] == 'Python')]
```

---

## PHASE 7: Column Creation & Transformation

### 13. Creating New Columns

```python
df['total'] = df['maths'] + df['science']
```

---

### 14. Applying Conditions

* `apply()`
* `lambda` functions

```python
df['status'] = df['total'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
```

---

## PHASE 8: Grouping & Aggregation (Core Project Skill)

### 15. GroupBy Operations

* Mean, sum, count
* Multiple aggregations

```python
df.groupby('course')['marks'].mean()

df.groupby('course').agg({
    'marks':'mean',
    'student':'count'
})
```

---

## PHASE 9: Datetime Operations

### 16. Date & Time Handling

* `to_datetime()`
* Extract year, month, day
* Day name

```python
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_name'] = df['date'].dt.day_name()
```

---

## PHASE 10: String Operations (Text Cleaning)

### 17. String Methods

* `upper()`
* `lower()`
* `contains()`
* `replace()`

```python
df['Name'].str.upper()
df['Name'].str.replace(' ','_')
```

---

## PHASE 11: Index Management

### 18. Indexing

* `set_index()`
* `reset_index()`

```python
df.set_index('sno')
df.reset_index()
```

---

## PHASE 12: Statistical Operations

### 19. Statistical Functions

* `mean()`
* `count()`
* `max()`
* `min()`

```python
df['marks'].mean()
df['marks'].count()
df['marks'].max()
```

---

## PHASE 13: Exporting Data (Final Output)

### 20. Exporting to Files

* Export to Excel
* Export to CSV
* Remove index

```python
df.to_excel('final_report.xlsx', index=False)
df.to_csv('final_report.csv', index=False)
```

---

## PHASE 14: Basic Visualization (Optional but Valuable)

### 21. Simple Plots

* Bar chart
* Line chart

```python
df.groupby('course')['marks'].mean().plot(kind='bar')
```

---
