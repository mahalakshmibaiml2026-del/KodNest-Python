import copy
original = [[1,2],[3,4]]
s_copy = copy.copy(original)
original[1][0] = 30
print(original)
print(s_copy)

import copy
original = [[1,2],[3,4]]
d_copy = copy.deepcopy(original)
original[0][0] = 100
print(original)
print(d_copy)