import matplotlib.pyplot as plt 

f = open('output.txt', 'r')

k = []
brute = []
sat = []
for i in f:
    detail = i.split(',')
    k.append(detail[0])
    brute.append(round(float(detail[1]), 2))
    sat.append(round(float(detail[2]), 2))
    
x = k
y1 = brute
y2 = sat

f.close()

plt.plot(x, y1, label = "Brute-Forse")
plt.plot(x, y2, label = "SAT Solver")
plt.xlabel('Number of vertices')
plt.ylabel('Seconds')
plt.title('Running time of Brute-Forse/SAT Solver')
plt.legend()
plt.show() 