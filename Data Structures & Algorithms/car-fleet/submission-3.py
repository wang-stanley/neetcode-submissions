class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_position, sorted_speed = zip(*sorted(zip(position, speed), reverse=True))
        sorted_position = list(sorted_position)
        sorted_speed = list(sorted_speed)

        print(f"sorted positions: {sorted_position}")
        print(f"sorted speeds: {sorted_speed}")

        fleets = []

        for i, p in enumerate(sorted_position):
            curEta = (target - p) / sorted_speed[i]
            if not fleets:
                fleets.append(curEta) # maybe use eta instead of p [x]
                continue
            # print(f"Cur Eta: {curEta} vs Next Eta: {fleets[-1]}")
            if curEta > fleets[-1]:
                fleets.append(curEta)

        return len(fleets)

        