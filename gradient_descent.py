import numpy as np

def gradient_descent (x,y):
    m_curr = b_curr = 0 #initial values and then we will take small steps to reach the desired values
    iterations = 10000 #always declare, here started with 1000 and theb it will be fine-tuned
    n = len(x) #length of data points
    learning_rate = 0.08

    for i in range (iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val ** 2 for val in (y-y_predicted)])
        md = -(2/n) * sum(x * (y - y_predicted))
        bd = -(2/n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, cost {}, iteration {}".format(m_curr,b_curr,cost,i))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)