# Image Decoding: Unveiling Secrets with Minesweeper

Welcome to the Image Decoding repository! This interactive project implements a unique puzzle-solving approach inspired by the classic game of Minesweeper. You can use this program to unravel hidden messages concealed within images of your choice.


https://github.com/Amirrezahmi/Image-Decoding/assets/89692207/c05a9c88-d416-4899-8145-2a2d7155e052

## Features

   - Decoding images using Minesweeper-based puzzles
   - Dynamic and visually appealing user interface
   - Background color transitions for an immersive experience
   - Human verification through logical reasoning and strategic thinking

## Prerequisites

To run the Image Decoding program, make sure you have the following installed:

   - Python (version 3.6 or above)
   - tkinter package
   - PIL package
   - pygame package


## Getting Started

  1. Clone this repository to your local machine.

     ```bash
     git clone https://github.com/Amirrezahmi/Image-Decoding.git
     ```

2. Navigate to the project directory.


     ```bash
   cd Image-Decoding
     ```
  
3. Install the required dependencies.


     ```bash
   pip install -r requirements.txt
     ```
  
4. Launch the program.

     ```bash
   python main.py
     ```
5. Select your image or press "Default Picture" button to begin the decoding process.

## How to Play

   1. Left Click: Click on a cell with the left mouse button to reveal its content.
      - Pay attention to the number displayed on the revealed cell. This number represents the number of adjacent cells containing clues.
      - Utilize the clues to strategically identify safe cells and avoid hidden mines.
   2. Right Click: Click on a cell with the right mouse button to mark it with a flag.
      - Flagging a cell indicates your suspicion of a mine.
      - Use this feature to mark cells you believe may contain mines, allowing you to avoid them during the decoding process.
      - $\textbf{Important}$: When you flag a cell correctly, the corresponding part of the image will be decoded, revealing a portion of the hidden message. However, if you flag a cell incorrectly, that part of the image won't decode, emphasizing that blindly flagging all cells won't help you uncover the entire secret message.

<div align="center">
  <img src="https://github.com/Amirrezahmi/Image-Decoding/assets/89692207/1aa8a4bf-9085-4d23-9bbc-d465947704e3" alt="20230617_123525_0000" width="600" />
</div>



   3. Decoding Strategy: Combine the information from the revealed numbers and your flagged cells to make informed decisions.
      - Deduce the contents of neighboring cells based on the numbers displayed.
      - Exercise caution! If you click on a cell containing a mine without flagging it, the game will restart, and you'll need to begin the decoding process again.
   4. First Click: The first click on the game board is always safe, ensuring you have a chance to observe the initial clue and plan your decoding strategy accordingly.
   5. Winning Condition: Uncover all non-mine cells to successfully decode the image and reveal its secret message.


## Human Verification

Beyond the exciting decoding adventure, this program can also serve as a human verification tool. By requiring users to employ logical reasoning and strategic thinking to decode the image, it ensures that they are real people interacting with the system.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug fixes, please open an issue or submit a pull request.


## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).


## Acknowledgments

The Minesweeper game concept and image decoding inspiration


## Contact


For any inquiries or feedback, please contact amirrezahmi2002@gmail.com.

Enjoy the adventure of image decoding!





