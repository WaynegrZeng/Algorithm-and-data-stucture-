#全局的list或者dict可以在函数内部被直接修改
#int或者str则需要进行global声明

#参考自B站，鹤翔万里：快速排序|演示|优化
def QuickSort(array,head,tail):
    if head >= tail:
        return None
    key = array[head]
    p1 = head
    p2 = tail
    while p1 < p2:
        while p1<p2 and array[p2]>=key:
            p2 = p2 - 1
        array[p1],array[p2] = array[p2],array[p1]
        while p1<p2 and array[p1]<=key:
            p1 = p1 + 1
        array[p1],array[p2] = array[p2],array[p1]     
    QuickSort(array,head,p1-1)
    QuickSort(array,p1+1,tail)

array = [2,3,5,1,4,6,-1,0]
QuickSort(array,0,len(array)-1)
print(array) #[-1, 0, 1, 2, 3, 4, 5, 6]


def test(array):
    array.append(4)
aaa = [2,3]
test(aaa)
print(aaa) #[2, 3, 4]