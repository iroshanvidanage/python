def min_refills(x, n, l):
    num_refills, current_refill = 0, 0

    while current_refill <= n:
        last_refills = current_refill

        while current_refill <= n and x[current_refill + 1] - x[current_refill] <= l:
            current_refill += 1

        if current_refill == last_refills:
            return 'Impossible'

        if current_refill <= n:
            num_refills += 1

    return num_refills
