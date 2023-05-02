from datetime import date

current_date = date(2023,1,1)


feb_2020 = date(2020, 1, 1)
current_year = current_date.year
if current_date.month<2:
    current_year-=1
    
current_feb = date(current_year,2,1)


# Calculate the difference between the current month and February 2020
month_diff_current = (current_date.year - feb_2020.year) * 12 + (current_date.month - feb_2020.month)+1
month_diff_feb = (current_feb.year - feb_2020.year) * 12 + (current_feb.month - feb_2020.month)

output =[i for i in range(month_diff_current,month_diff_feb,-1)]
print(output)



