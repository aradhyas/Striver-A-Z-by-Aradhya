class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes * 6
        hour_angle = hour * 30 + minutes * 0.5
        
        diff = abs(minute_angle - hour_angle)
        
        if diff > 180:
            diff = 360 - diff
        
        return diff