
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage

folder_mapping = {
    'Documents': ['.txt', '.doc', '.docx', '.pdf'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav'],
    'Spreadsheets': ['.xls', '.xlsx','.csv'],
    'Presentations': ['.ppt', '.pptx'],
    'Applications' : ['.exe'],
    'Database Files' : ['.sql','.iss'],
    'Html Files' :['.html'],
    'Python Files' :['.py','.ipynb']
}

def organize_files(directory):
    for folder in folder_mapping.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            for folder, extensions in folder_mapping.items():
                if file_extension in extensions:
                    destination_path = os.path.join(directory, folder, filename)
                    shutil.move(file_path, destination_path)
                    #print(f"Moved {filename} to {folder}")
                    break

def revert_file_organization(directory):
    subfolders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    for subfolder in subfolders:
        subfolder_path = os.path.join(directory, subfolder)
        for filename in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, filename)
            if os.path.isfile(file_path):
                destination_path = os.path.join(directory, filename)
                shutil.move(file_path, destination_path)
                #print(f"Moved {filename} back to the original directory")
    for subfolder in subfolders:
        subfolder_path = os.path.join(directory, subfolder)
        if not os.listdir(subfolder_path):
            os.rmdir(subfolder_path)
            #print(f"Removed empty subfolder {subfolder}")

class FileOrganizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Organizer")
        master.geometry("500x500")
        self.bg_image = tk.PhotoImage(file=r"imresizer-1721384273980.png")
        self.bg_label = tk.Label(master, image=self.bg_image)
        self.bg_label.place(relheight=1, relwidth=1)
        self.title_label = tk.Label(master, text="File Organizer",fg="Orange",font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)
        
        self.directory_label = tk.Label(master, text="Select a Folder:")
        self.directory_label.pack()

        self.directory_entry = tk.Entry(master, width=40)
        self.directory_entry.pack(pady=10)

        self.browse_button = tk.Button(master, text="Browse",bg="Blue",command=self.browse_directory)
        self.browse_button.pack(pady=10)

        self.organize_button = tk.Button(master, text="Organize Files",bg="Yellow",command=self.organize_files)
        self.organize_button.pack(pady=10)

        self.revert_button = tk.Button(master, text="Revert Files",bg="Cyan",command=self.revert_file_organization)
        self.revert_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Quit", bg="red",command=self.master.destroy)
        self.quit_button.pack(pady=10)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        self.directory_entry.delete(0, tk.END)
        self.directory_entry.insert(0, directory)

    def organize_files(self):
        directory = self.directory_entry.get()
        if os.path.isdir(directory):
            organize_files(directory)
            messagebox.showinfo("Success", "Files organized successfully!")
        else:
            messagebox.showerror("Error", "Invalid directory")

    def revert_file_organization(self):
        directory = self.directory_entry.get()
        if os.path.isdir(directory):
            revert_file_organization(directory)
            messagebox.showinfo("Success", "Files reverted successfully!")
        else:
            messagebox.showerror("Error", "Invalid directory")

root = tk.Tk()
my_gui = FileOrganizerGUI(root)
root.update()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Run the tkinter main loop
root.mainloop()