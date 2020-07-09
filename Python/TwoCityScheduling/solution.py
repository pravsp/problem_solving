class Solution:
    def twoCitySchedCost(self, costs) -> int:
        ppc = len(costs) / 2    # People Per City
        cityAprofitlst = list()
        cityACandidates = list()
        cityBCandidates = list()
        for i in range(len(costs)):
            Aexpense = costs[i][0]
            Bexpense = costs[i][1]
            cityAProfit = Bexpense - Aexpense
            cityAprofitlst.append((cityAProfit, Aexpense, Bexpense, i))

        cityAprofitlst.sort()
        total_cost = 0
        bCandidatecount = 0
        for cityAprofit, Aexp, Bexp, idx in cityAprofitlst:
            if bCandidatecount < ppc:
                total_cost += Bexp
                cityBCandidates.append(idx)
                bCandidatecount +=1
            else:
                total_cost += Aexp
                cityACandidates.append(idx)


        print("City A Candidates:", cityACandidates)
        print("City B Candidates:", cityBCandidates)
        return total_cost

if __name__ == '__main__':
    # costs = [[10,20],[200, 50],[180, 30],[30,20]]
    # costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    costs = [[33,135], [849,791], [422,469], [310,92], [253,489],
             [995,760], [852,197], [658,216], [679,945], [197,341],
             [362,648], [22,324], [408,25], [505,734], [463,279],
             [885,512], [922,850], [784,500], [557,860], [528,367],
             [877,741], [554,545], [598,888], [558,104], [426,427],
             [449,189], [113,51], [201,221], [251,62], [981,897],
             [392,519], [115,70], [961,109], [512,678], [476,708],
             [28,902], [763,282], [787,774], [925,475], [253,532],
             [100,502], [110,857], [822,942], [231,186], [869,491],
             [651,344], [239,806], [651,193], [830,360], [427,69],
             [776,875], [466,81], [520,959], [798,775], [875,199],
             [110,396]]
    print("Costs of each candidates:", costs)
    min_route = Solution().twoCitySchedCost(costs)
    print(min_route)
    

