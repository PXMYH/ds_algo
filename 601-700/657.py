# 657. Robot Return to Origin

# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

# The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

# Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

# Example 1:

# Input: "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.


# Example 2:

# Input: "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # method 1: turn string into an array and add together values => 152ms
        geo_location = 0
        for move in moves:
            if move == "L":
                geo_location += 1
            if move == "R":
                geo_location -= 1
            if move == "U":
                geo_location += 0.5
            if move == "D":
                geo_location -= 0.5

        if geo_location == 0:
            return True
        else:
            return False

        # method 2: use hashmap (dictionary), L and R are complementary, check both
        # to see if values are the same => 120ms

        if "L" in moves and "R" not in moves:
            return False

        if "R" in moves and "L" not in moves:
            return False

        if "U" in moves and "D" not in moves:
            return False

        if "D" in moves and "U" not in moves:
            return False

        geo_location = {}
        for move in moves:
            if move in geo_location:
                geo_location[str(move)] += 1
            else:
                geo_location[str(move)] = 1
        # print("geo: " + str(geo_location))

        if "U" in moves or "D" in moves:
            if "L" in moves or "R" in moves:
                if geo_location["U"] == geo_location["D"] and geo_location["L"] == geo_location["R"]:
                    return True
                else:
                    return False
            else:
                if geo_location["U"] == geo_location["D"]:
                    return True
                else:
                    return False
        else:
            if geo_location["L"] == geo_location["R"]:
                return True
            else:
                return False
