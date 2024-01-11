import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def push_to_github():
    # Get the GitHub repository URL from the input field
    repo_url = repo_url_entry.get()

    # Get the GitHub personal access token from the input field
    github_token = token_entry.get()

    # Get the commit message from the input field
    commit_message = commit_entry.get()

    # Get the selected files to push
    selected_files = file_listbox.curselection()
    files_to_push = [file_listbox.get(index) for index in selected_files]

    # Get the local repository path from the input field
    repo_dir = repo_path_entry.get()

    # Change the current working directory to the repository directory
    os.chdir(repo_dir)

    # Add selected files, commit, and push changes to GitHub
    try:
        for file in files_to_push:
            subprocess.run(["git", "add", file])
        subprocess.run(["git", "commit", "-m", commit_message])
        subprocess.run(["git", "push", repo_url])
        status_label.config(text="Changes pushed to GitHub successfully!")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

def browse_files():
    selected_files = filedialog.askopenfilenames()
    for file in selected_files:
        file_listbox.insert(tk.END, file)

# Create the main window
root = tk.Tk()
root.title("GitHub Push GUI")

# Create an input field for the GitHub repository URL
repo_url_label = tk.Label(root, text="Enter your GitHub repository URL:")
repo_url_label.pack()

repo_url_entry = tk.Entry(root)
repo_url_entry.pack()

# Create an input field for the GitHub personal access token
token_label = tk.Label(root, text="Enter your GitHub token:")
token_label.pack()

token_entry = tk.Entry(root)
token_entry.pack()

# Create an input field for the commit message
commit_label = tk.Label(root, text="Enter commit message:")
commit_label.pack()

commit_entry = tk.Entry(root)
commit_entry.pack()

# Create a file selection button
select_files_button = tk.Button(root, text="Select Files to Push", command=browse_files)
select_files_button.pack()

# Create a listbox to display selected files
file_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
file_listbox.pack()

# Create an input field for the local repository path
repo_path_label = tk.Label(root, text="Enter local repository path:")
repo_path_label.pack()

repo_path_entry = tk.Entry(root)
repo_path_entry.pack()

# Create a push button
push_button = tk.Button(root, text="Push to GitHub", command=push_to_github)
push_button.pack()

# Create a label for status messages
status_label = tk.Label(root, text="")
status_label.pack()

# Start the GUI application
root.mainloop()
