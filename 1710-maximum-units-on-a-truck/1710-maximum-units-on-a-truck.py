class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        unit = 0
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        sorted_box = boxTypes
        for n_box, unit_box in sorted_box:
            if n_box >= truckSize:
                unit = unit + truckSize * unit_box
                truckSize = 0
                break
            else:
                truckSize -= n_box
                unit = unit + n_box * unit_box
        return unit