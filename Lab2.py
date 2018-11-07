"""
Created on Tue Sep 11 20:07:50 2018
@author: Jaime A Hinojos
ID: 80590883
Date: 10/21/18
Lab2 version A
"""
class IDList(object): #creates object with the set ID and next pointer
    def __init__(self, data):
        self.iD = data
        self.nextID = None
class LinkedList(object): #creates the linked list and also has some integrated functions that do nt need recursion in order to be able to be executed.
    def __init__(self, r=None):
        self.root = r #IDList node reference
        self.sizeofList = 0 #helps identify the size of the total number of IDs
    def getNumberofId(self):
        return self.size
    def addId(self, d): #creates and new IDList object increments the size of the list and points the current object that was created to the last
        newId = IDList (d)
        self.sizeofList += 1
        if self.root is None:
            self.root = newId
            return
        last = self.root
        while last.nextID is not None:
            last = last.nextID
        last.nextID = newId
    def displayIdList(self):#prints the linked list without altering it just to verify if the operations performed do affect the linked list
        this_node = self.root
        while this_node:
            print(this_node.iD)
            this_node = this_node.nextID
    def linearDuplicate(self): #This method runs on O(n^2) and compares one node to the whole linked list and returns if there is a duplicate then it moves on to the next
        this_node = self.root
        count=0
        while this_node.nextID is not None:
            compare_node = this_node.nextID
            while compare_node.nextID is not None:
                if this_node.iD == compare_node.iD:
                    count += 1
                    print(this_node.iD+" is a duplicate")
                    break
                else:
                    compare_node = compare_node.nextID

            this_node = this_node.nextID
    def bubbleSort(self): #this method runs on O(n^2) and performs a bubble sort
        for i in range(self.sizeofList):
            other_node = self.root
            next_node = self.root.nextID
            prev_node = None #points to the previous node that comes before other_node to be able to link the list
            after_node = None #points to the node that comes after to be able to link the list
            if int(other_node.iD) > int(next_node.iD):
                temp = other_node
                other_node.nextID = next_node.nextID
                next_node.nextID = temp
                self.root = next_node
            prev_node = self.root
            other_node = prev_node.nextID
            next_node = other_node.nextID
            flag = 0
            for j in range(self.sizeofList-2):
                if int(other_node.iD) > int(next_node.iD):
                    after_node = next_node.nextID
                    prev_node.nextID = next_node
                    next_node.nextID = other_node
                    other_node.nextID = after_node
                    flag+=1
                prev_node = prev_node.nextID
                other_node = prev_node.nextID
                next_node = other_node.nextID
            if flag == 0:
                break
def createList(firstFile, SecondFile): #reads the files and stores each one in a list the two list are than joined together by creating a linked list
    listReturn = LinkedList()
    with open("activision.txt") as f:
        list = f.read().splitlines()
    with open("vivendi.txt") as f2:
        list2 = f2.read().splitlines()
    for i in range(len(list)):
        if list == None:
            break
        listReturn.addId(list[i])
    for j in range(len(list2)):
        if list2 == None:
            break
        listReturn.addId(list2[j])
    return listReturn
def mergeLists(list1, list2): #this method is in charge of sorting all the list that are passed on by the mergeSortist method, for it to later return one single sorted linked list
    temp = IDList(None)
    fake_head = temp
    if list1 is None:
        temp.nextID = list2
    elif list2 is None:
        temp.nextID = list1
    else:
        while list1 or list2 is not None:
            if list1 is None:
                temp.nextID = list2
                list2 = list2.nextID
            elif list2 is None:
                temp.nextID = list1
                list1 = list1.nextID
            elif int(list1.iD) <= int(list2.iD):
                temp.nextID = list1
                list1 = list1.nextID
            else:
                temp.nextID = list2
                list2 = list2.nextID
            temp = temp.nextID
        temp = fake_head.nextID
    return temp

def mergeSortList(head): #merge sort runs on O(nlog(n)) and is the most ideal but python doesn't really work with recursion so too many elements may exceed the limit of the amount of recursion calls that can be made
    if head is None:
        return None
    if head.nextID is None:#this method returns the final sorted list but it is in charge of calling the split function with every list that is returned and than calls the merge method to join everything together
        return head
    lefthalf, righthalf = listSplit(head)
    lefthalf = mergeSortList(lefthalf)
    righthalf = mergeSortList(righthalf)
    head = mergeLists(lefthalf, righthalf)
    return head
def listSplit(head): #method is in charge of returning the list split into two sections to later be split until there is only one node left
    if head is None or head.nextID is None:
        return
    slowpointer = head
    fastpointer = slowpointer.nextID
    while fastpointer is not None:
       fastpointer = fastpointer.nextID
       if fastpointer:
            fastpointer = fastpointer.nextID
            slowpointer = slowpointer.nextID
    middle = slowpointer.nextID
    slowpointer.nextID= None
    return head, middle
def booleanArray(myList): #runs on O(n) and first sets 2 arrays of size m+1 one array stores a default of 0 and the other of false
    boolean = [False]*(myList.sizeofList+1)
    numberCheck = [0]*(myList.sizeofList+1)
    temp = myList.root
    while temp is not None:
        numberCheck[int(temp.iD)] += 1 #increments the value at index(ID)
        if numberCheck[int(temp.iD)] == 2: # if the increment on the list is equal to 2 it will than set the boolean array at index(ID) to true to indicate that the value has been seen before.
           boolean[int(temp.iD)] = True
        temp = temp.nextID
    for i in range(len(boolean)):
        if boolean[i] == True:
            print(str(i)+" is duplicate")


def menu(myList): #interactive method for the user to use and perform the various actions that can be called.
    answer=""
    print("The linked list has been created what do you want to do?")
    while answer != "quit":
        print("1. Linear Duplicate Search")
        print("2. Bubble Sort List")
        print("3. Merge Sort List")
        print("4. Boolean Duplicate Search")
        print("5. Print List")
        print("6. Quit")
        print
        answer=str(input("What would you like to do? Enter number of Operation: "))
        if answer == "1":
            myList.linearDuplicate()
        elif answer == "2":
           myList.bubbleSort()
        elif answer == "3":
            myList.root = mergeSortList(myList.root)
        elif answer == "4":
            booleanArray(myList)
        elif answer == "5":
            myList.displayIdList()
        elif answer == "6":
            answer="quit"
        else:
            print("Invalid Input")
    print("Goodbye!")
    return

a = "activision.txt"
b = "vivendi.txt"
myList = createList(a, b)
menu(myList)
