def find_triplet(arr,n):
    found = False
    for j in range(0,n-2):
        for i in range(j+1,n-1):
            for k in range(i+1,n):
                if(arr[j]+arr[i]+arr[k] == 0):
                    print(arr[i],arr[j],arr[k])
                    found = True
    if(found == false):
        print("not exist")
                  
arr = [-1, 4, 0 ,5,1]
print(find_triplet(arr,len(arr))
                
                       
             

                
        
   
   
    
      
           
     
                
                
