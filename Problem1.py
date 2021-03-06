#Problem 1
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

def sum_check(num_list,k):
    potential_solutions = set()
    for i in num_list:
        if (k-i) in num_list:
            return True
        potential_solutions.add(k-i)
    return False

sum_check([10, 15, 3, 7],17)