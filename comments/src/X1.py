class X1:

    @staticmethod
    def sum_of_squares(lower_bound, upper_bound):
        total = 0

        for num in range(lower_bound, upper_bound + 1):
            total += X1.square(num)

        return total

    @staticmethod
    def square(num):
        return num * num
