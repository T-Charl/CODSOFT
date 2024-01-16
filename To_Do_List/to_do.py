from datetime import date
import csv

def help():
    print("""To-DO List Options:
Add - Add Task
Add Optionals:
  -Task Description
  -Task Due Date
        
Edit/Update - Edit Task
Delete - Delete Task
Complete - Mark Task as Completed""")


def open_csv():
    
    with open("To-DO list.csv", "w", newline='') as file:
        writer = csv.writer(file)
        headers = 'Time','Task', 'Description', 'Progress'
        writer.writerow(headers)


def add_task():
    with open("To-DO list.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(task_info())

            
# def update_task():
    

def display_task():
    with open("To-DO list.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for _ in list(reader)[1:]:
            print(_)


def task_info():
    task = input("What task would you like to add? ").strip()
    descrip = input("Task description... ").strip()
    time = input("Task time... ").strip()

    return time ,task, descrip 


def main():
    add_task()
    display_task()


display_task()

# if __name__ == "__main__":
#     main()