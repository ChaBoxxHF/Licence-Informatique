def fusion(l1,l2):
    i=0
    Lord=[]
    while i<len(l1) or i<len(l2):
        if l1[i]<l2[i]:
            Lord+=l1[i]
            i+=1
        elif l2[i]<l1[i]:
            Lord+=l2[i]
            i+=1
    return(Lord)
