# %%

with open("input.txt", "r") as f:
    data = f.readlines()
data = [int(x) for x in data]
data.append(0)
data.sort()
# %%
l1 = data.copy()
data.append(data[-1]+3)
l2 = data.copy()
l2.pop(0)

# %%
import numpy as np
# %%
l1 = np.array(l1)
l2 = np.array(l2)
values, counts = np.unique((l2-l1), return_counts=True)
counts[0]*counts[1]
# %%
