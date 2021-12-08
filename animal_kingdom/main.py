def groupChild(arr, parent, final):
    if len(arr) <= 0:
        return final
    else:
        # Take all elements which [1] is in parent
        newParent = [elem[0] for elem in arr if elem[1] in parent]
        newArr = [elem for elem in arr if elem[1] not in parent]
        final = final + [newParent]
        return groupChild(newArr, newParent, final)


if __name__ == "__main__":
    arr = [-1, 8, 6, 0, 7, 3, 8, 9, -1, 6]
    pairs = [[i, e] for i, e in enumerate(arr) if e != -1]
    parent = [i for i, e in enumerate(arr) if e == -1]
    res = groupChild(pairs, parent, [parent])
    print(res)
    print(len(res))

    # [[0, -1], [1, 8], [2, 6], [3, 0], [4, 7], [5, 3], [6, 8], [7, 9], [8, -1], [9, 6]]
    # for elem in pairs:
    #     print('elem', elem)
    #     if elem[1] == -1:
    #         print('a')
    #         try:
    #             parent[elem[0]]
    #         except KeyError:
    #             parent[elem[0]] = []

    #     elif elem[1] in parent.keys():
    #         prevVal = parent[elem[1]]
    #         currentVal = elem[0]
    #         parent[elem[1]] = prevVal + [currentVal]

    #     else:
    #         print('c')
    #         parent[elem[1]] = [elem[0]]

    #     print(parent)
    #     print()

 
