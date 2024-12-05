

def return_ans(arr , k):
    i = j = 0
    
    temp_store = []
    final_ans = []
    
    while(j < len(arr)):
        if arr[j] < 0:
            temp_store.append(arr[j])
        
        if j - i + 1 != k :
            j+=1
        elif j - i + 1 == k :
            if len(temp_store) == 0 :
                final_ans.append(0)
            else:
                final_ans.append(temp_store[0])
                if arr[i] < 0:
                    temp_store.pop(0)
            j+=1
            i+=1
    return final_ans