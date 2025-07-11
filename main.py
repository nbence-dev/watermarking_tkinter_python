from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageFont, ImageDraw, ImageTk

# TODO - Create GUI
# Main application window
window = Tk()
window.title("Watermarking Desktop GUI")  # GUI Heading
window.iconbitmap("watermark.ico")
window.geometry("500x500")  # The width and height of the GUI

# CONSTANTS used for resizing later
FRAME_WIDTH = 400
FRAME_HEIGHT = 300


# Function opens the Pictures directory.. now I just want it to work on all desktops
def openFile():

    filepath = filedialog.askopenfilename(  # gets the file path but also opens it
        initialdir=r"C:\Users\nicho\OneDrive\Pictures",
        title="Choose an image",
        filetypes=[("PNG Files", "*.png")],  # Limits it only to PNG files
    )
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
image_frame.pack(pady=20)


# TODO - Add place where image is loaded.
image_label = Label(image_frame)
image_label.pack()


# TODO - Add button that will open image directory
btn_open_directory = Button(window, text="Add Image", command=openFile)
btn_open_directory.pack()


def add_watermark():
    btn_save_image.config(state=NORMAL)


# TODO - After image is loaded, other button will be available to view and click
btn_add_watermark = Button(
    window, text="Add Watermark", command=add_watermark, state=DISABLED
)
btn_add_watermark.pack()


def save_image():
    pass


# TODO - After adding watermark, present save button
btn_save_image = Button(
    window, text="Save New Image", command=save_image, state=DISABLED
)
btn_save_image.pack()


def exitApp():
    window.destroy()


# TODO - Create Exit Application Button
btn_exit = Button(window, text="Close Application", command=exitApp)
btn_exit.pack()

window.mainloop()  # To ensure the GUI stays open
