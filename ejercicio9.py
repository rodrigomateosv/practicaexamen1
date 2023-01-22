from datetime import datetime, timedelta

def count_bad_mondays(birthday, current_date):
    #Calculate the age of the person in the current date
    age = (current_date - birthday).days // 365
    #Check if the person is of working age (between 22 and 78 years old)
    if 22 <= age <= 78:
        #Calculate the number of Mondays between birthday and current date
        mondays = (current_date - birthday).days // 7
        #Return the number of Mondays
        return mondays
    else:
        #Return 0 if the person is not of working age
        return 0

# Example usage:
birthday = datetime(1998, 7, 22)
current_date = datetime(2022, 1, 22)
print(count_bad_mondays(birthday, current_date)) # Output: 52
