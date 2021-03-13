# Functions
def l_s(ar,item):
    i=0
    while i < len(ar) and ar[i]!=item :
        i+=1
    if i< len(ar):
        return i
    else:
        return False

def b_s(ar,item):
    beg=0
    last=len(ar)-1
    while(beg<=last):
        mid= (beg+last)/2
        if (item == ar[mid]):
            return mid
        elif (item >ar[mid]):
            beg=mid+1
        else:
            last= mid-1
    else:
        return False          #when item not found

def Findpos(ar,item):
    size=len(ar)
    if item<ar[0]:
        return 0
    else:
        pos=-1
        for i in range (size-1):
            if (ar[i]<=item and item < ar[i+1]):
                pos=i+1
                break
            if (pos==-1 and i<=size-1):
                pos = size
        return pos

def shift(ar,pos):
    ar.append(None) # add an empty element at an end
    size = len(ar)
    i=size-1
    while i>=pos:
        ar[i]=ar[i-1]
        i=i-1

def s_sort(liste):
    for curpos in range(len(liste)):
        minpos=curpos  #starting with current position
        for scanpos in range(curpos+1,len(liste)):
            if liste[scanpos]<liste[minpos]:
                minpos=scanpos
        #Swap the two values
        temp=liste[minpos]
        liste[minpos]=liste[curpos]
        liste[curpos]=temp

def swapelements(list):
    i=0
    while (i<len(list)-1):
        if (list[i]>list[i+1]):
            temp=list[i]
            list[i]=list[i+1]
            list[i+1]=temp
        i=i+1
        #print " List after pass",(i), ":",list

def b_sort(list):
    for num in range(len(list)-1):
        pass
    swapelements(list)

def i_sort(ar):
    for i in range(1,len(ar)):
        v=ar[i]
        j=i
        while ar[j-1]> v and j>=1:
            ar[j]=ar[j-1]
            j-=1
        #Insert the value at its correct postion
        ar[j]=v

def traverse(ar):
    size =len(ar)
    for i in range(size):
        print (ar[i])

def isempty(stk):
    if stk==[]:
        return  True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top=len(stk)-1

def pop(stk):
    if isempty(stk):
        return "Underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item

def peek(stk):
    if isempty(stk):
        return "Underflow"
    else:
        top=len(stk)-1
        return stk[top]

def display(stk):
    if isempty(stk):
        return "Stack empty"
    else:
        top=len(stk)-1
        print (stk[top],"<-top")
        for a in range(top-1,-1,-1):
            print (stk[a])
def clean(n):
    print (" "*n )

def qu_isempty(qu):
    if qu==[]:
        return  True
    else:
        return False

def qu_enqueue(qu,item):
    qu.append(item)
    if len(qu)==1:
        front=rear=0
    else:
        rear=len(qu)-1

def qu_peek(qu):
    if qu_isempty(qu):
        return "Underflow"
    else:
        front=0
    return qu[front]

def qu_dequeue(qu):
    if qu_isempty(qu):
        return "Underflow"        
    else:
        item=qu.pop(0)
    if len(qu)==0:      #if it was single element queue
        front=rear=None
    return item

def qu_display(au):
    if qu_isempty(qu):
        print("QueUE Empty")
    elif len(qu)==1:
        print ([qu],"<== front,rear")
    else:
        front=0
        rear=len(qu)-1
        print (qu[front],"<- front")
        for a in range(1,rear):
            print (qu[a])
        print (qu[rear],"<-rear")

def line():
    print ("-------------------------------------------------------------------------------")

def raw_input(n):
    print (n)
