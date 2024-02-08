import matplotlib.ticker as ticker
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



class Car_Sales:
	def __init__(self):
		self.data = pd.read_csv('csv_files/Car Sales.xlsx - car_data.csv')
		while True:
			try:
				num = int(input("Choose between:\n(1)Gender vs. Transmission\n(2)Annual Income vs. Price\n(3)Trend for selling Cars\nChoose: "))
				if num in [1, 2, 3]:
					break
				else:
					print("Please only valid input.")
			except ValueError:
				print("Please only valid input.")

		if num == 1:
			self.gender_vs_transmission()
		elif num == 2:
			self.income_vs_price()
		elif num == 3:
			self.car_selling_trend()

	def gender_vs_transmission(self):
		df = self.data
		female_count = df[df['Gender'] == 'Female'].shape[0]
		male_count = df[df['Gender'] == 'Male'].shape[0]
		sns.displot(df, x='Gender', hue='Transmission', multiple='stack')
		plt.show()

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

	def car_selling_trend(self):
		pass
