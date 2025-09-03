cost = [[1,10.20],[1,5.10],[2,7.1],[3,9.0],[3,4.5],[4,14.23],[4,6.12],[5,10.20]]
totalcost = []
def calculatetotalcost():
        
        for i in range(1,6):
            initialcost = 0
            for items in cost:
                
                if items[0] == i:
                    initialcost += items[1]
                        
            totalcost.append(initialcost)

calculatetotalcost()
print(totalcost)



