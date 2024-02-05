import pandas as pd
import seaborn
from car_sales import Car_Sales
from salary_data import Salary_Data

# This function is used for Errormanagement
# and to choose which dataset should be used.
def get_init_user_input():
	select = None
	try:
		select = int(input("You can choose between two datasets:\n(1) Salary_Data\n(2) Car Sales\nChoose: "))
		print(select)
		if select not in [1, 2]:
			print("Please only write 1 or 2.\n")
			get_init_user_input()
	except:
		print("Please only write 1 or 2.\n")
		get_init_user_input()
	return select

# This function coordinates everything.
def	main():
	num = get_init_user_input()
	if num == 1:
		salary_data = Salary_Data()
	else:
		car_sales = Car_Sales()


main()