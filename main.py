"""This  mini project is created to teach new begineers how to program and
learn about python program """
try:
    from LLM import *
except ImportError:
    print ("Module Not imported")

# MAIN
con=True
while con:
    print("################################################################################")
    print("#                                                                              #")
    print("#                                PYTHON TUTORIAL                               #")
    print("#                                                                              #")
    print("################################################################################")
    print(" ")
    print(" Welcome to python tutorial!!!!!!!!")
    print(" ")
    print("  1. GET STARTED with PYTHON")
    print("  2. ABOUT PYTHON AND PROJECT")
    print("  3. EXIT")
    line()
#Main selection
    try:
        choose1=int(input("Enter your choice(1-3):"))
    except IOError:
        print (" No Input!")
        print (" ")
        print ("PROGRAM WILL RESTART")
        clean(2)
        line()
#Get Started With Python
    if choose1==1:
        con2=True
        while con2:
            clean(2)
            #Getting Started Menu
            print (" Lets start with python")
            print ("Choose anyone of the module to start")
            clean(2)
            print(" 1. Working with Srings")
            print(" 2. Simple Input and Output Statements")
            print(" 3. Python Functions and Modules")
            print(" 4. Loops in Python")
            print(" 5. Data Types and Usage")
            print(" 6. Linear list Manipulation")
            print(" 7. Stacks and Queues")
            print(" 8. Data File Handiling")
            print(" 9. Exception handiling and Generators in python")
            print("10. Get back to main menu")
            line()
            #1.Getting Started Selecion 
            try:
                choose2=int(input("Enter your choice(1-10): "))
            except IOError:
                print ("No input given")

            #1.1.String Operations
            if choose2==1: 
                con3=True
                while con3:
                    clean(2)
                    
                    #String Operations Menu
                    print ("Strings :-A data type are any number of valid characters into a set of quotion marks.")
                    print ("Operations that can be performed with string are::")
                    clean(2)
                    print ("1.Traversing of string")
                    print ("2.String opeartors  on string")
                    print ("3.String Functions")
                    print ("4.Slicing a string")
                    print ("5.Get Back to previous menu")
                    line()
                    #String Operations Selection
                    try:
                        choose3=int(input("Enter your choice(1-5):"))
                    except IOError:
                        print ("No input given")

                    #1.1.1.Transversing of string
                    if choose3==1:
                        print ("Traversing can be performed in a following way")
                        a=("Python")
                        print (">>>j=0")
                        print (">>>a='Python'")
                        print (">>>for i in a:")
                        print ("      print j,'-',i")
                        print ("      j=j+1")
                        print ("_______________")
                        j=0
                        for i in a :
                             print(j,"-",i)
                             j=j+1
                        print()
                        print (" *** ")
                        line()

                    #1.1.2.String operators on strings 
                    elif choose3==2:
                        print ("String operators are")
                        print ("1.String Concatenation operator (+):")
                        print ("  eg.")
                        print ("     'pineapple' + 'pen'")
                        print ("  will result into")
                        print ("     'pineapplepen' ")
                        print ("2. String replication operator  (*):")
                        print ("  eg.")
                        print ("     'DSS'*3")
                        print ("  will result into ")
                        print ("     'DSSDSSDSS'")
                        print ("3. Mermbership operator:")
                        print ("in : Returns True if sub string  exist in given string, otherwise False")
                        print ("not in: Returns True if sub string   not exist in given string, oterwise False")
                        print (" eg.")
                        print ("   >>> 'a' in 'ahmed'")
                        print ("       True")
                        print ("   >>> 'a' not in 'ahmed'")
                        print ("       False")
                        print ("4.Comparison operator(<,>,>=,<=,==,!=):")
                        print (" eg.")
                        print ("   'a'=='a' will give True")
                        print ("   'a'=='b' will give False")
                        line()

                    #1.1.3.String Functions
                    elif choose3==3:
                        q=open("S_FUN.txt")
                        w=q.read()
                        print (w)
                        del q,w
                        raw_input("Press Enter to Continue")
                        line()
                    #1.1.4.Slicing a string
                    elif choose3==4:
                        clean(2)
                        print ("Slicing a string can be performed  as follow,")
                        print ("")
                        print (">>a=Python")
                        a='Python'
                        print (">>>print a[0:3]")
                        print ("  ",a[0:3])
                        line()

                    #1.1.5.Get Back Previous Menu
                    elif choose3==5:
                        con3=False
                    else:
                        print ("Invalid input !!!!!!!!!!!")
                            
            #1.2.Simple Input output statements
            elif choose2==2:   
                print ("Smple input and output statement can be given bu using")
                print ("1. For input :")
                print ("  1.input() and")
                print ("  2.raw_input()")
                print ("  Following are sample programs to illustrate")
                print ("    eg.")
                print ("       >>> a=raw_input('Enter your  number:' )")
                print ("           Enter your number: 25")
                clean(2)
                print ("2.For output Python use 'print' key word")
                print (" ")
                print (">>>For i in 'Python':")
                print ("      print i    ")    # print is output keyword
                print ("   Output will be as")
                print ("   P \n   y\n   t\n   h\n   o\n    n\n")
                line()
                
            #1.3. Python functions and modules
            elif choose2==3: 
                 con4=True
                 while con4:                 
                     print ("Python offers 3 type of Functions")
                     print ("1.In-built functions")
                     print ("2.Function defined in Modules")
                     print ("3.User  defined functions")
                     print ("4.Get back to previous menu")
                     line()
                    #Functions and modules selection
                     try:
                         choose4=int(input(" Enter your choice(1-4):"))
                     except IOError:
                         print ("No input provided")

                    #1.3.1.In Built functions
                     if choose4==1:
                        print ("Python offers some builtin functions which are always availabel to use")
                        print (" eg. len(),type(),int()")
                        clean(2)
                        print (">>> a=Python")
                        print (">>>len(a)")
                        print ("   6")
                        line()

                    #1.3.2.Functions defined in modules
                     elif choose4==2:
                         q=open("M_FUN.txt")
                         w=q.read()
                         print (w)
                         q.close()
                         del q,w
                         line()

                    #1.3.3.User defined functions   
                     elif choose4==3:
                         print ("These are the functions defined by programmer.And can be defined using 'def' keyword. ")
                         print ("How to create a function is illustrated in following eample")
                         print (" ")
                         print ("def sum(x,y):")
                         print ("    r= x+y")
                         print ("    return r")
                         print ("a=input('Enter number1:')")
                         print ("b=input('Enter number 2:)")
                         print ("c=sum(a,b)")
                         print ("print c")
                         line()
                    #1.2.4.Get back to previous menu
                     elif choose4==4:
                         con4=False       
                     else:
                        print ("Invalid in put")

            #1.4.Loops In python
            elif choose2==4:
                con5=True
                while con5:
                    print ("Python offers  2  type of loop statement")
                    print ("1. The for loop")
                    print ("2. The while loop")
                    print ("3. Get back to previous menu")
                    line()
                    #Loops selection
                    try:
                        choose4=int(input("Enter your choice(1-3):"))
                    except IOError:
                        print ("No input provided ")

                    #1.4.1.For loop
                    if choose4==1:
                        print ("The general form of 'for loop' is as given below:")
                        print (" for <variable> in <sequence> :")
                        print ("     statements_to_repeat")
                        clean(2)
                        print ("eg.")
                        print ("    for element in [10,15,20,25]:")
                        print ("        print (element +2),")
                        print ("Or for loop can be also used wiht range()function")
                        print ("eg.")
                        print ("   for val in range(3,10):")
                        print ("      print val")
                        line()
                    #1.4.2.While loop
                    elif choose4==2:
                        print ("The general form of while loop is given below")
                        print (" while <logicalExpression>:")
                        print ("    loop-body")
                        line()
                    #1.4.3 Get to the previous menu
                    elif choose4==3:
                        con5=False
                    else:
                        print ("Invalid Input")
            #1.5.Data types and usage
            elif choose2==5:
                try:
                    e=file("D_T.txt")
                    w=e.read()
                    print (w)
                except EOFError:
                    print ("Error in file opening")
                del e,w
                line()
                

            #1.6.Linear list Manipulation
            elif choose2==6:
                con6=True
                while con6:
                    print (" Basic operations on Linear list")
                    print ("1.Searching")
                    print ("2.Insertion")
                    print ("3.Deletion")
                    print ("4.Traversal")
                    print ("5.Sorting")
                    print ("6.Return to previous menu")
                    line()

                    #Linear list manipulation selection
                    try:
                        choose6=int(input("Enter your choice(1-6):"))
                    except:
                        print ("InputError!!!!")

                    #1.6.1.Searching
                    if choose6==1:
                        con7=True
                        while con7:
                            print ("Python offers 2 type of common searching technique")
                            print ("1.Linear search")
                            print ("2.Binary search")
                            print ("3.Return to previous menu")
                            line()

                            #Searching selection
                            try:
                                choose7=int(input("Enter your choice(1-3)"))
                            except IOError:
                                print ("Input error")

                            #1.6.1.1.Linear search
                            if choose7==1:
                                print ("__________________Linear search_______________")
                                print ("In linear search each element of array with the given Item to be searched for, one by one")
                                print ("Following program illustrate searching by linear search")
                                n=int(input("Enter desired linearlist(max.50).."))
                                print ("\nEnter elements for linear list\n")
                                ar=[0]*n  # initialise list of size n with zeros
                                for i in range(n):
                                    ar[i]=input("Element" +str(i+1) +":")
                                item=input("\nENter element to be searched for...")
                                index = l_s(ar,item)
                                if index :
                                    print ("\nElement found at index:",index,",position:",(index+1))
                                    line()

                                else:
                                    print ("\nSorry!! Givn element not found\n")
                                                          #1.6.1.2.Binary Search
                            elif choose7==2:
                                print ("___________________Binary search_______________")
                                print (" Binary search can work for any sorted array while linear search can work for both sorted as well as unsorted array")
                                n=input("Enter desired linear-list size(max. 50)..")
                                ar=[0]*n
                                for i in range(n):
                                    ar[i]=input("Element"+str(i+1)+":")
                                s_sort(ar)
                                print ("\List after sorting",ar)
                                item=input("\nEnter Element to be searched for...")
                                index=b_s(ar,item)
                                if index :
                                    print ("\nElement found at index:",index,",position:",(index+1))
                                    line()
                                else:
                                    print ("\nSorry!! Givn element not found\n")
                                    line()
                                

                            #1.6.1.3.Get to previous menu
                            elif choose7==3:
                                con7=False
                            else:
                                print ("Invalid input")
                            del choose7,con7

                    #1.6.2.Insertion
                    elif choose6==2:
                        print ("_________________Insertion in a list______________")
                        n=input("Enter desired linear-list size(max. 50)..")
                        ar=[0]*n
                        for i in range(n):
                            ar[i]=input("Element"+str(i+1)+":")
                        s_sort(ar)
                        print ("List in sorted order is",ar)
                        item=input("Enetr new element to be inserted:")
                        position=Findpos(ar,item)
                        shift(ar,position)
                        ar[position]=item
                        print ("The list after insertng",item,"is")
                        print (ar)
                        line()

                    #1.6.3.Deletion
                    elif choose6==3:
                        print ("______________Deletion in a list____________________")
                        n=input("Enter desired linear-list size(max. 50)..")
                        ar=[0]*n
                        for i in range(n):
                            ar[i]=input("Element"+str(i+1)+":")
                        s_sort(ar)
                        print ("List in sorted order is",ar)
                        item=input("Enter new element to be deleted:")
                        position=b_s(ar,item)
                        if position:
                            del ar[position]
                            print ("The list after deletion",item,"is")
                            print (ar)
                            line()
                        else:
                            print ("SORRY! No such element in the list")
                       

                    #1.6.4.Deletion
                    elif choose6==4:
                        print ("____________ Traversal of list_____________________")
                        n=input("Enter desired linear-list size(max. 50)..")
                        ar=[0]*n
                        print ("Enter element for the  linear list")
                        for i in range(n):
                            ar[i]=input("Element"+str(i+1)+":")
                        print ("Traversing the list:")
                        traverse(ar)
                        line()
                   

                    #1.6.5.Sorting
                    elif choose6==5:
                        print ("Python offers 3 type of common sorting technique")
                        print ("1.Selection sort")
                        print ("2.Bubble sort")
                        print ("3.Insertion sort")
                        line()
                        #Sorting selecion
                        try:
                            choose7=int(input("Enter your choice(1-3):"))
                        except IOError:
                            print ("Input error")

                        #1.6.5.1.Selection sort
                        if choose7==1:
                            print ("_______________________Selection sort____________________________")
                            print(" ")
                            print (" The basic idea of selection sort is to repeadily select the smallest key in remaining us sorted array")
                            print (" The following program ilustrate the sorting by selection sort")
                            n=input("Enter desired linear-list size(max. 50)..")
                            ar=[0]*n
                            print ("Enter element for the  linear list")
                            for i in range(n):
                                ar[i]=input("Element"+str(i+1)+":")
                            print ("Original list is:",ar)
                            s_sort(ar)
                            print ("List after sorting:",ar)
                            line()

                            #1.6.5.2.Bubble sort
                        elif choose7==2:
                            print ("______________________Bubble sort__________________________________")
                            print (" ")
                            print ("The basic idea of bubble sort is  to compare two adjoining values and exchange them if they are not in proper order.")
                            print (" The following program ilustrate the sorting by Bubble sort")
                            n=input("Enter desired linear-list size(max. 50)..")
                            ar=[0]*n
                            print ("Enter element for the  linear list")
                            for i in range(n):
                                ar[i]=input("Element"+str(i+1)+":")
                            print ("Original list is:",ar)
                            b_sort(ar)
                            print ("List after sorting:",ar)
                            line()

                        #1.6.5.3.Insertion sort
                        elif choose7==3:
                            print ("______________________Insertion sort__________________________________")
                            print (" ")
                            print ("Suppose an array A wuth n elements a[1],A[2],...,A[N} is in memory.The insertion sort algorithm scans A from A[1]to A[N],insertion each element A[K]into is proper position in the previousy sorted sub array A[1],A[2]...,A[K-1].")
                            print (" The following program ilustrate the sorting by Insertion sort")
                            n=input("Enter desired linear-list size(max. 50)..")
                            ar=[0]*n
                            print ("Enter element for the  linear list")
                            for i in range(n):
                                 ar[i]=input("Element"+str(i+1)+":")
                            print ("Original list is:",ar)
                            i_sort(ar)
                            print ("List after sorting:",ar)
                            line()
                        else :
                            print ("Invalid input!!!!")
                        del choose7

                    #1.6.6.Get back to previous menu
                    elif choose6==6:
                        con6=False
                    else:
                        print ("Invalid Input")

            #1.7.Stacks And queues            
            elif choose2==7:
                con8=True
                while con8:
                    print ("1.Stacks")
                    print ("2.Queues")
                    print ("3.Return to previous menu")
                    line()

                    #Stacks and queues selection
                    try:
                        choose7=int(input("Enter your choice(1-3)"))
                    except IOError:
                        print ("Input error")

                    #1.7.1.Stacks
                    if choose7==1:
                        print ("Python program to illustrate Stack operation")
                        ###############STACK IMPLEMENTAION ###################
                        ("""
                           Stack:implemented as a list
                           top:Topmost element in a stack
                        """)
                        stack=[]
                        top=None
                        co=1
                        while co==1:
                            print ("STACK OPERATIONS")
                            print ("1.Push")
                            print ("2.Pop")
                            print ("3.Peek")
                            print ("4.Display stack")
                            print ("5.Exit")
                            line()

                            #Stacks operation selection    
                            try:
                                ch=int(input("Enter your choice(1-5):"))
                            except IOError:
                                print ("Input error")

                            #1.7.1.1.Push
                            if ch==1:
                                try:
                                    item=input("Enter item:")
                                except IOError:
                                    print ("Input error")
                                push(stack,item)

                            #1.7.1.2.Pop
                            elif ch==2:
                                item=pop(stack)
                                if item=="Underflow":
                                    print ("Underflow! Stack is empty!")
                                else:
                                    print ("Popped item is",item)

                            #1.7.1.3.Peek
                            elif ch==3:
                                item=peek(stack)
                                if item=="Underflow":
                                    print ("Underflow! Stack is empty!")
                                    line()

                                else:
                                    print ("Topmost item is",item)

                            #1.7.1.4.Display
                            elif ch==4:
                                display(stack)

                            #1.7.1.5.Exit
                            elif ch==5:
                                co=0
                            else:
                                print ("Invalid INPUT")
                            
                            
                        else:
                            print("Invalid choice!")

                    #1.7.2.Queue
                    elif choose7==2:         
                        print ("Python program to illustrate queue operation")
                        ############### queue IMPLEMENTAION ###################
                        ("""
                           queue:implemented as a list
                           front:Integer having position if first (front most) element in a queue
                           rear: integer having position of last element in queue
                        """)
                        queue=[]
                        front=None
                        b=True

                        #Queue selection
                        while b:
                            print ("QUEUE OPERATIONS")
                            print ("1.Enqueue")
                            print ("2.Dequeue")
                            print ("3.Peek")
                            print ("4.Display queue")
                            print ("5.Exit")
                            line()
                            try:
                                ch=int(input("Enter your choice(1-5):"))
                            except IOError:
                                print ("Input error")

                            #1.7.2.1.Enqueue
                            if ch==1:
                                try:
                                    item=input("Enter item:")
                                except IOError:
                                    print ("Input error")
                                qu_enqueue(queue,item)
                                

                            #1.7.2.2.Dequeue
                            elif ch==2:
                                item=qu_dequeue(queue)
                                if item=="Underflow":
                                    print ("Underflow! Queue is empty!")
                                    line()
                                else:
                                    print ("Deueue-ed item is",item)
                                

                            #1.7.2.3.Peek
                            elif ch==3:
                                item=qu_peek(queue)
                                if item=="Underflow":
                                    print ("Underflow! Queue is empty!")
                                    line()
                                else:
                                    print ("Frontmost item is",item)
                                raw_input("Press Enter to continue...")

                            #1.7.2.4.Display
                            elif ch==4:
                                display(queue)
                                raw_input("Press Enter to continue...")

                            #1.7.2.5.Exit
                            elif ch==5:
                                 b=False


                            else:
                                print("Invalid choice!")
                                raw_input("Press Enter to continue...")

                    #1.7.3.Return to previous menu
                    elif choose7==3:
                        con8=False
                        del choose7,con8
                    else:
                        print ("Invalid Input")
                        del choose7,con8

            #1.8.Data File Handiling        
            elif choose2==8:
                con9=True
                while con9:
                    print ("___________________ DATA FILE HANDLING__________________")
                    print ("1. Opening and closing a file")
                    print ("2. Reading and Writting onto files")
                    print ("3. Return to previous menu")
                    line()

                    #Data file selection
                    try:
                        choose7=int(input("Enter your choice(1-3):"))
                    except IOError:
                        print ("Input error")

                    #1.8.1. Opening and closing
                    if choose7==1:
                        a=open("R_W.txt")
                        b=a.read(837)
                        print (b)
                        a.close()
                        del a,b

                    #1.8.2.Reading and writing 
                    elif choose7==2:
                        a=open("R_W.txt")
                        b=a.read(837)
                        c=a.read(1900)
                        print (c)
                        a.close()
                        del a,b,c
                        print (" ")
                        raw_input("Press Enter to continue...")
                        line()
                    #1.8.3..Get back to previous menu
                    elif choose7==3:
                        con9=False
                    else:
                        print ("Invalid input")
                    del choose7,con9

            #1.9.Exception handiling
            elif choose2==9:
                con10=True
                while con10:
                    print ("1.Exception Handiling")
                    print ("2.Generators")
                    print ("3.Return to previous menu")
                    line()

                    #Exception handiling selection
                    try:
                        choose7=int(input("Enter your choice(1-3)"))
                    except IOError:
                        print ("Input error")

                    #1.9.1.Exception handiling
                    if choose7==1:
                        a=open("ERROR.TXT")
                        b=a.read(2170)
                        print (b)
                        a.close()
                        del a,b
                        line()

                    #1.9.2.Generators
                    elif choose7==2:
                        a=open("ERROR.TXT")
                        b=a.read(2170)
                        c=a.read(9999)
                        print (c)
                        a.close()
                        del a,b,c
                        line()

                    #1.9.3.Return to previous menu
                    elif choose7==3:
                        con10=False
                    else:
                        print ("Invalid Input")

            #1.10.Get back to main menu
            elif choose2==10:
                con2=False
            else:
                print ("Invalid input!")

    #2.About python and project
    elif choose1==2:
        clean(2)
        a=open("ABOUT.txt")
        b=a.read()
        a.close()
        print (b)
        del a,b
        clean(2)
        print ("*****************************************************************")

    #3.
    elif choose1==3:
        con=False
        print ("Thank you for using program")
    else:
        print (" ")
        print (" INVALID INPUT !!!!")
        print (" ")
        print ("PROGRAM WILL RESTART")
        
        
