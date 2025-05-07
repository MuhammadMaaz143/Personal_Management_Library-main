import json  # Import the JSON library to work with JSON files
# The json library is used to save and load the library data: 
# It serializes the data (books) into JSON format 
# and saves it to a file, or it deserializes the data from 
# JSON format to a Python dictionary when loading it from the file.

# JSON is a simple, human-readable format that allows for easy storage 
# and retrieval of data in a text file, and it is cross-platform compatible.


import os   # Import the OS library to check if files exist, 
            # It's commonly used when you need to check file existence, create 
            # or remove files and directories, and perform system commands.

# Path to the file where library data is saved
data_file = 'library.text'

# Function to load library data from a file
def load_library():
    if os.path.exists(data_file):  # Check if the file exists
        with open(data_file, 'r') as file:  # Open the file in read mode
            return json.load(file)  # Load the file data as a JSON (dictionary) and return it
    else:
        return {}  # If file doesn't exist, return an empty dictionary

# Function to save library data to the file
def save_library(library):
    with open(data_file, 'w') as file:  # Open the file in write mode
        json.dump(library, file)  # Convert the dictionary (library) into JSON format and save it

# Function to add a new book to the library
def add_book(library):
    title = input('Enter the title: ')  # Ask the user to enter the book title
    author = input('Enter the author: ')  # Ask the user to enter the book author
    year = input('Enter the year: ')  # Ask the user to enter the year the book was published
    genre = input('Enter the genre: ')  # Ask the user to enter the book's genre
    read = input('Have you read the book? (yes/no): ').lower() == 'yes'  # Ask if the user has read the book, converting the answer to a boolean
    
    # Create a dictionary for the new book with its details
    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    
    # Add the new book to the library using the title as the key
    library[title] = new_book
    save_library(library)  # Save the updated library to the file
    print(f'Book {title} has been added to the library.')  # Confirm that the book has been added

# Function to remove a book from the library
def remove_book(library):
    title = input('Enter the title of the book you want to remove: ')  # Ask the user for the book title to remove
    
    if title in library:  # If the book exists in the library
        del library[title]  # Remove the book from the dictionary by its title
        save_library(library)  # Save the updated library to the file
        print(f'Book {title} has been removed from the library.')  # Confirm the removal
    else:
        print(f'Book {title} was not found in the library.')  # If the book is not found, inform the user

# Function to search for books by title or author
def search_library(library):
    search_by = input('Search by title or author: ').lower()  # Ask the user if they want to search by title or author
    search_term = input(f'Enter the {search_by}: ').lower()  # Ask the user to enter the search term (title or author)

    # Ensure the search is only by 'title' or 'author' fields
    if search_by not in ['title', 'author']:
        print("Invalid search option. Please search by 'title' or 'author'.")
        return

    # Find books where the search term matches either the title or author
    results = [book for book in library.values() if search_term in book[search_by].lower()]
    
    if results:  # If there are any results
        for book in results:
            status = 'read' if book['read'] else 'unread'  # Determine if the book has been read
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")  # Print book details
    else:
        print(f'No books found for "{search_term}" in the {search_by} field.')  # If no matches are found, inform the user

# Function to display all books in the library
def display_all_books(library):
    if library:  # If the library is not empty
        for book in library.values():  # Loop through each book in the library
            status = 'read' if book['read'] else 'unread'  # Check if the book has been read
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")  # Print book details
    else:
        print('Library is empty')  # If the library is empty, inform the user

# Function to display statistics about the library
def display_statistics(library):
    total_books = len(library)  # Count the total number of books in the library
    total_read = sum(1 for book in library.values() if book["read"])  # Count how many books have been read
    total_unread = total_books - total_read  # Calculate how many books are unread
    percentage_read = (total_read / total_books) * 100 if total_books > 0 else 0  # Calculate the percentage of read books

    # Print the statistics
    print(f'Total books: {total_books}')
    print(f'Total read: {total_read}')
    print(f'Total unread: {total_unread}')
    print(f'Percentage read: {percentage_read:.2f}%')  # Show percentage with two decimal points

# Main function that runs the program
def main():
    library = load_library()  # Load the library data from the file when the program starts
    
    while True:  # Keep the program running until the user chooses to exit
        # print("Menu")  # Display menu options
        # print("1. Add a book")
        # print("2. Remove a book")
        # print("3. Search the library")
        # print("4. Display all books")
        # print("5. Display statistics")
        # print("6. Exit")

        # Display the menu options using
        #  The triple quotes (''' or """) allow you to create a string that spans multiple lines 
        # without needing to use escape characters like \n for newlines.
        print('''Welcome to the library system. 
            1. Add a new book
            2. Remove a book
            3. Search the library
            4. Display all books
            5. View statistics
            6. Exit
            ''')

        choice = input('Enter your choice: ')  # Get the user's choice
        
        if choice == '1':
            add_book(library)  # Call function to add a book
        elif choice == '2':
            remove_book(library)  # Call function to remove a book
        elif choice == '3':
            search_library(library)  # Call function to search for books
        elif choice == '4':
            display_all_books(library)  # Call function to display all books
        elif choice == '5':
            display_statistics(library)  # Call function to display statistics
        elif choice == '6':
            break  # Exit the program if the user chooses to exit
        else:
            print('Invalid choice. Please try again.')  # If the user enters an invalid option


# Check if the script is being run directly by the user
if __name__ == '__main__':
    main()  # Run the main function to start the program