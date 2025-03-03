import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def compress_image(input_path, output_path, quality=85):
    """Compress an image while maintaining high visual quality."""
    try:
        img = Image.open(input_path)
        img.save(output_path, optimize=True, quality=quality)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to compress image: {e}")
        return False

def select_file():
    """Open file dialog to select an image."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        entry_var.set(file_path)

def compress_and_save():
    """Handle compression and save the image."""
    input_path = entry_var.get()
    if not input_path:
        messagebox.showwarning("Warning", "Please select an image first!")
        return
    
    output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg")])
    if output_path:
        if compress_image(input_path, output_path):
            messagebox.showinfo("Success", "Image compressed and saved successfully!")

# GUI Setup
root = tk.Tk()
root.title("Photo Compressor")
root.geometry("400x200")

entry_var = tk.StringVar()

tk.Label(root, text="Select an image to compress:").pack(pady=10)

tk.Entry(root, textvariable=entry_var, width=40, state='readonly').pack(pady=5)

tk.Button(root, text="Browse", command=select_file).pack(pady=5)

tk.Button(root, text="Compress & Save", command=compress_and_save).pack(pady=10)

root.mainloop()
