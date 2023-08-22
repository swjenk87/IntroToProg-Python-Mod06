# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SJenkins,2023-08-19,Initial testing, adding functionality
# SJenkins,2023-08-21,Completed remaining coding to complete Assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection

# Additional variables added to enhance functionality.
str_warning = "Warning: Your To Do List Doesn't Exist!" # Create a warning message and check if it is being used



# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """

        try:
            list_of_rows.clear()  # clear current data
            file = open(file_name, "r")
            for line in file:
                task, priority = line.split(",")
                row = {"Task": task.strip(), "Priority": priority.strip()}
                list_of_rows.append(row)
            file.close()

        except:
            print(str_warning)
            print("Creating One for You Now!\n")
            file = open(file_name, "w")
            file.close()
            print("Your To Do List is Created and Ready to Modify!")

        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want to add more data to:
        :return: (list) of dictionary rows
        """
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        # TODO: Add Code Here!
        print("You Entered:", task, "with a Priority of", priority)
        print("-" * 50)
        list_of_rows.append(row)
        print("You're Task has been Added! Remember to Save Before Exiting!\n")

        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!

        # Indicate which Task to remove
        bln_item_removed = False  # Use this to verify that the data was found and removed
        for row in list_of_rows:
            rm_task, rm_priority = dict(row).values()
            if(rm_task == task):
                list_of_rows.remove(row)
                bln_item_removed = True

        # Update user on the status
        if bln_item_removed == True:
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        # Check if user wants to see the data one more time before saving to file.
        disp_data = input("Do you wish to see your list before saving?: ")
        if(disp_data.lower() == "y"):
            print("Currently Your Tasks Are: \n")
            for row in list_of_rows:
                print(row["Task"] + " (" + row["Priority"] + ")")
            print("-" * 50)

        # Save Table to text file.
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        file.close()
        input("Your tasks have been saved to your To Do List! Hit [Enter] to go back to the main menu.")

        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        if(list_of_rows != []):
            for row in list_of_rows:
                print(row["Task"] + " (" + row["Priority"] + ")")
        else:
            print("\tYou have no tasks in your ToDo List")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def continue_task_revisions():
        """ Ask the user a yes/no question to continue revisions

        :return: (yes_no_choice) - Yes to continue, no to end
        """
        # Ask the user if they want to add more data before taking them back to the menu.
        str_con_data = str(input("Do you want to do more revisions? (y/n): "))
        if (str_con_data .lower() == "y"):
            print("\n")
            yes_no_choice = True

        elif (str_con_data .lower() == "n"):
            print("\n")
            yes_no_choice = False

        return yes_no_choice

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (strTask, strPriority) with task and priority
        """
        # TODO: Add Code Here!
        # Confirming the user's choice to add a new task to the To Do List.
        print("You've Chosen to Add a New Task!")

        # Modify the strTask variable with a user input, check if "exit" was entered.
        str_task = input("Type a New Task (or Exit for the Menu): ")

        # Check for exit criteria
        if(str_task.lower() == "exit"):  # Exit criteria
            return

        # Modify the strPriority variable with a user input, check if "exit" was entered.
        str_priority = input("Type the Task's Estimated Priority[High/Medium/Low] (or Exit for the Menu): ")

        # Check for exit criteria
        if(str_priority.lower() == "exit"):  # Exit criteria
            return

        return str_task, str_priority

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        # TODO: Add Code Here!
        # Letting the user know they have chosen to remove items and to follow the prompts.
        print("Follow the instructions below to remove a To Do List item!")

        # Indicate which Task to remove
        str_remove_task = input("Which Task Would you Like to Remove?: ")

        return str_remove_task


# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        # Sets initial state to true
        add_user_choice = True

        # Loops as long as the user opts to keep adding items, via a y/n choice below.
        while(add_user_choice != False):
            task, priority = IO.input_new_task_and_priority()
            table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)

            # Determine if the user wishes to continue revising the list
            add_user_choice = IO.continue_task_revisions()

            continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        # Sets initial state to true
        remove_user_choice = True

        # Loops as long as the user opts to keep removing items, via a y/n choice below.
        while(remove_user_choice != False):
            task = IO.input_task_to_remove()
            table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)

            # Determine if the user wishes to continue revising the list
            remove_user_choice = IO.continue_task_revisions()

        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor .write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop
