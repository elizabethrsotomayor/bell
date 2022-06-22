def bell(n: int) -> list:
    """
    Receive a positive integer and return an array based on the example:
    n => resulting array

     1 => [1]
     2 => [2, 2]
     3 => [3, 4, 3]
     4 => [4, 6, 6, 4]
     5 => [5, 8, 9, 8, 5]
     6 => [6, 10, 12, 12, 10, 6]
     7 => [7, 12, 15, 16, 15, 12, 7]
     8 => [8, 14, 18, 20, 20, 18, 14, 8]
     9 => [9, 16, 21, 24, 25, 24, 21, 16, 9]
    10 => [10, 18, 24, 28, 30, 30, 28, 24, 18, 10]
    11 => [11, 20, 27, 32, 35, 36, 35, 32, 27, 20, 11]
    12 => [12, 22, 30, 36, 40, 42, 42, 40, 36, 30, 22, 12]
    :param n: the number to base the bell on
    :return:
    """
    lst = []
    initial = n - 2
    for i in range(1, n + 1):
        if n > 2 and 1 < i < n:
            if 3 <= i <= (n - 2):
                initial = initial - 2
                lst.append(lst[i - 2] + initial)
            elif i == n - 1:
                initial = n - 2
                lst.append(n + initial)
            else:
                lst.append(n + initial)
        else:
            lst.append(n)

    return lst
