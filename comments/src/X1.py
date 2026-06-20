class X1:

    @staticmethod
    def sum_of_squares(lower_bound, upper_bound):
        total = 0

        # Iterate from lower bound (q) to upper bound (z)
        for num in range(lower_bound, upper_bound + 1):
            # Add square of each number in the range
            total += X1.square(num)

        # Return accumulated sum
        return total

    @staticmethod
    def square(num):
        # Return square of input
        return num * num
