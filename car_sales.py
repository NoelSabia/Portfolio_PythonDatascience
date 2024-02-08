import matplotlib.ticker as ticker
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Class for "Car Sales"
class Car_Sales:
	#init function reading in the csv file and handling the input. Moreover triggering the right function.
	def __init__(self):
		self.data = pd.read_csv('csv_files/Car Sales.xlsx - car_data.csv')
		self.choose_car()

	def choose_car(self):
		while True:
			try:
				num = int(input("Choose between:\n(1)Gender vs. Transmission\n(2)Annual Income vs. Price\n(3)Trend for selling Cars\n(0)Exit\nChoose: "))
				if num in [0, 1, 2, 3]:
					break
				else:
					print("Please only valid input.")
			except ValueError:
				print("Please only valid input.")

		if num == 0:
			exit(0)
		elif num == 1:
			self.gender_vs_transmission()
		elif num == 2:
			self.income_vs_price()
		elif num == 3:
			self.car_selling_trend()

	def gender_vs_transmission(self):
		df = self.data
		sns.displot(df, x='Gender', hue='Transmission', multiple='stack')
		plt.show()
		self.choose_car()

	def income_vs_price(self):
		df = self.data
		income = df['Annual Income']
		price = df['Price ($)']

		fig, ax = plt.subplots()
		ax.bar(income, price, width=1, edgecolor="black")
		ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
		plt.xlabel('Income')
		plt.ylabel('Price in Dollar')
		plt.show()
		self.choose_car()

	def car_selling_trend(self):
		df = self.data
		df['Date'] = pd.to_datetime(df['Date'])
		df['Quarter'] = df['Date'].dt.to_period("Q")
		sold = df['Quarter'].value_counts().sort_index()
		ax = plt.subplot()
		ax.plot(sold.index.astype(str), sold.values)
		plt.xlabel("Quarters")
		plt.ylabel("Sold Cars")
		plt.xticks(rotation=45)
		plt.show()
		self.choose_car()
