def zero_one_bag_problem(num, capacity, weight_list, value_list):
    value_matrix = [[0 for i in range(capacity)] for i in range(num)]
    for j in range(capacity):
        current_capacity = j+1
        for i in range(num):
              if weight_list[i] > current_capacity:
                  if i== 0:
                      value_matrix[i][j] = 0
                  else:
                      value_matrix[i][j] = value_matrix[i-1][j]

              elif  weight_list[i] <= current_capacity:
                  if current_capacity - sum(weight_list[0:i+1]) >= weight_list[i]:
                      value_matrix[i][j] = value_matrix[i-1][j] + value_list[i]
                  else:
                      temp = current_capacity - weight_list[i]
                      case1 = value_matrix[i-1][temp-1] + value_list[i]
                      case2 = value_matrix[i-1][j]
                      value_matrix[i][j] = max(case1,case2)
    print(value_matrix)
    return value_matrix[-1][-1]







if __name__ == "__main__":
    num = 5
    capacity = 10
    # weight_list = [2, 2, 6, 5, 4]
    value_list = [6, 3, 5, 4, 6]
    weight_list = [1, 1, 3, 1, 1]

    q = zero_one_bag_problem(num, capacity, weight_list, value_list)
    print(q)