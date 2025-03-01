def is_year_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True
	    
def days_in_month(year, month):
    dicti = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    bisies = is_year_leap(year)
    if bisies and month == 2:
        return 29

    else:
        q = dicti[month]
        return q
    
def day_of_year(year, month, day):
        
        dicti = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if is_year_leap(year):
                dicti[2] = 29
                
        complet_index = month
        sumar = 0
        for i in range(1, complet_index):
                sumar += dicti[i]
                      
        remanente = day

        total = sumar + remanente
        return total
    
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

print(day_of_year(2000, 12, 31))
