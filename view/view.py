import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def create_ui():
    root = tk.Tk()
    root.title("Custom UI")

    # Load the image
    img = Image.open("img.png")
    img = img.resize((100, 100))  # Resize the image to fit the labels
    photo = ImageTk.PhotoImage(img)

    # Main frame
    main_frame = ttk.Frame(root, padding=10)
    main_frame.grid(row=0, column=0, sticky="nsew")

    # Left large image
    left_image = tk.Label(main_frame, image=photo)
    left_image.image = photo  # Keep a reference to the image
    left_image.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=5, pady=5)

    # Top middle text
    top_text = tk.Label(main_frame, text="文字", background="light blue")
    top_text.grid(row=0, column=1, columnspan=4, sticky="nsew", padx=5, pady=5)

    # Middle images
    for i in range(4):
        img_label = tk.Label(main_frame, image=photo)
        img_label.image = photo  # Keep a reference to the image
        img_label.grid(row=1, column=1 + i, sticky="nsew", padx=5, pady=5)

    # Bottom text
    bottom_text = tk.Label(main_frame, text="文字", background="light blue")
    bottom_text.grid(row=2, column=1, columnspan=4, sticky="nsew", padx=5, pady=5)

    # Right column with image and dropdown
    options = ["选项1", "选项2", "选项3", "选项4"]
    for i in range(10):
        img_label = tk.Label(main_frame, image=photo)
        img_label.image = photo  # Keep a reference to the image
        img_label.grid(row=i, column=5, sticky="nsew", padx=5, pady=5)

    selected_option = tk.StringVar()
    option_menu = ttk.Combobox(main_frame, textvariable=selected_option, values=options)
    option_menu.grid(row=i, column=6, sticky="nsew", padx=5, pady=5)
    option_menu.current(0)  # Set default option

    # Configure grid weights
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)
    for i in range(1, 5):
        main_frame.grid_columnconfigure(i, weight=1)
        main_frame.grid_columnconfigure(5, weight=1)
        main_frame.grid_columnconfigure(6, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)

    root.mainloop()


create_ui()
