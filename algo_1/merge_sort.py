import random


def merge_sort(list1):
    if len(list1) <= 1:
        return list1
    left = merge_sort(list1[:len(list1)//2])
    right = merge_sort(list1[len(list1)//2:])
    return merge_sorted_list(left, right)


def merge_sorted_list(list1, list2):
    full_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            full_list.append(list1[i])
            i += 1
        else:
            full_list.append(list2[j])
            j += 1
    while i < len(list1):
        full_list.append(list1[i])
        i += 1
    while j < len(list2):
        full_list.append(list2[j])
        j += 1
    return full_list


if __name__ == "__main__":
    while True:
        val = []
        for i in range(0, random.randint(10, 100)):
            val.append(random.randint(5, 10))
        sorted_val = sorted(val)
        if merge_sort(val) == sorted_val:
            print(val)
            print(merge_sort(val))
            print("OK")
        else:
            print(val)
            break
