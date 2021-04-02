def merge_sort(list1):
    if len(list1) <= 1:
        return list1
    left = list1[:len(list1)//2]
    right = list1[len(list1)//2:]
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
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 4, 5, 6, 7, 8]
    print(split_list(list1 + list2))
