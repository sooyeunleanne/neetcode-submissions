class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        prev_time_to_target = 0 # time it takes the fleet ahead to reach target

        for pos,spd in cars:
            time_to_target = (target - pos)/spd

            # if this car takes longer to reach target than the car(s) ahead
            # it can't catch up to the fleet, so it forms a new fleet
            if time_to_target > prev_time_to_target:
                fleets += 1
                prev_time_to_target = time_to_target
            
            # otherwise, it catches up to the fleet ahead and merges with it
        
        return fleets