import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import ImageSequenceClip

def create_gif(image_folder, gif_path, fps=10):
    try:
        # Validate image folder
        if not os.path.isdir(image_folder):
            raise ValueError("Invalid image folder path.")

        # Get list of image files in the folder
        image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

        # Check if there are images to process
        if not image_files:
            raise ValueError("No image files found in the folder.")

        # Sort the image files by their names
        image_files.sort()

        # Load images into ImageSequenceClip
        clip = ImageSequenceClip([os.path.join(image_folder, f) for f in image_files], fps=fps)

        # Write the clip to a GIF file
        clip.write_gif(gif_path, verbose=False, progress_bar=False)

        result_label.config(text=f"GIF created successfully: {gif_path}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

def select_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def create_gif_button_click():
    folder_path = folder_entry.get()
    file_path = file_entry.get()
    create_gif(folder_path, file_path)

# Create the main window
root = tk.Tk()
root.title("Image to GIF Converter")

# Create and layout GUI components
folder_label = tk.Label(root, text="Image Folder:")
folder_label.grid(row=0, column=0)

folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1)

folder_button = tk.Button(root, text="Select Folder", command=select_folder)
folder_button.grid(row=0, column=2)

file_label = tk.Label(root, text="Save as:")
file_label.grid(row=1, column=0)

file_entry = tk.Entry(root, width=50)
file_entry.grid(row=1, column=1)

file_button = tk.Button(root, text="Select File", command=select_file)
file_button.grid(row=1, column=2)

create_button = tk.Button(root, text="Create GIF", command=create_gif_button_click)
create_button.grid(row=2, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3)

# Start the Tkinter event loop
root.mainloop()