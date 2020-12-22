# %%
import numpy as np
# %%
with open("input.txt", "r") as f:
    data = f.readlines()
data = [int(x) for x in data]
data.append(0)
data.sort()
l1 = data.copy()
data.append(data[-1]+3)
l2 = data.copy()
l2.pop(0)

# %%
l1 = np.array(l1)
l2 = np.array(l2)
diff = l2-l1
# diff = np.append(diff,3)
# %%
ones = []
index = 0
counter = 0 
for x in diff:
    if x == 1:
        counter +=1
    if x == 3:
        ones.append(counter)
        counter = 0 
        index +=1
ones
# %%
values,counts = np.unique(np.array(ones),return_counts=True)
# %%
counts
# %%
2**counts[2]*4**counts[3]*7**counts[4]
# %%
