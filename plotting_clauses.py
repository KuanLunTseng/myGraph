import matplotlib.pyplot as plt 

f = open('output.txt', 'r')

k = []
clause = []
for i in f:
    detail = i.split(',')
    clause.append(int(detail[3][:-1]))
    k.append(int(detail[0]))
    
    

    
x = k
y1 = clause

f.close()

plt.plot(x, y1, label = "#clause")
plt.xlabel('Number of vertices')
plt.ylabel('Number of clauses')
plt.title('Number of clauses to construct the clique problem in SAT solver')
plt.legend()
plt.show() 
