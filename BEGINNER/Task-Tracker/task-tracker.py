import json
import os


def main():
    #.. MENU
    def create_menu():
        print("\nMENU: ")
        print("-Add task -> 1")
        print("-Delete task -> 2")
        print("-Update task -> 3")
        print("-Mark status (in-progress/done) -> 4")
        print("-List all tasks by status -> 5")
        print("0 -> Exit")

    create_menu()

    def check_json(name):
        return os.path.isfile(name)
    
    def create_json():
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

    def write_json(data):
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
    
    def read_json():
        try:
            with open("data.json" ,"r") as f:
                content = f.read().strip()
                if not content: 
                    data = []
                else: 
                    data = json.loads(content)
        except:
            print("Error")
        return data


    def add_task(new_task):
        data = read_json()
        id = len(data) + 1

        if data:
            for task in data:
                if task["ID"] == id: #.. we need to check so tasks doesnt share ids
                    id += 1
        
        task_to_add = {
            "Task": new_task, 
            "ID": id,
            "Description": None,
            "Status": None,
            "CreatedAt": None,
            "UpdatedAt": None
            }
        data.append(task_to_add)

        print(f"\nTask added succesfully: (ID:{task_to_add["ID"]})\n")
        
        
        write_json(data)


    def delete_task(task_to_delete):
        data = read_json()
        data = [task for task in data if task.get("Task") != task_to_delete]

        write_json(data)
    
    def update_task(task_to_update, new_task):
        try: 
            with open("data.json", "r") as f:
                tasks = json.load(f)
        except:
            tasks = []
        for task in tasks:
            if task.get("Task") == task_to_update:
                task["Task"] = new_task
        with open("data.json", "w") as f:
            json.dump(tasks, f, indent=4)

    def mark_task(task_to_mark, status):
        data = read_json()
        for task in data:
            if task.get("Task").lower() == task_to_mark.lower():
                task["Status"] = status

        write_json(data)

    def list_tasks():
        data = read_json()
        for task in data:
            print(
                f"\nTask: {task["Task"]}\n"
                f"ID: {task["ID"]}\n"
                f"Status: {task["Status"]}\n"
            )





    # ---- CHECK OPTIONS HERE ---- # 

    def check_option(op):
        #.. if json file isn`t created we create it here so we don`t have to do it every time
        if not check_json("data.json"):
            create_json()

        if op == 1:
            new_task = input("Enter the task you want to add to your tracker: ")
            add_task(new_task)


        elif op == 2:
            task_to_delete = input("Enter the task you want to delete: ")
            delete_task(task_to_delete)
        elif op == 3:
            task_to_update = input("Enter the task you want to update: ")
            new_task = input("Which is the new task?\n")
            update_task(task_to_update, new_task)

        elif op == 4:
            task_to_mark = input("Task to mark: ")
            status = input("To do, done or in-progress: ")
            mark_task(task_to_mark, status)

        elif op == 5:
            list_tasks()


        elif op == 0:
            print("Bye!")
            return False

        return True
    


    #.. read input arguments from the user
    option = int(input("\nWhat do you want to do?\n"))
    return check_option(option)






if __name__ == "__main__":
    while True:
        if not main():
            break