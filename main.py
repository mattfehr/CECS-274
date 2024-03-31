import Calculator
import BookStore
import DLList




def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Check mathematical expression 
        2 Store variable values
        3 Print expression with values
        4 Evaluate Expression
        0 Return to main menu
        """)
        option = input()
        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        elif option =="2":
            cont = True
            while cont:
                variable = input("Enter a variable: ")
                value = input("Enter its value: ")
                calculator.set_variable(variable, value)
                answer = input("Enter another variable? Y/N ")
                if answer == "N":
                    cont = False
        elif option == "3":
            expression = input("Introduce the mathematical expression: ") 
            if calculator.matched_expression(expression):
                calculator.print_expression(expression)
            else:
                print("Invalid expression")
        elif option == "4":
            expression = input("Enter the expression: ")
            print_exp = calculator.print_expression(expression)
            error = False
            for value in print_exp:
                if value.isalpha():
                    error = True
                    print("Result: Error - Not all variable values are defined.")
                    break
            if error == False:
                print(f"Evaluating expression: {print_exp}")
                print(f"Result: {calculator.evaluate(expression)}")


        ''' 
        Add the menu options when needed
        '''


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best seller
        7 Add a book by key to shopping cart
        8 Add a book by title prefix to shopping cart
        9 Search best-sellers with infix
        10 Sort the catalog
        11 Display the first n books of catalog
        0 Return to main menu
        """)
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
            # bookStore.pathLength(0, 159811)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            cnt = int(input("Enter max number of results: "))
            bookStore.searchBookByInfix(infix, cnt)
        elif option == "6":
            bookStore.getCartBestSeller()
        elif option == "7":
            response = input("Enter book key: ")
            bookStore.addBookbyKey(response)
        elif option == "8":
            response = input("Introduce the prefix: ")
            title = bookStore.addBookByPrefix(response)
            if title != None:
                print(f"Added first matched title: {title}")
            else:
                print("Error: Prefix was not found.")
        elif option == "9":
            infix_9 = input("Enter infix: ")
            structure = int(input("Enter structure (1 or 2): "))
            max_titles_num = int(input("Enter max number of titles: "))
            bookStore.bestsellers_with(infix_9, structure, max_titles_num)  
        elif option == "10":
            print("""
            Choose an algorithm:
                1 - Merge Sort
                2 - Quick Sort (first element pivot)
                3 - Quick Sort (random element pivot)
            """)
            selection = input("Your selection: ")
            if bookStore.sort_catalog(selection) == False:
                print("Invalid algorithm")
        elif option == "11":
            number = int(input("Enter the number of books to display: "))
            bookStore.display_catalog(number)
           
        ''' 
        Add the menu options when needed
        '''


# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome test
        0 Exit/Quit
        """)
        option = input()

        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            p = DLList.DLList()
            word = input("Enter a word/phrase: ")
            for letter in word:
                if letter.isalnum():
                    p.add(0,letter.lower())
            if p.isPalindrome():
                print("Result: Palindrome")
            else:
                print("Result: Not a palindrome")


if __name__ == "__main__":
    main()
