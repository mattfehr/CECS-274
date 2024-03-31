import Book
import ArrayList
'''
import ArrayQueue
import RandomQueue
'''
import DLList
import SLLQueue
import MaxQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import algorithms
'''
import AdjacencyList
'''
import time


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = ArrayList.ArrayList() #DLList.DLList()
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                #self.bookIndices.add(s.key, self.bookCatalog.size()-1)
                self.sortedTitleIndices.add(s.title, self.bookCatalog.size()-1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")


    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str, cnt: int):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        count = 0
        for book in self.bookCatalog:
            if infix in book.title:
                print(book)
                count+= 1
                if cnt == count:
                    break
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        print("getCartBestSeller returned")
        best_seller = self.shoppingCart.max()
        print("Result:", best_seller.title)

    def addBookbyKey(self, key):
        start_time = time.time()
        book_index = self.bookIndices.find(key)
        if book_index != None:
            book = self.bookCatalog.get(book_index)
            self.shoppingCart.add(book)
            print("Added title: ", book.title)
        else:
            print("Book not found.")
        elapsed_time = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def addBookByPrefix(self, prefix):
        if prefix != "":
            book_index = self.sortedTitleIndices.find_smallest(prefix).v
            if book_index != None:
                book = self.bookCatalog.get(book_index)
                if book.title >= prefix:
                    if book.title[:len(prefix)] == prefix:
                        self.shoppingCart.add(book)
                        return book.title
        return None
    
    def bestsellers_with(self, infix, structure, n = 0) :
        best_sellers = None
        if structure == 1:
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure.")
        if best_sellers is not None:
            if infix == "":
                print("Invalid infix.")
            else:
                start_time = time.time()
                # FIXME: Insert the rest of the implementation here 
                if structure == 1:
                    for book in self.bookCatalog:
                        if infix in book.title:
                            best_sellers.add(book.rank, book)
                    books = best_sellers.in_order()
                    books = books[::-1]
                    if n == 0:
                        for book in books:
                            print(book.v)
                    else:
                        count = 0 
                        while count != n:
                            print(books[count].v)
                            count += 1
                if structure == 2:
                    for book in self.bookCatalog:
                        if infix in book.title:
                            best_sellers.add(book.rank*-1)
                    ranks = []
                    for rank in range(best_sellers.size()):
                        ranks.append(best_sellers.remove()*-1)
                    books = []
                    for rank in ranks:
                        for book in self.bookCatalog:
                            if book.rank == rank:
                                books.append(book)   
                    if n == 0:
                        for book in books:
                            print(book)
                    else:
                        count = 0 
                        while count != n:
                            print(books[count])
                            count += 1                 
                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")

    def sort_catalog(self, s):
        start_time = time.time()
        if s == "1":
            algorithms.merge_sort(self.bookCatalog)
            elapsed_time = time.time() - start_time
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
            return True
        elif s == "2":
            algorithms.quick_sort(self.bookCatalog, False)
            elapsed_time = time.time() - start_time
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
            return True
        elif s == "3":
            algorithms.quick_sort(self.bookCatalog, True)
            elapsed_time = time.time() - start_time
            print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")
            return True
        else:
            return False
        
    def display_catalog(self, n):
        count = 0
        while count != n:
            print(self.bookCatalog[count])
            count += 1