'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

def ordered_2darray_search(twod_array,a_num):
    nrow = len(twod_array)
    ncol = len(twod_array[0])
    i = nrow-1
    j = 0
    try:
        while i>=0 and j<=ncol:
            if twod_array[i][j] > a_num:
                i = i - 1
            elif twod_array[i][j] < a_num:
                j = j + 1
            else:
                print ("True")
                break
    except Exception as e:
        print(repr(e))

twod_array = [[1,2],[3,4]]

a_num = 2

ordered_2darray_search(twod_array,a_num)