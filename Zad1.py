def flatten_list(wej):
    result = []
    for x in wej:
        if type(x) == int:
            result.append(x)
        elif type(x) == list:
            flatten_list(x)
    return result

a = [1, 2, [3, 4, [5], [6]], 7, 8, 9]

print(flatten_list(a))