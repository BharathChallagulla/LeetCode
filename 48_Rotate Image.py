class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1

        while l < r:

            t, b = l, r
            for i in range(r - l):

                # store topLeft in temporary variable
                topLeft = matrix[t][l+i]
                
                # store topBottom at topLeft
                matrix[t][l+i] = matrix[b-i][l]

                # store bottomRight at bottomLeft
                matrix[b-i][l] = matrix[b][r-i]

                # store topRight in bottomRight
                matrix[b][r-i] = matrix[t+i][r]

                # store our topLeft at topRight
                matrix[t+i][r] = topLeft
            l, r = l+1, r-1