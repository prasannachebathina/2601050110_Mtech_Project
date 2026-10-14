# Library Book Recommendation and Reservation System

## 1. Project Description
The Library Book Recommendation and Reservation System is a simple Python-based application used to manage library books. It allows users to view available books, get book recommendations, reserve books, and return reserved books.

## 2. Objectives
- To display the list of library books.
- To recommend books to users.
- To reserve available books.
- To return reserved books.
- To maintain the availability status of books.

## 3. Technologies Used
- **Programming Language:** Python
- **Concepts:** Lists, Functions, Conditional Statements, Loops, Exception Handling
- **Platform:** Python IDLE, VS Code, or Google Colab

## 4. Features
1. **Show Books:** Displays all books with their availability status.
2. **Recommend Books:** Displays recommended books.
3. **Reserve Book:** Allows users to reserve an available book.
4. **Return Book:** Allows users to return a reserved book.
5. **Exit:** Terminates the application.

## 5. Book List
The system contains the following books:
- Python Programming
- Data Structures
- Machine Learning
- Artificial Intelligence
- Database Management

## 6. How to Run the Program
1. Install Python on your computer.
2. Save the Python code in a file named `library_system.py`.
3. Open a terminal or command prompt.
4. Navigate to the folder containing the file.
5. Execute the following command:

```bash
python library_system.py
```

## 7. Sample Output

```text
==============================
     LIBRARY BOOK SYSTEM
==============================
1. Show Books
2. Recommend Books
3. Reserve Book
4. Return Book
5. Exit

Enter your choice: 1

--- BOOKS ---
1. Python Programming - Available
2. Data Structures - Available
3. Machine Learning - Available
4. Artificial Intelligence - Available
5. Database Management - Available
```

## 8. Expected Results
The application successfully displays books, recommends selected books, reserves available books, and returns reserved books. It also handles invalid book numbers and repeated reservation or return requests.

## 9. Limitations
- Book information is stored in memory.
- Changes are lost when the program terminates.
- The program does not use a database or user login system.

## 10. Conclusion
The Library Book Recommendation and Reservation System demonstrates basic Python programming concepts through a practical library management application. It provides simple book listing, recommendation, reservation, and return operations.

---

# Python Multithreading Demonstration

## 1. Description
This program demonstrates multithreading in Python using the `threading` and `time` modules. Two threads execute the same task concurrently and print their progress.

## 2. Objective
To understand how multiple threads can execute tasks concurrently within a Python program.

## 3. Technologies Used
- **Programming Language:** Python
- **Modules:** `threading`, `time`
- **Concepts:** Threads, Concurrency, `start()`, `join()`

## 4. Working Principle
1. The `task()` function prints the thread name and iteration number.
2. Each thread executes five iterations.
3. `time.sleep(1)` pauses each thread for one second during each iteration.
4. Two thread objects are created.
5. The `start()` method starts both threads.
6. The `join()` method waits for both threads to complete.
7. The program prints a completion message.

## 5. How to Run the Program
Save the program as `thread_demo.py` and execute:

```bash
python thread_demo.py
```

## 6. Sample Output

```text
Thread 1 running 1
Thread 2 running 1
Thread 1 running 2
Thread 2 running 2
Thread 1 running 3
Thread 2 running 3
Thread 1 running 4
Thread 2 running 4
Thread 1 running 5
Thread 2 running 5
All threads completed!
```

**Note:** The exact order of the output may vary because both threads run concurrently.

## 7. Expected Results
The program creates two threads and allows them to execute the same task concurrently. It waits for both threads to finish before displaying the final completion message.

## 8. Advantages
- Supports concurrent task execution.
- Helps demonstrate thread creation and synchronization.
- Can improve responsiveness in suitable applications.

## 9. Conclusion
The Python Multithreading Demonstration explains the basic concepts of thread creation, execution, and synchronization using the `threading` module.

---

## Overall Conclusion
These programs demonstrate practical Python programming concepts. The library application focuses on book management and reservation, while the threading program demonstrates concurrent execution using multiple threads.
