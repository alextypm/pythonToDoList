from tkinter import *

root = Tk()
root.title("Saiyajin-To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []  # List to store tasks

def add_task():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:  # Check if task is not empty
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"{task}\n")  # Write task to file
        task_list.append(task)  # Add task to task_list
        listbox.insert(END, task)  # Insert task into listbox

def delete_task():
    global task_list
    task = str(listbox.get(ANCHOR))  # Get selected task from listbox
    if task in task_list:
        task_list.remove(task)  # Remove from task list
        with open("tasklist.txt", "w") as taskfile:  # Rewrite tasklist to file
            for task in task_list:
                taskfile.write(f"{task}\n")  # Write each task to file
        listbox.delete(ANCHOR)  # Delete selected task from listbox

def open_task_file():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task.strip():  # Skip empty lines
                task_list.append(task.strip())  # Append task to task_list
                listbox.insert(END, task.strip())  # Insert task into listbox
    except FileNotFoundError:
        with open("tasklist.txt", "w"):  # Create file if it doesn't exist
            pass

# Icon for the window
image_icon = PhotoImage(file="./image/task.png")
root.iconphoto(False, image_icon)

# Top bar
top_image = PhotoImage(file="./image/topbar.png")
Label(root, image=top_image).pack()

dock_image = PhotoImage(file="image/dock.png")
Label(root, image=dock_image, bg="#32405b").place(x=30, y=25)

note_image = PhotoImage(file="image/task.png")
Label(root, image=note_image, bg="#32405b").place(x=340, y=25)

heading = Label(root, text="All TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Main frame for task input
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

# Add Button
button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=add_task)
button.place(x=300, y=0)

# Listbox to display tasks
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=("arial", 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Delete Button
delete_icon = PhotoImage(file="image/delete.png")
Button(root, image=delete_icon, bd=0, command=delete_task).pack(side=BOTTOM, pady=13)

# Open tasks from file on start
open_task_file()

root.mainloop()
