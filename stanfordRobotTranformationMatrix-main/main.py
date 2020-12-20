import numpy as np



class stanfordT:
    def __init__(self, **kwargs):
        self.theta = kwargs['theta']
        self.d = kwargs['d']
        self.a2 = kwargs['a2']
    
    def splitup(self, degrees):
        total2 = 0
        #arr = len(degrees)
        for j in range(len(degrees)): # 3
            deg = list(degrees[j]) # - s 5 c 1 s 2 c 4
            if deg[0] != "-":   
                total2 += self.calculate(deg)
                
            elif deg[0] == "-":
                total2 -= self.calculate(deg)
                #print(total2)
            else:
                print("var bi sikinti") 

        return total2

    def matrix(self):
        
        r11 = self.splitup(
            [
                "c6c5c1s2c4", 
                "c6c5s1s4", 
                "c6c1c2c5", 
                "-s6c1s2s4", 
                "s6s1c4"
            ]
        )
        r12 = self.splitup(
            [
                "-s6c5c1s2c4",
                "-s6c5s1s4",
                "-s6c1c2s5",
                "-c6c1s2s4",
                "c6s1c4"
            ]
        )
        r13 = self.splitup(
            [
                "-s5c1s2c4",
                "-s4s1s4",
                "c1c2c5"
            ]
        )
        r14 = self.splitup(
            [
                "-d6s5c1s2c4",
                "-d6s5s1s4",
                "d6c1c2c5",
                "c1c2d3",
                "s1a2"
            ]
        )
        r21 = self.splitup(
            [
                "c6c5s1s2c4",
                "-c6c5c1s4",
                "c6s1c2s5",
                "-s6s1s2s4",
                "-s6c1c4"
            ]
        )
        r22 = self.splitup(
            [
                "-s6c5s1s2c4",
                "s6c5c1s4",
                "-s6s1c2s5",
                "-c6s1s2s4",
                "-c6c1c4"
            ]
        )
        r23 = self.splitup(
            [
                "-s5s1s2c4",
                "s5c1s4",
                "s1c2c5"
            ]
        )
        r24 = self.splitup(
            [
                "-d6s5s1s2c4",
                "d6s5c1s4",
                "d6s1c2c5",
                "s1s2d3",
                "-c1a2"
            ]
        )
        r31 = self.splitup(
            [
                "c6c2c4c5",
                "-c6s2s5",
                "-c2s4s6"
            ]
        )
        r32 = self.splitup(
            [
                "-s6c2c4c5",
                "s6s2s5",
                "-c2s4c6"
            ]
        )
        r33 = self.splitup(
            [
                "-c2c4s5",
                "-s2c5"
            ]
        )
        r34 = self.splitup(
            [
                "-d6c2c4s5",
                "-d6s2c5",
                "-s2d3"
            ]
        )
        r41 = 0
        r42 = 0
        r43 = 0
        r44 = 1


        self.T = [
            [r11, r12, r13, r14],
            [r21, r22, r23, r24],
            [r31, r32, r33, r34],
            [r41, r42, r43, r44]
            ]
        return np.reshape(self.T, [4,4]) 
    # fix the values such as cos(0) (if you dont understand this section pls try np.cos(np.deg2rad( ! )) 
    def fixing(self, expr):
    #print(np.where((expr < 0) & (expr > -0.01) , 0, expr))
        return np.where((expr < 0.01) & (expr > -0.01) , 0, expr) 

    def calculate(self, deg):
        total = 1
        if deg[0] != "-":
            for i in range(0, len(deg), 2):

                if deg[i] == "c":
                    total *= self.fixing(
                        np.cos(np.deg2rad(self.theta[int(deg[i+1])-1]))
                        )

                elif deg[i] == "s":
                    total *= self.fixing(
                        np.sin(np.deg2rad(self.theta[int(deg[i+1])-1]))
                        )

                elif deg[i] == "d":
                    if deg[i+1] == "6":
                        total *= self.d[int(deg[i+1])-5]
                    elif deg[i+1] == "3":
                        total *= self.d[int(deg[i+1])-3]
                    else: print("check the variables")

                elif deg[i] == "a":
                    total *= self.a2[0];

                else: print("It shows us an error")

        elif deg[0] == "-":
            for i in range(1, len(deg), 2):

                if deg[i] == "c":
                    total *= self.fixing(
                        np.cos(np.deg2rad(self.theta[int(deg[i+1])-1]))
                        )

                elif deg[i] == "s":
                    total *= self.fixing(
                        np.sin(np.deg2rad(self.theta[int(deg[i+1])-1]))
                        )

                elif deg[i] == "d":
                    if deg[i+1] == "6":
                        total *= self.d[int(deg[i+1])-5]
                    elif deg[i+1] == "3":
                        total *= self.d[int(deg[i+1])-3]
                    else: print("check the variables")

                elif deg[i] == "a":
                    total *= self.a2[0]

                else: print("It shows us an error")
       
        return total 
    
    def pointInPlane(self, nokta, **axis):
        if axis['axis'] == 'global':
            return np.matmul(self.matrix(), np.reshape(np.append(nokta, 1), [4, 1]))
        else:
            return np.matmul(np.linalg.inv(self.matrix()), np.reshape(np.append(nokta, 1), [4, 1]))
            
