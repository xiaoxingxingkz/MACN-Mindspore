from scipy import stats
import numpy as np
import scipy.stats

request_c = []
f = open("D:\\Connection\\Superiortemporal_real\\ad.txt", "r")
for line in f.readlines():
    line = line.strip('\n')
    request_c.append(np.float(line))
    # print(line)
f.close()
a = np.array(request_c)


request_e = []
f = open("D:\\Connection\\Superiortemporal_real\\cn.txt", "r")
for line in f.readlines():
    line = line.strip('\n')
    request_e.append(np.float(line))
    # print(line)
f.close()
b = np.array(request_e)


request_c = np.array([30, 152, 267, 369, 478, 1, 333])
request_e = np.array([30, 152, 277, 383, 497])

t, pval = scipy.stats.ttest_ind(request_c, request_e)

print(t,pval)
