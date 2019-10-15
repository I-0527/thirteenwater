        if len(huabucket[i])>=5 and f1==True:    #同花顺
            flag[0]=1
            thua=list(set(huabucket[i]))
            thua.sort()
            arr=[]
            for j in thua:
                arr.append(val.index(j))
            if f2=='A':
                newcard.append(i+'10')
                order.remove(i+'10')
                newcard.append(i+'J')
                order.remove(i+'J')
                newcard.append(i+'Q')
                order.remove(i+'Q')
                newcard.append(i+'K')
                order.remove(i+'K')
                newcard.append(i+'A')
                order.remove(i+'A')
                newindex = newindex-5
            else :
                j = val.index(f2)
                for k in range(j-4,j+1,1):
                    newcard.append(i+val[k])
                    order.remove(i+val[k])
                newindex = newindex-5

    order=sortCard(order,newindex)
    tbucket = {'A':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'Q':0,'K':0}
    thuabucket = {'$':[],'&':[],'*':[],'#':[]}
    for x in order:
        tbucket[x[1:]] = tbucket[x[1:]] + 1
        thuabucket[x[0]].append(x[1:])
    if 1:
        if isbomb(**tbucket)==True:   #炸弹
            flag[1]=1
            arr=[]
            for i,j in tbucket.items():
                if j==4:
                    arr.append(val.index(i))
            arr.sort()
            if len(arr)!=0 and arr[0]==1:        #AAAA
                for i in range(4):
                    newcard.append('$A')
                    order.remove('$A')
                    newcard.append('*A')
                    order.remove('*A')
                    newcard.append('&A')
                    order.remove('&A')
                    newcard.append('#A')
                    order.remove('#A')
                newindex = newindex -4
            else:
                newcard.append('$'+val[max(arr)])
                order.remove('$'+val[max(arr)])
                newcard.append('*'+val[max(arr)])
                order.remove('*'+val[max(arr)])
                newcard.append('&'+val[max(arr)])
                order.remove('&'+val[max(arr)])
                newcard.append('#'+val[max(arr)])
                order.remove('#'+val[max(arr)])
                newindex = newindex -4

    if flag[0]==1 and flag[1]==1:
        order = sortCard(order,4)
        thbucket = {'A':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'Q':0,'K':0}
        for x in order:
            thbucket[x[1:]] = thbucket[x[1:]] + 1
        arr=[]
        for i in range(4):
            arr.append(val.index(order[i][1:]))
        arr.sort()
        if isduizi(**thbucket) and arr[0]==arr[1] and arr[2]==arr[3]:    #同花顺炸弹对子
            if singleCardCompare(arr[0],arr[2])==1: 
                for i in order:
                    if i[1:]==val[arr[2]]:
                        newcard.append(i)
                        order.remove(i)
                        newindex = newindex -1
                        break
                for i in range(3):
                    newcard.append(order[i])
                    newindex = newindex -1
                return userid,newcard
            elif singleCardCompare(arr[0],arr[2])==-1:
                for i in order:
                    if i[1:]==val[arr[0]]:
                        newcard.append(i)
                        order.remove(i)
                        newindex = newindex -1
                        break
                for i in range(3):
                    newcard.append(order[i])
                    newindex = newindex -1
                return userid,newcard
        elif isduizi(**thbucket) :
            for i,j in thbucket.items():
                if j==2:
                    num=val.index(i)
                    break
            for j in range(len(arr)):
                if arr[j]!=num:
                    for i in order:
                        if i[1:]==val[arr[j]]:
                            newcard.append(i)
                            order.remove(i)
                            newindex = newindex -1
                            break
            for i in range(2):
                newcard.append(order[0])
                order.remove(order[0])
                newindex = newindex -1
            return userid,newcard
        else:                  #同花顺炸弹乌龙
            if arr[0]==1:
                for i in range(1,4):
                    newcard.append(order[i])
                newcard.append(order[0])
            else:
                for i in range(4):
                    newcard.append(order[i])
            return userid,newcard
        
