# 📚 Smart Library System
# Author: [Bara-Chebbi]
# Date: [April-17-2025]

# --- Import required modules ---
import pickle  # Import pickle module for saving and loading data

# --- Part 1: Initialize the library catalog ---
# Dictionary to store book titles and their available copies
library_catalog = {
    "Science Book": 5,  # 5 copies of Science Book available
    "Math Book": 3,  # 3 copies of Math Book available
    "History Book": 2  # 2 copies of History Book available
}

# --- Part 2: Initialize the borrowers dictionary ---
# Dictionary where keys are borrower names and values are sets of borrowed books
borrowers = {
    "Chiheb": {"Science Book"},  # Chiheb has borrowed Science Book
    "Abdo": {"Math Book"},  # Abdo has borrowed Math Book
    "Boba": {"History Book"}  # Boba has borrowed History Book
}

# --- Part 3: Borrowing a book function ---
def borrow_book(borrower_name, book_title):
    """
    Allows a user to borrow a book if available.
    Updates both library_catalog and borrowers dictionaries.
    """
    if book_title in library_catalog and library_catalog[book_title] > 0:  # Check if book exists and is available
        if borrower_name in borrowers and book_title in borrowers[borrower_name]:  # Check if borrower already has the book
            print(f"{borrower_name} already has {book_title}.")  # Inform user that they already borrowed it
            return  # Exit function

        library_catalog[book_title] -= 1  # Reduce available copies count

        if borrower_name not in borrowers:  # If borrower is not in dictionary
            borrowers[borrower_name] = set()  # Initialize empty set for borrowed books
        
        borrowers[borrower_name].add(book_title)  # Add book to borrower's record
        print(f"{borrower_name} has borrowed {book_title}.")  # Confirm successful borrowing
    else:
        print(f"Sorry, {book_title} is not available for borrowing.")  # Inform user if book is unavailable

# --- Part 4: Returning a book function ---
def return_book(borrower_name, book_title):
    """
    Allows a user to return a borrowed book.
    Updates both library_catalog and borrowers dictionaries.
    """
    if borrower_name in borrowers and book_title in borrowers[borrower_name]:  # Check if borrower has the book
        borrowers[borrower_name].remove(book_title)  # Remove book from borrower's record

        if not borrowers[borrower_name]:  # If borrower has no books left
            del borrowers[borrower_name]  # Remove borrower from dictionary

        library_catalog[book_title] += 1  # Increase available copies count
        print(f"{borrower_name} has returned {book_title}.")  # Confirm successful return
    else:
        print(f"{borrower_name} has not borrowed {book_title}.")  # Inform user if return request is invalid

# --- Part 5: Reporting functions ---
def list_available_books():
    """
    Displays all books with available copies.
    """
    print("Available Books:")
    for book, copies in library_catalog.items():  # Iterate through library catalog
        if copies > 0:
            print(f"- {book}: {copies} copies available.")  # Show books with remaining copies
        else:
            print(f"- {book}: Not available.")  # Show books that are currently unavailable

def list_borrowers():
    """
    Displays all borrowers and the books they currently have.
    """
    print("Current Borrowers:")
    for borrower, books in borrowers.items():  # Iterate through borrower records
        print(f"{borrower}: {', '.join(books) if books else 'No books borrowed'}")  # Display borrowed books or indicate none borrowed

def common_books(borrower1, borrower2):
    """
    Displays books borrowed by both borrower1 and borrower2.
    """
    if borrower1 in borrowers and borrower2 in borrowers:  # Check if both borrowers exist
        common = borrowers[borrower1] & borrowers[borrower2]  # Find common borrowed books
        print(f"\nCommon books borrowed by {borrower1} and {borrower2}: {', '.join(common) if common else 'None'}")  # Display result
    else:
        print("One or both borrowers do not exist.")  # Inform user if input names are incorrect

# --- Part 6: Saving data using pickle ---
def save_data():
    """
    Saves library_catalog and borrowers dictionaries to .pkl files.
    """
    with open('library_catalog.pkl', 'wb') as file:  # Open file for writing in binary mode
        pickle.dump(library_catalog, file)  # Save library catalog
    
    with open('borrowers.pkl', 'wb') as file:  # Open file for writing in binary mode
        pickle.dump(borrowers, file)  # Save borrower records
    
    print("Data saved successfully.")  # Confirm save operation

# --- Part 7: Loading data using pickle ---
def load_data():
    """
    Loads library_catalog and borrowers dictionaries from .pkl files if available.
    """
    global library_catalog, borrowers  # Ensure changes affect global variables

    try:
        with open("library_catalog.pkl", "rb") as file:  # Open file for reading in binary mode
            library_catalog = pickle.load(file)  # Load data into library catalog
    except FileNotFoundError:
        print("Library catalog file not found, starting with default catalog.")  # Handle missing file scenario

    try:
        with open("borrowers.pkl", "rb") as file:  # Open file for reading in binary mode
            borrowers = pickle.load(file)  # Load data into borrower records
    except FileNotFoundError:
        print("Borrowers file not found, starting with default borrowers.")  # Handle missing file scenario

# --- Main Program Execution ---
if __name__ == "__main__":  # Check if script is run directly
    load_data()  # Load saved data

    while True:  # Infinite loop for menu-based interaction
        print("\nLibrary Menu:")  # Display menu options
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List Available Books")
        print("4. List Borrowers")
        print("5. Find Common Borrowed Books")
        print("6. Exit")

        choice = input("Choose an option: ")  # Get user input for menu selection

        if choice == "1":
            name = input("Enter your name: ")  # Ask for borrower's name
            book = input("Enter book title: ")  # Ask for book title
            borrow_book(name, book)  # Call borrow function
        elif choice == "2":
            name = input("Enter your name: ")  # Ask for borrower's name
            book = input("Enter book title: ")  # Ask for book title
            return_book(name, book)  # Call return function
        elif choice == "3":
            list_available_books()  # Display available books
        elif choice == "4":
            list_borrowers()  # Display borrower list
        elif choice == "5":
            name1 = input("Enter first borrower name: ")  # Ask for first borrower name
            name2 = input("Enter second borrower name: ")  # Ask for second borrower name
            common_books(name1, name2)  # Find common books
        elif choice == "6":
            save_data()  # Save data before exiting
            print("Data saved. Goodbye!")  # Confirm save operation
            break  # Exit loop
        else:
            print("Invalid option. Please try again.")  # Handle invalid input