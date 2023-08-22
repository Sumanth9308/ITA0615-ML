import math as m

result = [[9.2,85,8,"pass"],
          [8,80,7,"pass"],
          [8.5,81,8,"pass"],
          [6,45,5,"fail"],
          [6.5,50,4,"fail"],
          [8.2,72,7,"pass"],
          [5.8,38,5,"fail"],
          [8.9,91,9,"pass"]]

g = [7.6,60,8]
k = int(input("Enter K : "))

no_attr = len(result[0]) - 1
distance = []

for i in range(0,len(result)):
    x = 0
    for j in range(0,no_attr):
        x = x + m.pow(g[j]- result[i][j], 2)
    #we append the distances of every instance on the main list(result) to use it in future
    result[i].append(m.sqrt(x))
    distance.append(m.sqrt(x))
# we sort the distance list to find the nearest k distances
distance.sort()

NN = []

pass_ = 0
fail_ = 0

for i in range(0,k):
    NN.append(distance[i])

for j in range(0,k):
    for i in range(0,len(result)):
        if(result[i][len(result[0]) - 1] == NN[j]):
            if(result[i][len(result[0]) - 2] == "pass"):
                pass_ = pass_ + 1
            else:
                fail_ = fail_ + 1

print("Nearest Neighbours (distances): " + str(NN))

if(pass_ > fail_ ):
    print("Outcome : Pass")
else:
    print("Outcome : Fail")
