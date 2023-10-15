import tkinter as tk
from tkinter import ttk
from pathlib import Path

from optimization import search_file


def clear_inputs():
    search_entry.delete(0, tk.END)
    # show_files_var.set(False)
    # show_folders_var.set(False)
    extension_entry.delete(0, tk.END)
    # is_folder.set(False)
    result_listbox.delete(0)


def search_files_folders():
    search_term = search_entry.get()
    # show_files = show_files_var.get()
    # show_folders = show_folders_var.get()
    extension_filter = extension_entry.get()

    result_listbox.delete(0, tk.END)
    file_to_search = search_term + extension_filter

    result = Path(search_file(file_to_search))

    result_listbox.insert(tk.END, f"File: {result}")


root = tk.Tk()
root.title("File Manager")


search_frame = ttk.Frame(root)
search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

search_label = ttk.Label(search_frame, text="Search:")
search_label.grid(row=0, column=0, sticky="w")

search_entry = ttk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=1, padx=(10, 10))

# show_files_var = tk.BooleanVar()
# show_files_checkbox = ttk.Checkbutton(
#     search_frame, text="File", variable=show_files_var
# )
# show_files_checkbox.grid(row=0, column=2)

# show_folders_var = tk.BooleanVar()
# show_folders_checkbox = ttk.Checkbutton(
#     search_frame, text="Folder", variable=show_folders_var
# )
# show_folders_checkbox.grid(row=0, column=3)
# is_folder = tk.BooleanVar()
# is_folder_checkbox = ttk.Checkbutton(search_frame, text="Is Folder", variable=is_folder)
# is_folder_checkbox.grid(row=0, column=3, padx=(10, 10))

extension_label = ttk.Label(search_frame, text="Extension:")
extension_label.grid(row=0, column=4, padx=(10, 0))

extension_entry = ttk.Entry(search_frame, width=10)
extension_entry.grid(row=0, column=5)

search_button = ttk.Button(search_frame, text="Search", command=search_files_folders)
search_button.grid(row=0, column=6, padx=(10, 10))

result_listbox = tk.Listbox(root, width=80, height=20)
result_listbox.grid(row=1, column=0, padx=10, pady=10)

clear_button = ttk.Button(search_frame, text="Clear", command=clear_inputs)
clear_button.grid(row=0, column=7, padx=(10, 10))

root.mainloop()
