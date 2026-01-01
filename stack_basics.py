def build_array(list,n):
    i = 0
    j = 0
    final_list = []
    for i in range(1, n+1):
        if j == len(list):
            break

        if i == list[j]:
            final_list.append('Push')
            j+=1
        
        else:
            final_list.append('Pop')

    return final_list

print(build_array([1,3], 3))


