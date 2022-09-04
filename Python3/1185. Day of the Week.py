'''
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
'''

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if not year % 4 and year % 100 or not year % 400:
            months[1] = 29

        for i in range(1972, year):
            if not i % 4 and i % 100 or not i % 400:
                day += 366
            else:
                day += 365

        for i in range(month - 1):
            day += months[i]
            
        return days[day % 7]