#coding=utf-8
"""
实现列表的排序

"""
def sort_list(the_list):
    for i in range(0,len(the_list)):
        for j in range(i+1,len(the_list)):
            if the_list[i] > the_list[j]:
                print(the_list)
                #互换值
                the_list[i],the_list[j] = the_list[j],the_list[i]
    return the_list

if __name__ == "__main__":
    test_list = [3,2,0,4,1,5]
    res_list = sort_list(test_list)
    print(res_list)