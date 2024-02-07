from sklearn.preprocessing import LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

class Salary_Data:
	def __init__(self):
		self.data = pd.read_csv("csv_files/Salary_Data.csv")
		while True:
			try:
				self.num = int(input("(1) Age vs. Years of Experience vs. Salary\n(2) Education Level vs. Gender vs. Salary\nChoose: "))
				if self.num in [1, 2]:
					break
				else:
					print("Please only valid input.\n")
			except ValueError:
				print("Please only valid input.\n")

		if self.num == 1:
			self.show_chart1()
		elif self.num == 2:
			self.show_chart2()
		
	def show_chart1(self):
		try:
			fig = plt.figure()
			td = fig.add_subplot(111, projection="3d")
			x_axis = self.data['Age']
			y_axis = self.data['Years of Experience']
			z_axis = self.data['Salary']
			td.scatter(x_axis, y_axis, z_axis)
			td.set_xlabel('Age')
			td.set_ylabel('Years of Experience')
			td.set_zlabel('Salary')
			plt.show()
		except Exception as e:
			print(f"An error occurred: {e}")

	def show_chart2(self):
		try:
			fig = plt.figure()
			td = fig.add_subplot(111, projection='3d')
			le = LabelEncoder()
			self.data['Education Level'] = le.fit_transform(self.data['Education Level'])
			self.data['Gender'] = le.fit_transform(self.data['Gender'])
			x = np.linspace(min(self.data['Education Level']), max(self.data['Education Level']), num=100)
			y = np.linspace(min(self.data['Gender']), max(self.data['Gender']), num=100)
			x, y = np.meshgrid(x, y)
			z = self.calculate_z_values(x, y)
			td.plot_surface(x, y, z, cmap='viridis')
			td.set_xlabel('Education Level')
			td.set_ylabel('Gender')
			td.set_zlabel('Salary')
			plt.show()
		except Exception as e:
			print(f"An error occurred: {e}")

	def calculate_z_values(self, x, y):
		return x * y