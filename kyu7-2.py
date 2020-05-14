# Given a 2D list of size m * n. Your task is to find the sum of minimum value in each row.

def sum_of_minimums(numbers) :    
    small_list = []
    for each in numbers :
        small_list.append(min(each))

    total = 0
    for each in small_list :
        total = total + each

    return total

print(sum_of_minimums([
  [2, 1, 3, 4, 5],       # minimum value of row is 1
  [5, 6, 7, 8, 9],       # minimum value of row is 5
  [22, 21, 20, 56, 100]  # minimum value of row is 20
]))
