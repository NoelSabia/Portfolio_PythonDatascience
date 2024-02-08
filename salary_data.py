import pandas as pd
import matplotlib.pyplot as plt

#Class for Salary Data
class Salary_Data:
	#init function reading in the csv file and handling the input. Moreover triggering the right function.
	def __init__(self):
		self.data = pd.read_csv("csv_files/Salary_Data.csv")
		self.choose()

	def choose(self):
		while True:
			try:
				self.num = int(input("(1) Age vs. Years of Experience vs. Salary\n(2) Education Level vs. Gender vs. Salary\n(0)Exit\nChoose: "))
				if self.num in [0,1, 2]:
					break
				else:
					print("Please only valid input.\n")
			except ValueError:
				print("Please only valid input.\n")

		if self.num == 0:
			exit(0)
		elif self.num == 1:
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
			self.choose()
		except Exception as e:
			print(f"An error occurred: {e}")

	def show_chart2(self):
		try:
			df = self.data

			self.choose()
		except Exception as e:
			print(f"An error occurred: {e}")
