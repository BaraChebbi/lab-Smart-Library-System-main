# lab-Smart-Library-System-main
This is a lab-Smart-Library-System-main 
# Smart Library System

**Author:** Bara-Chebbi  
**Date:** April 17, 2025

## Overview

The Smart Library System is a small Library Management System built in Python. It leverages dictionaries to manage the library catalog and borrower records, sets to track the collection of books each borrower owns, and the `pickle` module for data persistence. This program simulates essential library operations such as borrowing and returning books, listing available books, displaying borrowers, and finding common books between two borrowers.

## Features

- **Borrow a Book:**  
  Allows a user to borrow a book if copies are available. The system checks for book availability and confirms whether the user already borrowed the book.

- **Return a Book:**  
  Provides functionality for a user to return a book, updating both the catalog and the borrower’s set of books.

- **List Available Books:**  
  Displays all books in the catalog with the number of copies available. Unavailable books are clearly indicated.

- **List Borrowers:**  
  Lists all registered borrowers along with the books they have currently borrowed.

- **Find Common Borrowed Books:**  
  Compares the books borrowed by two users and displays any titles that both have on loan.

- **Data Persistence with Pickle:**  
  Uses `pickle.dump()` to save the current state (library catalog and borrowers) to files and `pickle.load()` to restore the state on startup, ensuring data persists between sessions.

## How to Use

1. **Open on Google Colab:**  
   Upload the provided notebook or open the shared link to the Colab notebook.

2. **Run the Code:**  
   Execute the notebook cells sequentially. The program will initialize by attempting to load existing data using pickle. If no data files are found, it will start with the default catalog and borrowers.

3. **Interact via the Menu:**  
   The system runs an interactive menu in the console:
   - **Option 1:** Borrow a Book  
     Input your name and the title of the book you wish to borrow.
   - **Option 2:** Return a Book  
     Input your name and the title of the book to return it.
   - **Option 3:** List Available Books  
     See all books with the current number of copies available.
   - **Option 4:** List Borrowers  
     View a list of users and the books they have currently borrowed.
   - **Option 5:** Find Common Borrowed Books  
     Enter two borrower names to see if there are any books they both borrowed.
   - **Option 6:** Exit  
     Save the current data to file and gracefully exit the system.

## Code Structure

- **Import and Initialization:**  
  Imports the `pickle` module, initializes the `library_catalog` dictionary for book copies, and the `borrowers` dictionary (using sets) for borrowed books.

- **Primary Functions:**
  - `borrow_book(borrower_name, book_title)`: Manages borrowing operations.
  - `return_book(borrower_name, book_title)`: Handles the return of books.
  - `list_available_books()`: Displays the books available in the library.
  - `list_borrowers()`: Lists all current borrowers and their books.
  - `common_books(borrower1, borrower2)`: Finds and displays common books between two borrowers.
  - `save_data()` and `load_data()`: Use pickle to persist and restore the library catalog and borrowers.

- **Main Execution Loop:**  
  Provides a menu-driven interface to allow users to perform library operations until they choose to exit. Before exiting, it ensures all data is saved.

## Execution Results

Once executed, the Smart Library System provides a user-friendly console interface with clear prompts. The menu’s options enable testing of all functionalities, and successful execution will show messages confirming each operation (e.g., successful borrowing, returning, or data saving).

## Future Improvements

- **Enhanced Error Handling:**  
  More robust error checking and user feedback for invalid inputs.

- **Feature Expansion:**  
  Adding options for book reservations, overdue notifications, or even a graphical user interface (GUI) for a more interactive experience.

- **Extended Reporting:**  
  Detailed reports and statistics on borrowing trends and popular books.

Feel free to explore the code, offer improvements, or extend its functionality to meet additional library management needs.

## Conclusion

This project provides a clear, structured approach to simulating a library management system using Python’s built-in data structures and the pickle module. It’s an excellent foundation upon which more complex systems can be built.

---

*Enjoy managing your library with the Smart Library System!*
