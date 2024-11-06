from cvxpy import *
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

T = 24
N = np.array([0, 4, 2, 2, 3, 0, 4, 5, 6, 6, 4, 1, 4, 4, 0, 1, 3, 4, 2, 0, 3, 2, 0, 1])

lambda_ = Variable(T, nonneg=True)
rho = Parameter(nonneg = True)

objective = Minimize(sum(lambda_) - N @ log(lambda_) + rho * (lambda_[0] - lambda_[23])**2 + rho * sum_squares(diff(lambda_)))

rho_values = [0.1, 1, 10, 100]
lambda_values = []
prob = Problem(objective)

fig = plt.figure()
for value in rho_values:
    rho.value = value
    result = prob.solve()
    plt.plot(np.arange(T), lambda_.value, label=f"rho={value}")
    lambda_values.append(lambda_.value)
plt.legend()
plt.show()

fig.savefig('Q4.png')
N_test = [0, 1, 3, 2, 3, 1, 4, 5, 3, 1, 4, 3, 5, 5, 2, 1, 1, 1, 2, 0, 1, 2, 1, 0]
for value, lambda_ in zip(rho_values, lambda_values):
    log_likelihood = np.sum(np.log(np.exp(-lambda_) * lambda_**N_test / sp.special.factorial(N_test)))
    print(f"rho = {value}, log likelihood = {log_likelihood}")