class X1:

    @staticmethod
    def sum_of_squares(lower_bound, upper_bound):
        p = 0

        # Iterate from lower bound (q) to upper bound (z)
        for i in range(lower_bound, upper_bound + 1):
            # Add square of each number in the range
            p += X1.square(i)

        # Return accumulated sum
        return p

    @staticmethod
    def square(k):
        # Return square of input
        return k * k
