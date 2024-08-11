class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0,0
        res = []

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        direction = RIGHT

        while len(res) != m*n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    res.append(matrix[i][j])
                    j += 1
                i += 1
                j -= 1
                direction = DOWN
                RIGHT_WALL -= 1

            elif direction == DOWN:
                while i < DOWN_WALL:
                    res.append(matrix[i][j])
                    i += 1
                i -= 1
                j -= 1
                direction = LEFT
                DOWN_WALL -= 1

            elif direction == LEFT:
                while j > LEFT_WALL:
                    res.append(matrix[i][j])
                    j -= 1
                i -= 1
                j += 1
                direction = UP  
                LEFT_WALL += 1 
            elif direction == UP:
                while i > UP_WALL:
                    res.append(matrix[i][j])
                    i -= 1
                i += 1
                j += 1
                direction = RIGHT  
                UP_WALL += 1
        return res