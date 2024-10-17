Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class SimpleLinearRegression:
...     def __init__(self, lr=0.01, iterations=1000):
...         self.lr = lr  
...         self.iterations = iterations 
...         self.slope = 0 
...         self.intercept = 0 
... 
...     def train(self, X, Y):
...         n = len(X)  
...         for _ in range(self.iterations):
...             d_slope = 0 
...             d_intercept = 0  
...             for i in range(n):
...                 prediction = self.slope * X[i] + self.intercept 
...                 d_slope += -2 * X[i] * (Y[i] - prediction)
...                 d_intercept += -2 * (Y[i] - prediction)
... 
...             self.slope -= (d_slope / n) * self.lr
...             self.intercept -= (d_intercept / n) * self.lr
... 
... 
...     def predict(self, X):
...         return [self.slope * x + self.intercept for x in X]
... 
... 
... def input_data():
...     num_employees = int(input("Enter the number of employees you want to input data for: ")) 
...     experience_data = []
...     salary_data = []
...     print("Now, please enter the years of experience and respective salary:")
... 
...     for i in range(num_employees):
...         years = float(input(f"Experience (in years) for Employee {i + 1}: "))
...         salary = float(input(f"Salary for Employee {i + 1} (in Rs.): "))
...         experience_data.append(years)
...         salary_data.append(salary)

    return experience_data, salary_data

if __name__ == "__main__":

    X, Y = input_data()


    model = SimpleLinearRegression(lr=0.01, iterations=1000)
    model.train(X, Y)

    predicted_salaries = model.predict(X)
    print("Here are the predicted salaries based on the data you provided:", predicted_salaries)

    new_exp = float(input("Enter the number of years of experience to predict the salary for: "))
    new_salary_prediction = model.predict([new_exp])
    print(f"The estimated salary for {new_exp} years of experience is: Rs. {new_salary_prediction[0]:.2f}")
