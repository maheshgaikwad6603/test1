def max_sum_subsequence(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# Test the code with the original list [1, 2, 3]
original_list = [1, 2, 3]
max_sum = max_sum_subsequence(original_list)
print("Original list:", original_list)
print("Maximum sum subsequence of the list:", max_sum)


def max_sum_subsequence(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


original_list = [1, 2, 4, 3, 5, 4, 6, 9, 2, -10]
max_sum = max_sum_subsequence(original_list)
print("Original list:", original_list)
print("Maximum sum subsequence of the list:", max_sum)


def max_sum_subsequence(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


original_list = [1, 2, -4, 3, 5, 4, 6, 9, 2, -10]
max_sum = max_sum_subsequence(original_list)
print("Original list:", original_list)
print("Maximum sum subsequence of the list:", max_sum)


def max_sum_subsequence(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


original_list = [1, 2, 4, 3, 5, -24, 6, 9, -2]
max_sum = max_sum_subsequence(original_list)
print("Original list:", original_list)
print("Maximum sum subsequence of the list:", max_sum)

import pandas as pd

# Define the URL of the CSV file
url = "https://raw.githubusercontent.com/sharajman/sample-data/main/03-18-2020.csv"

# Read the CSV file into a DataFrame
data = pd.read_csv(url)

# Sort the data based on the number of confirmed cases in descending order
sorted_data = data.sort_values(by="Confirmed", ascending=False)

# Get the top 10 countries' data
top_10_countries = sorted_data.head(10)

# Print the data for each country
for index, country_data in top_10_countries.iterrows():
    last_update = country_data["Last Update"]
    country = country_data["Country/Region"]
    confirmed = country_data["Confirmed"]
    deaths = country_data["Deaths"]
    recovered = country_data["Recovered"]

    print("Last Update:", last_update)
    print("Country/Region:", country)
    print("Confirmed Cases:", confirmed)
    print("Deaths:", deaths)
    print("Recovered Cases:", recovered)
    print("-------------------------")



import pandas as pd

# Define the URL of the data file
url = "https://raw.githubusercontent.com/sharajman/sample-data/main/tbl_employee.sq"

# Read the data file into a DataFrame
data = pd.read_csv(url, delimiter="\t")

# Select the columns emp_name (first_name, last_name), email_id, and manager_name (first_name, last_name)
employee_data = data[["first_name", "last_name", "email_id", "manager_first_name", "manager_last_name"]]

# Rename the columns for better readability
employee_data.columns = ["Employee Name", "Email ID", "Manager Name"]

# Sort the data by employee name
sorted_data = employee_data.sort_values(by="Employee Name")

# Display the sorted data
print(sorted_data)


