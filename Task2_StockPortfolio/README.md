# Task 2 - Stock Portfolio Tracker

## Overview
This project is developed as part of the **CodeAlpha Python Programming Internship**.

The Stock Portfolio Tracker is a console-based Python application that calculates the total investment value based on a predefined stock price list. The user selects a stock and enters the quantity, and the program computes the total investment and saves the result to a file.

## Features
- Predefined stock price dictionary  
- User input for stock selection  
- Calculates total investment based on quantity  
- Validates stock name input  
- Displays detailed investment summary  
- Saves portfolio details to a text file (`portfolio.txt`)  
- Simple and interactive console-based interface  

## Programming Language
- Python 3

## Concepts Used
- Dictionaries  
- Conditional Statements (if-else)  
- User Input Handling  
- File Handling (open, write)  
- Arithmetic Operations  
- String Formatting  


## Project Structure

```bash
Task2_StockPortfolio/
│── main.py
│── README.md
│── portfolio.txt (generated after execution)
```

## How to Run
1. Ensure Python 3 is installed  
2. Open terminal or command prompt  
3. Navigate to the project folder  
4. Run the program:

```bash
python main.py
```

## How It Works

- A predefined dictionary stores stock names and prices
- User enters stock name (e.g., AAPL, TSLA)
- User enters quantity of shares
- Program calculates total investment value
- Output is displayed and saved into portfolio.txt

## Sample Output

```bash
========================================
     STOCK PORTFOLIO TRACKER
========================================

Enter stock name: TSLA
Enter quantity: 3

Stock: TSLA
Price per Share: $250
Quantity: 3
Total Investment: $750

Portfolio saved to portfolio.txt
```

## Author

**Yogashri R**

## Future Enhancements

- Support multiple stocks in a single portfolio
- Fetch real-time stock prices using financial APIs
- Export portfolio report as CSV/Excel file
- Develop GUI version using Tkinter or PyQt
