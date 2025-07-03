import json
import os
from datetime import datetime


def main():
    

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
            "CreatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "UpdatedAt": None
            }
        data.append(task_to_add)

        print(f"\nTask added succesfully: (ID:{task_to_add["ID"]})\n")
        
        
        write_json(data)


    def delete_task(task_id_to_delete):
        data = read_json()
        data = [task for task in data if task.get("ID") != task_id_to_delete]

        print(f"Task deleted successfully (ID: {task_id_to_delete})")
        write_json(data)
    
    def update_task(task_id, new_task):
        try: 
            data = read_json()
        except:
            data = []
        for task in data:
            if task.get("ID") == task_id:
                task["Task"] = new_task
                task["UpdatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"Task updated succesfully (ID: {task_id})")
        write_json(data)

    def mark_task(task_id_to_mark, status):
        data = read_json()
        for task in data:
            if task.get("ID") == task_id_to_mark:
                task["Status"] = status

        print(f"Task marked succesfully (ID: {task_id_to_mark})")
        write_json(data)

    def list_tasks():
        data = read_json()
        for task in data:
            print(
                f"\nTask: {task["Task"]}\n"
                f"ID: {task["ID"]}\n"
                f"Status: {task["Status"]}"
            )
    def list_tasks_by_status(status):
        data = read_json()
        for task in data:
            if task["Status"] == status:
                print(
                    f"\nTask: {task["Task"]}\n"
                    f"ID: {task["ID"]}\n"
                    f"Status: {task["Status"]}"
                )





    # ---- CHECK COMMANDS HERE ---- # 

    def check_command(command):
        #.. if json file isn`t created we create it here so we don`t have to do it every time
        if not check_json("data.json"):
            create_json()

        

        if command.startswith("add"):
            new_task = command[4:]
            add_task(new_task)

        elif command.startswith("delete"):
            task_id_to_delete = int(command[7])
            delete_task(task_id_to_delete)

        elif command.startswith("update"):
            try:
                task_to_update = command[7:].split(maxsplit=1)
                task_id = int(task_to_update[0])
                new_task = task_to_update[1]
                update_task(task_id, new_task)
            except:
                print("Error, please to update a task do it like this: update 'ID' 'New task'")

        elif command.startswith("mark"):
            try:
                task_to_mark = command[4:].split(maxsplit=1)
                new_status = task_to_mark[0]
                task_id = int(task_to_mark[1])
                mark_task(task_id, new_status)
            except:
                print("Error, to mark a task do it like this: mark 'status' 'id'")


        elif command.startswith("list"):
            if len(command) == 4:
                list_tasks()
            else:
                try:
                    status = command[4:].strip()
                    print(status)
                    list_tasks_by_status(status)
                except:
                    print("Error, to list by status do it like this: list 'to-do'...")


        elif command == "0":
            print("Bye!")
            return False

        return True
    


    #.. read input arguments from the user
    command = input("--> ").strip()
    return check_command(command)






if __name__ == "__main__":
    while True:
        if not main():
            break