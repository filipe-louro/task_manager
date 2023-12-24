import tkinter as tk
from logic import Logic


class Gui:
    @staticmethod
    def create_gui():
        root = tk.Tk()
        root.title("Lista de Tarefas")

        frame_lists = tk.Frame(root)
        frame_lists.pack(side=tk.LEFT, padx=10, pady=10)

        frame_tasks = tk.Frame(root)

        listbox_lists = tk.Listbox(frame_lists, height=15, width=25, border=0)
        listbox_lists.pack(side=tk.TOP, fill=tk.BOTH)

        scrollbar_lists = tk.Scrollbar(frame_lists)
        scrollbar_lists.pack(side=tk.RIGHT, fill=tk.BOTH)

        listbox_lists.config(yscrollcommand=scrollbar_lists.set)
        scrollbar_lists.config(command=listbox_lists.yview)

        listbox_tasks = tk.Listbox(frame_tasks, height=15, width=50, border=0)
        listbox_tasks.pack(side=tk.TOP, fill=tk.BOTH)

        scrollbar_tasks = tk.Scrollbar(frame_tasks)
        scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

        listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
        scrollbar_tasks.config(command=listbox_tasks.yview)

        entry_list = tk.Entry(frame_lists, width=25)
        entry_list.pack(pady=5)

        button_add_list = tk.Button(
            frame_lists, text="Adicionar Lista", width=23, command=lambda: Logic.add_list(entry_list, listbox_lists, button_add_item, button_edit_list, button_delete_list), relief=tk.RAISED, font=("Helvetica", 10), bg="lightblue", fg="black")
        button_add_list.pack(pady=5)

        button_edit_list = tk.Button(
            frame_lists, text="Editar Lista", width=23, command=lambda: Logic.edit_list(listbox_lists, listbox_tasks, listbox_lists.curselection(), None), relief=tk.RAISED, font=("Helvetica", 10), bg="lightgreen", fg="black")
        button_edit_list.pack(pady=5)

        button_delete_list = tk.Button(
            frame_lists, text="Deletar Lista", width=23, command=lambda: Logic.delete_list(listbox_lists, listbox_tasks, button_edit_list, button_delete_list, button_add_item), relief=tk.RAISED, font=("Helvetica", 10), bg="salmon", fg="black")
        button_delete_list.pack(pady=5)

        button_add_item = tk.Button(
            frame_tasks, text="Adicionar Item", width=48, command=lambda: Logic.add_task(entry_task, listbox_tasks, button_add_item), relief=tk.RAISED, font=("Helvetica", 10), bg="lightblue", fg="black")
        button_add_item.pack()

        button_delete_item = tk.Button(
            frame_tasks, text="Deletar Item", width=48, command=lambda: Logic.delete_task(listbox_tasks, button_delete_item), relief=tk.RAISED, font=("Helvetica", 10), bg="salmon", fg="black")
        button_delete_item.pack()

        button_back = tk.Button(frame_tasks, text="Voltar", width=48,
                                command=lambda: Logic.go_back(frame_tasks, frame_lists, label_list_title, button_back), relief=tk.RAISED, font=("Helvetica", 10), bg="lightgrey", fg="black")
        button_back.pack()

        entry_task = tk.Entry(frame_tasks, width=50)
        entry_task.pack(pady=5)

        label_list_title = tk.Label(
            frame_tasks, text="Listas de Tarefas", font=("Helvetica", 14, "bold"))
        label_list_title.pack()

        listbox_lists.bind("<<ListboxSelect>>", lambda event: Logic.show_edit_buttons(
            listbox_lists, button_edit_list, button_delete_list, button_add_item))
        entry_task.bind("<KeyRelease>", lambda event: Logic.show_add_item_button(
            entry_task, button_add_item))
        listbox_lists.bind("<Double-Button-1>", lambda event: Logic.show_tasks(
            listbox_lists, frame_lists, frame_tasks, label_list_title, button_back))

        return root
