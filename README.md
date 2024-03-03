# hw2

Justin Quedit
CMSC 447
2/29/24

This CRUD application was created using Flask and Sqlite. It has simple functionality that allows a user to insert entries onto a table, delete them, and update them. They may also search for a user. 

This application is run by entering the command 'python myapp.py' in a terminal. To see the user interface, the link in terminal must be selected and will open the application in a browser. 

Things to note:
- I removed the database but the application will automatically create one when adding an entry on the user interface
- The ID is permanent and cannot be changed because it is the primary key in the table. Entries do not update automatically. After updating a text box, you need to click the update button corresponding to the entry.
- After searching for a user, you can go back to the full list of users by leaving the search box blank and clicking search
