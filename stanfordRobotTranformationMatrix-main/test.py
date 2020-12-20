from main import stanfordT


uret = stanfordT(
    theta = [0,90, 0, 90,270,0],
    d = [50, 40], # d3 d6
    a2 = [40] # a2
    )

#print()
#print(uret.matrix())
print(uret.pointInPlane([0,0,10], axis = 'global'))