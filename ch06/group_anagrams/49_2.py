strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
arr_dict  = dict()
for x in strs:
    temp = ''.join(s for s in sorted(x))
    if temp not in arr_dict:
        arr_dict[temp] = []
    arr_dict[temp].append(x)

arr = []    
for key,value in arr_dict.items():
    arr.append(value)
print(arr)