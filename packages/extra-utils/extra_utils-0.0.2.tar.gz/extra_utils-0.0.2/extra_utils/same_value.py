# @Time : 2021/10/1 13:20 
# @Author : skyoceanchen
# @File : same_value.py 
# @Software: PyCharm
# @PRODUCT_NAME: PyCharm
# @MONTH_NAME_SHORT:10月

def same_up_list(lis):
    for index, value in enumerate(lis):
        if index != 0:
            if int(value) == 0:
                value = lis[index - 1]
                lis[index] = value
    return lis

