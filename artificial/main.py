import numpy as np
import matplotlib.pyplot as plt
print("Welcome to Ai Labs")

x_train = np.array([1,2,3,4,5,6,7])
y_train = np.array([10,20,30,40,50,60,70])
print(f"X train : {x_train}")
print(f"Y train is : {y_train}")

# to find the m (number of training example)
print(len(x_train))
# or
print(x_train.shape[0])
m = x_train.shape[0]
f_wb = np.zeros(m)
# w = 100 , b =100
for i in range(0,7):
    f_wb[i] = 10 * x_train[i] + 0


print("The out is :" , f_wb)
# to plot above training data in  chart
# Plot the data points
plt.plot(x_train, f_wb, c='b',label='Our Prediction')
plt.scatter(x_train,y_train,marker="x", c="r")
plt.xlabel("Age of person")
plt.ylabel("Test result")
plt.title("Sachin's first data")
plt.show()



