from tkinter import Tk, filedialog, Listbox, Button, Label, Scrollbar, END, Text, Frame
from PIL import Image, ImageTk
import os
import pyperclip

class MetadataViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("PNG Metadata Viewer")
        self.root.geometry("800x600")
        
        # Colors for dark mode
        self.bg_color = "#222222"  # Dark background
        self.text_color = "#DDDDDD"  # Light text
        self.highlight_color = "#444444"  # Slightly lighter for highlights
        
        # Set dark mode styling for root window
        self.root.config(bg=self.bg_color)

        # Set up frames for layout
        self.left_frame = Frame(root, bg=self.bg_color)
        self.left_frame.pack(side="left", fill="both", expand=True)

        self.right_frame = Frame(root, bg=self.bg_color)
        self.right_frame.pack(side="right", fill="y")

        # Left frame for displaying image and metadata
        self.image_label = Label(self.left_frame, bg=self.bg_color)
        self.image_label.pack(pady=10)

        self.metadata_text = Text(self.left_frame, wrap="word", height=10, state="disabled",
                                  bg=self.bg_color, fg=self.text_color, insertbackground=self.text_color)
        self.metadata_text.pack(expand=True, fill="both", pady=(5, 10))

        # Right frame for file list and directory selection
        self.select_dir_button = Button(self.right_frame, text="Select Directory", command=self.select_directory,
                                        bg=self.highlight_color, fg=self.text_color, activebackground=self.bg_color,
                                        activeforeground=self.text_color)
        self.select_dir_button.pack(pady=10)

        self.file_listbox = Listbox(self.right_frame, width=30, height=25, bg=self.bg_color, fg=self.text_color,
                                    selectbackground=self.highlight_color, selectforeground=self.text_color)
        self.file_listbox.pack(side="left", fill="y")
        self.file_listbox.bind('<<ListboxSelect>>', self.on_select)

        self.scrollbar = Scrollbar(self.right_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.file_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.file_listbox.yview)

        # Navigation controls
        self.root.bind("<Left>", self.previous_image)
        self.root.bind("<Right>", self.next_image)
        
        # Variable to store current image index
        self.current_index = -1
        self.image_files = []

    def select_directory(self):
        # Select directory and populate the listbox with PNG files
        directory = filedialog.askdirectory()
        if directory:
            self.image_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith('.png')]
            self.file_listbox.delete(0, END)
            for file in self.image_files:
                self.file_listbox.insert(END, os.path.basename(file))
            self.current_index = 0
            self.display_image_metadata(self.current_index)

    def display_image_metadata(self, index):
        # Display the image and metadata for the given index
        if 0 <= index < len(self.image_files):
            selected_file = self.image_files[index]
            metadata = self.extract_metadata(selected_file)
            self.show_image(selected_file)
            self.show_metadata(metadata)

    def on_select(self, event):
        # Update the display when a new item is selected from the list
        selection = self.file_listbox.curselection()
        if selection:
            self.current_index = selection[0]
            self.display_image_metadata(self.current_index)

    def extract_metadata(self, image_path):
        # Extract metadata from the selected PNG file
        try:
            with Image.open(image_path) as img:
                metadata = img.info.get("parameters", "No metadata found")
                return metadata
        except Exception as e:
            print(f"Error reading metadata from {image_path}: {e}")
            return "Error reading metadata"

    def show_image(self, filename):
        # Display downscaled image (25% of the original size)
        try:
            img = Image.open(filename)
            new_size = (int(img.width * 0.5), int(img.height * 0.5))
            img.thumbnail(new_size, Image.ANTIALIAS)
            img_thumbnail = ImageTk.PhotoImage(img)

            # Update the image label
            self.image_label.config(image=img_thumbnail)
            self.image_label.image = img_thumbnail  # Keep a reference to avoid garbage collection
        except Exception as e:
            print(f"Error displaying image thumbnail: {e}")

    def show_metadata(self, metadata):
        # Display metadata in the text widget
        self.metadata_text.config(state="normal")
        self.metadata_text.delete("1.0", END)
        self.metadata_text.insert("1.0", metadata)
        self.metadata_text.config(state="disabled")

    def next_image(self, event=None):
        # Display the next image and metadata
        if self.current_index < len(self.image_files) - 1:
            self.current_index += 1
            self.display_image_metadata(self.current_index)
            self.file_listbox.selection_clear(0, END)
            self.file_listbox.selection_set(self.current_index)
            self.file_listbox.activate(self.current_index)

    def previous_image(self, event=None):
        # Display the previous image and metadata
        if self.current_index > 0:
            self.current_index -= 1
            self.display_image_metadata(self.current_index)
            self.file_listbox.selection_clear(0, END)
            self.file_listbox.selection_set(self.current_index)
            self.file_listbox.activate(self.current_index)

    def copy_metadata(self):
        # Copy metadata to the clipboard
        if self.current_metadata:
            pyperclip.copy(self.current_metadata)
            print("Metadata copied to clipboard.")

if __name__ == "__main__":
    root = Tk()
    app = MetadataViewer(root)
    root.mainloop()
 
