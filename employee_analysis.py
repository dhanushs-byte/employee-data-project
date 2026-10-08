import pandas as pd
import matplotlib.pyplot as plt


# Load CSV file
df = pd.read_csv("employees.csv")

# Display employee data
print("Employee Data:")
print(df)

# Calculate average salary
average_salary = df["salary"].mean()

# Find highest salary
highest_salary = df["salary"].max()

# Find employee with highest salary
highest_paid_employee = df.loc[df["salary"].idxmax(), "name"]

# Display results
print("\nEmployee Analysis")
print("-----------------")

print(f"Average Salary: ₹{average_salary:.2f}")
print(f"Highest Salary: ₹{highest_salary}")
print(f"Highest Paid Employee: {highest_paid_employee}")


# Create salary chart
plt.figure(figsize=(10, 5))

plt.bar(df["name"], df["salary"])

plt.title("Employee Salary Chart")
plt.xlabel("Employee")
plt.ylabel("Salary (₹)")

plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig("salary_chart.png")

# Display chart
plt.show()