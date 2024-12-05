

def return_ans(arr , k):
    l = 0
    r = 0
    temp_store = []
    final_ans = []
    while(r < len(arr)):
        if arr[r] < 0:
            temp_store.append(arr[r])
        
        if r - l + 1 != k :
            r+=1
        elif r - l + 1 == k :
            if len(temp_store) == 0 :
                final_ans.append(0)
            else:
                final_ans.append(temp_store[0])
                if arr[l] < 0:
                    temp_store.pop(0)
            r+=1
            l+=1
    return final_ans