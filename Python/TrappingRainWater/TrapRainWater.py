"""Solution to trap the rain water."""

"""
Problem:
=======
Given n Non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining
"""
class TrapRainWater:
    def trap(self, height):
        left_hieghest = 0
        right_hieghest = 0
        lmap = list()
        rmap = list()
        total_liters = 0
        for  map_v in height:
            left_hieghest = max(left_hieghest, map_v)
            lmap.append(left_hieghest)

        for map_v in height[::-1]:
            right_hieghest = max(right_hieghest, map_v)
            rmap.append(right_hieghest)

        for elem,l_h,r_h in zip(height,lmap,reversed(rmap)):
            total_liters = total_liters + (min(l_h, r_h) - elem)

        return total_liters

if __name__ == '__main__':
    elv_map = [0,1,0,2,1,0,1,3,2,1,2,1]
    trapped_water = TrapRainWater().trap(elv_map)
    print("Amount of water trapped: ", trapped_water)
