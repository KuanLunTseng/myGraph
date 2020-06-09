import matplotlib.pyplot as plt 

f = open('mprofile_20200608212230.dat', 'r')

mem = []
k = []
for i, d in enumerate(f):
    detail = d.split(' ')
    #if i > 100:
    #    break
    if detail[0] == 'MEM':
        mem.append(round(float(detail[1]), 2))
        
        k.append(i)
'''
print(k)
print(brute)
print(sat)
'''
x = k
y1 = mem


print(x)
print(y1)



plt.plot(x, y1, label = "Mem-usage")
plt.xlabel('time')
plt.ylabel('MB')
plt.title('Memory usage over time in construting SAT Solver')
plt.legend()
plt.show() 
f.close()
