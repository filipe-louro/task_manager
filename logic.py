import tkinter as tk
from tkinter import messagebox


class Logic:
    def add_task(entry_task, listbox_tasks, button_add_item):
        task = entry_task.get()
        if task:
            listbox_tasks.insert(tk.END, task)
            entry_task.delete(0, tk.END)
            button_add_item.pack_forget()

    def delete_task(listbox_tasks, button_delete_item):
        try:
            selected_task_index = listbox_tasks.curselection()[0]
            listbox_tasks.delete(selected_task_index)
            if not listbox_tasks.curselection():
                button_delete_item.pack_forget()
        except IndexError:
            pass

    def show_edit_buttons(listbox_lists, button_edit_list, button_delete_list, button_add_item):
        if listbox_lists.curselection():
            button_edit_list.config(state=tk.NORMAL)
            button_delete_list.config(state=tk.NORMAL)
            button_add_item.config(state=tk.NORMAL)
        else:
            button_edit_list.config(state=tk.DISABLED)
            button_delete_list.config(state=tk.DISABLED)
            button_add_item.config(state=tk.DISABLED)

    def add_list(entry_list, listbox_lists, button_add_item, button_edit_list, button_delete_list):
        list_name = entry_list.get()
        if list_name:
            listbox_lists.insert(tk.END, list_name)
            entry_list.delete(0, tk.END)
            button_add_item.pack_forget()
            button_edit_list.pack()
            button_delete_list.pack()

    def delete_list(listbox_lists, listbox_tasks, button_edit_list, button_delete_list, button_add_item):
        try:
            selected_list_index = listbox_lists.curselection()[0]
            selected_list = listbox_lists.get(selected_list_index)

            confirmation = messagebox.askokcancel(
                "Confirmação", f"Tem certeza que deseja deletar a lista '{selected_list}'?")

            if confirmation:
                listbox_lists.delete(selected_list_index)
                listbox_tasks.delete(0, tk.END)
                button_edit_list.pack_forget()
                button_delete_list.pack_forget()
                button_add_item.pack_forget()

        except IndexError:
            pass

    def show_add_item_button(entry_task, button_add_item):
        if entry_task.get():
            button_add_item.pack()
        else:
            button_add_item.pack_forget()

    def show_tasks(listbox_lists, frame_lists, frame_tasks, label_list_title, button_back):
        selected_index = listbox_lists.curselection()
        if selected_index:
            selected_list = listbox_lists.get(selected_index)
            label_list_title.config(text=f"Tarefas de {selected_list}")
            frame_lists.pack_forget()
            frame_tasks.pack(side=tk.LEFT, padx=10, pady=10)
            button_back.pack(side=tk.BOTTOM)

    def go_back(frame_tasks, frame_lists, label_list_title, button_back):
        frame_tasks.pack_forget()
        frame_lists.pack(side=tk.LEFT, padx=10, pady=10)
        label_list_title.config(text="Listas de Tarefas")
        button_back.pack_forget()

    def edit_list(listbox_lists, listbox_tasks, selected_index, button_save_changes):
        if selected_index:
            selected_list = listbox_lists.get(selected_index)
            edit_window = tk.Toplevel()
            edit_window.title(f"Editar Lista - {selected_list}")

            edit_frame = tk.Frame(edit_window)
            edit_frame.pack(padx=20, pady=20)

            edit_label = tk.Label(edit_frame, text="Editar Lista:",
                                  font=("Helvetica", 14, "bold"))
            edit_label.pack()

            edit_list_name = tk.Entry(edit_frame, width=40)
            edit_list_name.insert(tk.END, selected_list)
            edit_list_name.pack(pady=10)

            edit_list_content = tk.Text(edit_frame, height=10, width=50)
            edit_list_content.pack(pady=10)

            for item in listbox_tasks.get(0, tk.END):
                edit_list_content.insert(tk.END, f"{item}\n")

            def save_changes():
                updated_list_name = edit_list_name.get()
                updated_list_content = edit_list_content.get(
                    "1.0", tk.END).strip().split("\n")
                listbox_lists.delete(selected_index)
                listbox_lists.insert(selected_index, updated_list_name)

                listbox_tasks.delete(0, tk.END)
                for item in updated_list_content:
                    listbox_tasks.insert(tk.END, item)

                edit_window.destroy()

            save_button = tk.Button(
                edit_frame, text="Salvar Alterações", command=save_changes)
            save_button.pack(pady=10)
