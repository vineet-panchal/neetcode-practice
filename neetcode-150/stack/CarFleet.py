'''
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:

Input: target = 10, position = [1,4], speed = [3,2]

Output: 1
Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

Example 2:

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Output: 3
Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

Constraints:

n == position.length == speed.length.
1 <= n <= 1000
0 < target <= 1000
0 < speed[i] <= 100
0 <= position[i] < target
All the values of position are unique.

'''

'''


Problem Explanation
This problem is about cars on a highway where:

Cars can't overtake each other
A slower car ahead blocks faster cars behind it
When a faster car catches up to a slower one, they form a "fleet" and travel together
We need to count how many separate fleets reach the destination

Key Insight
The crucial observation is: cars closer to the target have priority. A car can only join a fleet if it catches up to the car directly ahead of it before reaching the destination.
For each car, we can calculate its "time to reach target":
time = (target - position) / speed
If a car behind has a smaller or equal time than the car ahead, it will catch up and form a fleet. Otherwise, it remains a separate fleet.
Example Walkthrough
Example 2: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Sort cars by position (closest to target first):

Car at pos 7: time = (10-7)/1 = 3 hours
Car at pos 4: time = (10-4)/2 = 3 hours
Car at pos 1: time = (10-1)/2 = 4.5 hours
Car at pos 0: time = (10-0)/1 = 10 hours


Process from closest to farthest:

Car at 7: forms fleet #1 (time = 3)
Car at 4: time = 3 ≤ 3, catches up → joins fleet #1
Car at 1: time = 4.5 > 3, can't catch up → forms fleet #2
Car at 0: time = 10 > 4.5, can't catch up → forms fleet #3



Answer: 3 fleets
'''


def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create pairs of (position, time_to_target)
        cars = []
        for pos, spd in zip(position, speed):
            time_to_target = (target - pos) / spd
            cars.append((pos, time_to_target))
        
        # Sort by position in descending order (closest to target first)
        cars.sort(reverse=True)
        
        # Stack to store the time of each fleet
        stack = []
        
        for pos, time in cars:
            # If this car is slower (takes more time) than the fleet ahead,
            # it cannot catch up and forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # Otherwise, it catches up and joins the fleet ahead
            # (we don't append - it merges with the existing fleet)
        
        return len(stack)


def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine and sort by position (descending)
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        
        for pos, spd in cars:
            time = (target - pos) / spd
            
            # New fleet if stack is empty or this car is slower
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)

'''


Complexity

Time: O(n log n) for sorting
Space: O(n) for the cars list and stack

The Python version is even more concise while maintaining the same logic and clarity!
'''