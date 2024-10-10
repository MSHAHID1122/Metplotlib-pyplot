import matplotlib.pyplot as plt

# Data
departments = ['CS', 'IT', 'EE', 'ME']
students = [150, 120, 100, 80]

# 1. Create a bar chart
plt.figure(figsize=(10, 5))  # Set the figure size

plt.subplot(1, 2, 1)  # Create first subplot for the bar chart
plt.bar(departments, students, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Departments')
plt.ylabel('Number of Students')
plt.title('Department-wise Enrollment')

# 2. Create a pie chart
plt.subplot(1, 2, 2)  # Create second subplot for the pie chart
plt.pie(students, labels=departments, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'purple'])
plt.title('Enrollment Distribution by Department')

# Display the charts
plt.tight_layout()
plt.show()