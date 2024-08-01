import tkinter #tk-interface (graphical user interface library)
from playsound import playsound
from threading import Thread

import tkinter as tk
import time


def main():
    # Create the splash screen
    splash_root = tk.Tk()
    splash_root.title("Introduction")
    splash_root.geometry("550x150")

    # Add a label or image to the splash screen
    splash_label = tk.Label(splash_root, text="Welcome to the Tic-Tac-Toe Game!\n\n"
                            "Instructions:\n\n"
                            "1. Each player takes a turn clicking the box each as X or O\n"
                            "2. The first player to make their X or O in a straight line with 3 letters regardless of position wins\n"
                            "3. Click the X in the top right side to start the game\n"
                            "4. Click restart to restart the game!\n"
                            "5. Good Luck Players!")
    splash_label.pack()
    splash_root.mainloop()

if __name__ == "__main__":
    main()


def play_click_sound():
    try:
        playsound(r"C:\Users\ongzo\Downloads\game-sound.mp3")
    except Exception as e:
        print(f"Error playing sound: {e}")
    
# play sound from file path
def play_music_loop():
  while True:
    playsound(r"C:\Users\ongzo\Downloads\Fluffing-a-Duck(chosic.com).mp3")

# Create a thread for music
music_thread = Thread(target=play_music_loop)
music_thread.daemon = True  # Ensure thread terminates when main program ends
music_thread.start()

def set_tile(row, column):
    global curr_player
    play_click_sound()  # Call the sound function after marking the board
      # Add a small delay to prevent rapid sound overlap

    if (game_over):
        return

    if board[row][column]["text"] != "":
        #already taken spot
        return

    board[row][column]["text"] = curr_player #mark the board

    if curr_player == playerO: #switch player
        curr_player = playerX
    else:
        curr_player = playerO
    
    label["text"] = curr_player+"'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    #horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=colour_orange)
            for column in range(3):
                board[row][column].config(foreground=colour_orange, background=colour_lightgray)
            game_over = True
            return
        
    #vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=colour_orange)
            for row in range(3):
                board[row][column].config(foreground=colour_orange, background=colour_lightgray)
            game_over = True
            return
        
    #diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=colour_orange)
        for i in range(3):
            board[i][i].config(foreground=colour_orange, background=colour_lightgray)
        game_over = True
        return
    
    #anti-diagonally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=colour_orange)
        board[0][2].config(foreground=colour_orange, background=colour_lightgray)
        board[1][1].config(foreground=colour_orange, background=colour_lightgray)
        board[2][0].config(foreground=colour_orange, background=colour_lightgray)
        game_over = True
        return
    
    #tie
    if (turns == 9):
        game_over = True
        label.config(text="Tie!", foreground=colour_orange)


def new_game():
    global turns, game_over

    turns = 0
    game_over= False

    label.config(text=curr_player+"'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=colour_blue, background=colour_gray)


#game setup
playerX = "X"
playerO = "O"
curr_player =  playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

colour_blue = "#33FFFC"
colour_orange = "#FF9F33"
colour_gray = "#737373"
colour_lightgray = "#B9B7B7"

turns = 0
game_over = False

#window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 20), background=colour_gray,
                      foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=colour_gray, foreground=colour_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=colour_gray,
                        foreground="White", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
# Create a thread to play music
music_thread = Thread(target=play_music_loop)

# Start the thread
music_thread = Thread(target=play_music_loop)
music_thread.daemon = True  # Ensure thread terminates when main program ends
music_thread.start()
window.mainloop()
