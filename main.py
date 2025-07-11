from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageFont, ImageDraw, ImageTk
import os
import platform
import subprocess
import time


def center_window(window, width=500, height=500):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


# TODO - Create GUI
# Main application window
window = Tk()
window.title("Watermarking Desktop GUI")  # GUI Heading
window.iconbitmap("watermark.ico")
center_window(window, width=445, height=500)  # The width and height of the GUI

# CONSTANTS used for resizing later
FRAME_WIDTH = 400
FRAME_HEIGHT = 300
BTN_WIDTH = 18


initial_dir = os.path.join(os.path.expanduser("~"), "Pictures")


# Function opens the Pictures directory.. now I just want it to work on all desktops
def openFile():
    global filename
    global filepath
    global original

    filepath = filedialog.askopenfilename(  # gets the file path but also opens it
        initialdir=initial_dir,
        title="Choose an image",
        filetypes=[("PNG Files", "*.png")],  # Limits it only to PNG files
    )
    filename = os.path.basename(filepath)
    if filepath:
        original = Image.open(filepath)  # gets the original image
        resized = original.resize(
            (FRAME_WIDTH, FRAME_HEIGHT), Image.LANCZOS
        )  # resizing the image with high-quality resampling filter. Good in downsclaing
        img = ImageTk.PhotoImage(resized)  # load the image into the label
        image_label.config(image=img)
        image_label.image = img
        btn_add_watermark.config(state=NORMAL)


# TODO - Create a frame which holds the image
image_frame = Frame(window, bg="gray", width=FRAME_WIDTH, height=FRAME_HEIGHT)
image_frame.grid(row=0, columnspan=3, sticky="nsew", padx=10)
image_frame.pack_propagate(False)


# TODO - Add place where image is loaded.
image_label = Label(image_frame)
image_label.pack()


# TODO - Add button that will open image directory
btn_open_directory = Button(window, text="Add Image", command=openFile, width=BTN_WIDTH)
btn_open_directory.grid(row=1, column=0, padx=5, pady=5)


def add_watermark():
    global original
    global watermarked_image
    # Youtube Tutorial Watermarking
    original = original.convert("RGBA")
    width, height = original.size

    overlay = Image.new("RGBA", original.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(overlay)

    watermark_color_pattern = (255, 255, 255, 30)

    for i in range(0, width + height, 50):
        draw.line([(0, height - i), (i, height)], fill=watermark_color_pattern, width=5)

    font_size = 80
    font = ImageFont.truetype("arial.ttf", font_size)

    bbox = draw.textbbox((0, 0), "Nicholas", font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = original.width // 2
    y = original.height // 2

    position = (x - text_width // 2, y - text_height // 2)

    watermark_color_text = (255, 255, 255, 80)
    draw.text(position, "Watermark", fill=watermark_color_text, font=font)

    watermarked_image = Image.alpha_composite(original, overlay)
    #     # Creating RGBA overlay

    #     global original
    #     original = original.convert("RGBA")

    #     # Prepare to draw
    #     draw = ImageDraw.Draw(original)
    #     font = ImageFont.truetype("arial.ttf", 46)
    #     text = "Watermark"

    #     # Measure text size
    #     bbox = draw.textbbox((0, 0), text, font=font)
    #     text_width = bbox[2] - bbox[0]
    #     text_height = bbox[3] - bbox[1]

    #     # Calculate center coordinates on original
    #     center_x = original.width // 2
    #     center_y = original.height // 2

    #     # Offset by half the text dimensions
    #     position = (center_x - text_width // 2, center_y - text_height // 2)

    #     # Draw centered watermark
    #     draw.text(position, text, font=font, fill=(255, 255, 255, 128))

    # width, height = original.size
    # center_x = width // 2
    # center_y = height // 2
    # # Define the font
    # text_font = ImageFont.truetype("arial.ttf", 46)
    # # That is the text font
    # text_to_add = "Watermark"

    # # Edit image
    # edit_image = ImageDraw.Draw(original)
    # edit_image.text((center_x, center_y), text_to_add, font=text_font)

    # Resize original image and add it to frame
    resized = watermarked_image.resize(
        (FRAME_WIDTH, FRAME_HEIGHT), Image.LANCZOS
    )  # resizing the image with high-quality resampling filter. Good in downsclaing
    img = ImageTk.PhotoImage(resized)  # load the image into the label
    image_label.config(image=img)
    image_label.image = img
    btn_save_image.config(state=NORMAL)
    messagebox.showinfo("Success!", "Watermark added successfully.")


# TODO - After image is loaded, other button will be available to view and click
btn_add_watermark = Button(
    window, text="Add Watermark", command=add_watermark, state=DISABLED, width=BTN_WIDTH
)
btn_add_watermark.grid(row=1, column=1, padx=5, pady=5)


def open_file(filepath):
    if platform.system() == "Windows":
        os.startfile(filepath)
    elif platform.system() == "Darwin":
        subprocess.run(["open", filepath])
    elif platform.system() == "Linux":
        subprocess.run(["xdg-open", filepath])


def save_image():
    original_folder = os.path.dirname(filepath)
    new_filename = f"watermarked_{filename}"
    save_path = os.path.join(original_folder, new_filename)
    watermarked_image.save(save_path)
    messagebox.showinfo("Success!", f"Image saved to: {save_path}.\nOpening image...")
    time.sleep(0.8)

    open_file(save_path)


# TODO - After adding watermark, present save button
btn_save_image = Button(
    window, text="Save New Image", command=save_image, state=DISABLED, width=BTN_WIDTH
)
btn_save_image.grid(row=1, column=2, padx=5, pady=5)


def exitApp():
    window.destroy()
    messagebox.showinfo("Terminating program...", "Have a good day")


# TODO - Create Exit Application Button
btn_exit = Button(window, text="Close Application", command=exitApp, width=BTN_WIDTH)
btn_exit.grid(row=2, column=2, padx=10, pady=120)

window.mainloop()  # To ensure the GUI stays open
