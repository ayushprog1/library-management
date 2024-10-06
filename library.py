import time
print("                       welcome to central library                         ...")
time.sleep(1)
books=[]
available_book=[]
member=[]
borrow=[]
def main():
    print('''choose 1 for show all books
choose 2 for add/donate book 
choose 3 for add/remove member
choose 4 for enter name
choose 5 for show borrow book
choose 6 for exit''')
    global n
    n=int(input("enter choice: "))

    if n==1:
        print(books)
    elif n==2:
        addbooks()
    elif n==3:
        addrevmember()
    elif n==4:
        name()
    elif n==5:
        print("available books",available_book)
        print("borrow books",borrow)
    elif n==6:
        exit()
    else:
        print("please enter valid input")
    main()



def addrevmember():
    try:
        a=int(input("enter 1 for add and 2 for remove 3 to show all member : \n"))
        if a==1:
            name=input("enter name: ")
            member.append(name)
        elif a==2:
            name=input("enter name: ")
            member.remove(name)
        elif a==3:
            print(member)
        else:
            print("please enter valid input")
    except:
        print("please enter valid input")
    main()

def name():
    try:
        m=input("enter name: ")
        if m in member:
            c=int(input("enter 1 to borrow book ,2 for return book"))
            print("available_book: " ,available_book)
            if c==1: 
                b=input("enter book name: ")
                available_book.remove(b)
                d=f"{b} - {m}"
                borrow.append(d)
                print("book borrow successful")
            elif c==2:
                b=input("enter book name: ")
                available_book.append(b)
                d=f"{b} - {m}"
                borrow.remove(d)
                print("thank for using our library")
            else: 
                print("please enter valid input")
        else:
            print("please become our member first")
    except:
        print("please enter valid input")
    main()

def addbooks():
    try:
        a=int(input("enter no. of books: "))
        for i in range(a):
            book=input("enter book name: ")
            books.append(book)
            available_book.append(book)
        print("thanks for adding book")
    except:
        print("please enter valid input")
    main()

main()