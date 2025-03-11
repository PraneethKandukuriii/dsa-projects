class ToDoList:
    def __init__(self):
        self.stack = []

    def add_task(self,task):
        self.stack.append(task)
        print(f"Task : {task} Added.")
    
    def remove_task(self):
        if self.stack:
            removed_task = self.stack.pop()
            print(f"Removed Last Task.")
        else:
            print("No Tasks To Remove.")

    def view_tasks(self):
        if self.stack:
            print("Your TO-Do-List :\n")
            for i in range(len(self.stack)-1,-1,-1):
                print(f"{i+1}.{self.stack[i]}")
        else:
            print("Your To-Do-List Is Empty.")

    def mark_task(self,task):
        if task in self.stack:
            self.stack.remove(task)
            print(f"Task : {task} Marked As Completed and Removed")

        else:
            print("Task Not Found")


todo = ToDoList()

while True:
    print("\n1. Add Task\n2. Remove Last Task\n3. View Tasks\n4. Mark Task as Completed\n5. Exit")
    choice = input("Choose the option")

    if choice == '1':
        task = input("Enter Task:")
        todo.add_task(task)
    elif choice == '2':
        todo.remove_task()

    elif choice == '3':
        todo.view_tasks()
    
    elif choice == '4':
        task = input("Enter Task:")
        todo.mark_task(task)

    elif choice == '5':
        print("Exiting.....GoodByee!")
        break

    else:
        print("Invalid Choice...")





