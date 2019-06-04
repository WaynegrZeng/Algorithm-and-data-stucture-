def xxx(twod_array,a_num):
    nrow = len(twod_array)
    ncol = len(twod_array[0])
    i = nrow-1
    j = 0
    try:
        while i>=0 and j<=ncol:
            # print(str(twod_array[i][j]))
            if twod_array[i][j] > a_num:
                i = i - 1
            elif twod_array[i][j] < a_num:
                j = j + 1
            else:
                print ("True")
                break
    except Exception as e:
        print(repr(e))

twodarrya = [[1,2],[3,4]]

anum = 2

xxx(twodarrya,anum)