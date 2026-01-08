def find_number_of_provinces(isConnected):
    n = len(isConnected)
    province = 0
    visited = [False]*n

    def dfs(city):
        visited[city] = True
        for j in range(n):
            if isConnected[city][j] == 1 and not visited[j]:
                dfs(j)
    
    for i in range(n):    
        if not visited[i]:
                dfs(i)
                province+=1

    return province

isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
print(find_number_of_provinces(isConnected))

# [true   , true   , true]
# [0      ,1      ,2      ]

# 1st dfs = visited [0] = true so 
#     0, 0 ==1 but visited
#     0, 1 == 1 and not visited
#       so now we have dfs(1) = 
#       visited[1] = true
#       1, 0 is 1 but visited
#       1,1 is 1 but visited
#       1,2 is 0

#       so this makes province = 1
#       now we do for i in range n, but 0,1 is visited so we go to 2
#       visited[2] = true
#             2,0 = 0
#             2,1 = 0
#             2,2 = 1

#     then we go to province and add 1. hence, it becomes 2

