# 853. Car Fleet

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        max_time = 0.0

        for pos, spd in cars:
            time = float(target - pos)/ float(spd)

            #arriving slower than max_time = another fleet
            if time > max_time:
                fleets += 1
                max_time = time
        
        return fleets