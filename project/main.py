from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import random
import colorsys
from tkinter.filedialog import askopenfilename
import pygame


pygame.mixer.init()

# Create the window
window = Tk()
window.title("Image Decoding")
window.resizable(False, False)

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the size and position of the first window
window_width = 512
window_height = 512
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Define the starting HSL values for background color
hsl = [0, 0.5, 0.3]  # Adjust the lightness value (range: 0.0 to 1.0)

# Define the color transition step size
step = 0.001

# Function to update the background color
def update_bg_color():
    # Convert HSL to RGB
    rgb = colorsys.hls_to_rgb(hsl[0], hsl[2], hsl[1])

    # Convert RGB to hexadecimal color code
    hex_color = f"#{int(rgb[0] * 255):02x}{int(rgb[1] * 255):02x}{int(rgb[2] * 255):02x}"

    # Set the window background color
    window.configure(bg=hex_color)

    # Update the HSL values for the next color
    hsl[0] += step
    hsl[0] %= 1.0

    # Schedule the next color update
    window.after(20, update_bg_color)

# Start the color update loop
update_bg_color()

# Function to handle button 1 (Default Picture)
def use_default_picture():
    global image
    # Load the default picture
    image = Image.open("treasure.jpg").convert("RGBA")
    image = image.resize((512, 512))
    window.destroy()  # Close the window and proceed to the main window

# Function to handle button 2 (Upload a Picture)
def upload_picture():
    global image
    # Open a file dialog to select an image file
    filename = askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if filename:
        # Load the selected image
        image = Image.open(filename).convert("RGBA")
        image = image.resize((512, 512))
        window.destroy()  # Close the window and proceed to the main window

# Create the buttons in the window
default_button = Button(window, text="Default Picture", command=use_default_picture)
default_button.pack(pady=10)
upload_button = Button(window, text="Upload a Picture", command=upload_picture)
upload_button.pack(pady=10)

# Start the main loop
window.mainloop()

# After the window is closed, continue with the main program

# Load the image and create the mask
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=20))

# Create the main window
window = Tk()
window.title("Image decoding")
window.resizable(False, False)
# Define the starting HSL values
hsl = [0, 0.5, 0.3]  # Adjust the lightness value (range: 0.0 to 1.0)

# Define the color transition step size
step = 0.001

# Function to update the background color
def update_bg_color():
    # Convert HSL to RGB
    rgb = colorsys.hls_to_rgb(hsl[0], hsl[2], hsl[1])
    
    # Convert RGB to hexadecimal color code
    hex_color = f"#{int(rgb[0] * 255):02x}{int(rgb[1] * 255):02x}{int(rgb[2] * 255):02x}"
    
    # Set the window background color
    window.configure(bg=hex_color)

    # Update the HSL values for the next color
    hsl[0] += step
    hsl[0] %= 1.0

    # Schedule the next color update
    window.after(20, update_bg_color)

# Start the color update loop
update_bg_color()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size to cover the entire screen
window.geometry(f"{screen_width}x{screen_height}")
left_frame = Frame(window)
right_frame = Frame(window)
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)
canvas = Canvas(right_frame, width=image.width, height=image.height)
canvas.pack()

# Calculate the number of cells in the game board based on the size of the image
cell_size = 30
num_cells_x = image.width // cell_size
num_cells_y = image.height // cell_size

# Create the game board buttons
buttons = [[None for _ in range(num_cells_x)] for _ in range(num_cells_y)]

first_click = True
def start_game():
    global image_tk, mask, board, mines, first_click

    # Create the mask
    mask = Image.new("L", image.size, 0)

    # Display the image on the canvas
    image_tk = ImageTk.PhotoImage(blurred_image)
    canvas.create_image(0, 0, anchor=NW, image=image_tk)

    # Create the game board
    board = [[0 for _ in range(num_cells_x)] for _ in range(num_cells_y)]
    mines = random.sample([(i, j) for i in range(num_cells_x) for j in range(num_cells_y)], 10)

    # Move a mine from the randomly selected cell to a different cell
    if first_click:
        random_cell = random.choice(mines)
        new_cell = random.choice([(i, j) for i in range(num_cells_x) for j in range(num_cells_y) if (i, j) not in mines])
        mines.remove(random_cell)
        mines.append(new_cell)

    for mine in mines:
        board[mine[0]][mine[1]] = -1

    # Reset the game board buttons
    for i in range(num_cells_x):
        for j in range(num_cells_y):
            button = Button(window, text=" ")
            button.bind("<Button-1>", lambda event, i=i, j=j: open_cell(i, j))
            button.bind("<Button-3>", lambda event, i=i, j=j: flag_cell(i, j))
            button.place(x=i * cell_size, y=j * cell_size, width=cell_size, height=cell_size)
            buttons[i][j] = button

    first_click = True


    
def open_cell(i, j):
    global first_click

    # If the cell is flagged, do nothing
    if buttons[i][j]['text'] == "🚩":
        return

    # If the cell is flagged or a mine (and not the first click), game over
    if board[i][j] == -1 and not first_click:
        # Display the bomb symbol and play the bomb sound
        buttons[i][j].config(text="💣", fg="red")
        pygame.mixer.music.load("bomb.mp3")
        pygame.mixer.music.play()

        # Restart the puzzle
        start_game()
        return

    if buttons[i][j]['state'] == DISABLED or (board[i][j] == -1 and not first_click):
        return

    if first_click:
        first_click = False
        # Ensure the first click is not a mine
        while board[i][j] == -1:
            start_game()
        # Open some cells around the first click
        for x in range(max(0, i - 1), min(num_cells_x, i + 2)):
            for y in range(max(0, j - 1), min(num_cells_y, j + 2)):
                open_cell(x, y)

    # Calculate the number of adjacent mines
    num_mines = sum(board[x][y] == -1 for x in range(max(0, i - 1), min(num_cells_x, i + 2)) for y in
                    range(max(0, j - 1), min(num_cells_y, j + 2)))

    # Update the button text and color
    buttons[i][j].config(text=str(num_mines),
                         fg="red" if num_mines == 1 else "blue" if num_mines == 2 else "purple" if num_mines == 3 else "black")

    # Update the mask and blend it with the original image
    mask.paste(255, (i * cell_size, j * cell_size, (i + 1) * cell_size, (j + 1) * cell_size))
    revealed_image = Image.composite(image, blurred_image, mask)

    # Update the image on the canvas
    global image_tk
    image_tk = ImageTk.PhotoImage(revealed_image)
    canvas.create_image(0, 0, anchor=NW, image=image_tk)
    
def flag_cell(i, j):
    # If the cell is already opened or flagged, do nothing
    if buttons[i][j]['text'] != " ":
        return

    # Flag the cell
    buttons[i][j].config(text="🚩", state=DISABLED)

    # Check if the flagged cell is a bomb
    if (i, j) in mines:
        # Update the mask and blend it with the original image
        mask.paste(255, (i * cell_size, j * cell_size, (i + 1) * cell_size, (j + 1) * cell_size))
        revealed_image = Image.composite(image, blurred_image, mask)

        # Update the image on the canvas
        global image_tk
        image_tk = ImageTk.PhotoImage(revealed_image)
        canvas.create_image(0, 0, anchor=NW, image=image_tk)


start_game()
window.mainloop()