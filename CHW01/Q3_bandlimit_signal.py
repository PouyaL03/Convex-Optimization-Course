from cvxpy import *
from zero_crossings_data import *
import matplotlib.pyplot as plt

C = np.zeros((n, B))
S = np.zeros((n, B))
range_n = np.arange(1, n + 1)
for j in range(B):
    C[:, j] = np.cos(2 * np.pi * (f_min + j) * range_n / n)
    S[:, j] = np.sin(2 * np.pi * (f_min + j) * range_n / n)

A = np.hstack((C, S))
x = Variable(2 * B)
objective = Minimize(norm(A @ x))
constraints = [multiply(s, A @ x) >= 0, s.T @ (A @ x) == n]

prob = Problem(objective, constraints)
result = prob.solve()

y_hat = A @ x.value
print(f"Recovery: {np.linalg.norm(y - y_hat) / np.linalg.norm(y_hat)}")

fig = plt.figure()
plt.plot(range_n, y, label='original')
plt.plot(range_n, y_hat, label='recorvered')
plt.legend()
plt.show()
fig.savefig('Q3.png')
# constraints += [elementwise(s, A * x)]