"""There are 2N people a company is planning to interview. cost of flying i-th
person to city A is costs[i][0] and the cost of flying the i-th person to city
B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N
people arrive in each city
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
interviewing in each city.

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""

class TwoCityScheduling:
    def twoCitySchedCost(self, costs: list) -> int:
        people_per_city = len(costs) / 2
        cityAprofit = [cost[1] - cost[0] for cost in costs] 
        cityAcandidates = list()
        cityBcandidates = list()
        for i in range(len(cityAprofit)):
            bcc = 0     # better cost count
            ref_profit = cityAprofit[i]
            for j in range(len(cityAprofit)):
                if i == j:
                    continue
                if cityAprofit[j] > ref_profit:
                    bcc += 1
                    if bcc > people_per_city:
                        break
            if bcc < people_per_city and (len(cityAcandidates) <
                people_per_city):
                cityAcandidates.append(i)
            else:
                cityBcandidates.append(i)
        total_cost = 0
        print("City A Candidates:",cityAcandidates)
        print("City b Candidates:",cityBcandidates)
        for i in range(len(costs)):
            if i in cityAcandidates:
                total_cost = total_cost + costs[i][0]
            else:
                total_cost = total_cost + costs[i][1]

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
    min_route = TwoCityScheduling().twoCitySchedCost(costs)
    print(min_route)
