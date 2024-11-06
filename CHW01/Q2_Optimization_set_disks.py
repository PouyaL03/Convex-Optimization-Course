from cvxpy import *
from disks_data import *

C = Variable((n,2))
R = Variable(n)
objective = Minimize(sum_squares(R))
constraints = []
constraints += [R >= 0]
constraints += [C[:k,:] == Cgiven]
constraints += [R[:k] == Rgiven]
print(len(Gindexes))
for i in range(len(Gindexes)):
    constraints += [norm(C[Gindexes[i][0]] - C[Gindexes[i][1]]) <= R[Gindexes[i][0]] + R[Gindexes[i][1]]]
    
prob = Problem(objective, constraints)
result = prob.solve()

plot_disks(R=R.value, C=C.value, Gedges=Gindexes, name='area.png')

objective = Minimize(sum(R))
    
prob = Problem(objective, constraints)
result = prob.solve()

plot_disks(R=R.value, C=C.value, Gedges=Gindexes, name='perimeter.png')