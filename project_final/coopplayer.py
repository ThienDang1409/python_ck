import pygame
import sys
import random
import time
import homepage
# Initialize Pygame
pygame.init()

# Constants
horizontal_size = 1200
vertical_size = 700
board_size = 450
#row_column_size = 9
#cell_size = board_size / row_column_sizea
#background
background_image_path = "image/2player.jpg"
background_image_load = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image_load, (horizontal_size,vertical_size))

#icon
# icon_path = "image/icon.png"
# icon_load = pygame.image.load(icon_path)
# icon_main = pygame.transform.scale(icon_load, (100,100))
# icon_rect = icon_main.get_rect()
# icon_rect.center = (horizontal_size - 80,120)
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
lightgray = (211, 211, 211)

# Button dimensions
# btn_width = 120
# btn_height = 50

# Button positions
# board4x4_btn_x = board_size + 10
# board4x4_btn_y = (vertical_size - board_size / 2) - btn_height / 2 * 3 - 20
# board9x9_btn_x = board_size + 10
# board9x9_btn_y = (vertical_size - board_size / 2) - btn_height / 2
# exit_btn_x = board_size + 10
# exit_btn_y = (vertical_size - board_size / 2) + btn_height / 2 + 20
# board16x16_btn_x = board4x4_btn_x
# board16x16_btn_y = board4x4_btn_y - btn_height - 10

# Sudoku boards (4x4, 9x9, 16x16)
sudoku_4x4 = [
    [3, 4, 0, 2],
    [2, 1, 0, 3],
    [4, 3, 0, 1],
    [1, 2, 3, 0]
]

sudoku_9x9 = [
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 3],
    [0, 0, 0, 8, 0, 3, 0, 0, 1],
    [0, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

sudoku_16x16 = [
    [0, 0, 0, 0, 0, 4, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 6, 0, 0, 0, 0, 3, 8, 9, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 2, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
# Selected Sudoku board
current_sudoku_board = sudoku_4x4
def set_default_4x4(current_sudoku_board):
    global default_value_4x4
    for i in range(len(current_sudoku_board)):
            for j in range(len(current_sudoku_board)):
                if current_sudoku_board[i][j] != 0:
                    default_value_4x4.append((j,i))
# Drawing code for a 4x4 board
def draw_board_4x4(screen, current_sudoku_board):
    global default_value_4x4
    board_size = 450
    cell_size = board_size / len(current_sudoku_board)

    for i in range(len(current_sudoku_board) + 1):
        if i % 2 == 0:
            pygame.draw.line(screen, white, (i * cell_size, vertical_size - board_size), (i * cell_size, vertical_size), 3)
            pygame.draw.line(screen, white, (0, i * cell_size + (vertical_size - board_size)), (board_size, i * cell_size + (vertical_size - board_size)), 3)
        else:
            pygame.draw.line(screen, white, (i * cell_size, vertical_size - board_size), (i * cell_size, vertical_size))
            pygame.draw.line(screen, white, (0, i * cell_size + (vertical_size - board_size)), (board_size, i * cell_size + (vertical_size - board_size)))

    for i in range(len(current_sudoku_board)):
        for j in range(len(current_sudoku_board)):
            if current_sudoku_board[i][j] != 0:
                font = pygame.font.Font(None, 60)
                if(j,i) not in default_value_4x4:
                    text = font.render(str(current_sudoku_board[i][j]), True, (144, 238, 144))
                else:
                    text = font.render(str(current_sudoku_board[i][j]), True, white)
                screen.blit(text, (j * cell_size + cell_size // 2 - 7, vertical_size - board_size + i * cell_size + cell_size // 2 - 7))

def draw_board_4x4_coop(screen, current_sudoku_board):
    global default_value_4x4
    board_size = 450
    cell_size = board_size / len(current_sudoku_board)

    for i in range(len(current_sudoku_board) + 1):
        if i % 2 == 0:
            pygame.draw.line(screen, white, (horizontal_size - i * cell_size, vertical_size - board_size), (horizontal_size - i * cell_size, vertical_size), 3)
            pygame.draw.line(screen, white, (horizontal_size, i * cell_size + (vertical_size - board_size)), (horizontal_size - board_size, i * cell_size + (vertical_size - board_size)), 3)
        else:
            pygame.draw.line(screen, white, (horizontal_size - i * cell_size, vertical_size - board_size), (horizontal_size - i * cell_size, vertical_size))
            pygame.draw.line(screen, white, (horizontal_size, i * cell_size + (vertical_size - board_size)), (horizontal_size - board_size, i * cell_size + (vertical_size - board_size)))

    for i in range(len(current_sudoku_board)):
        for j in range(len(current_sudoku_board)):
            if current_sudoku_board[i][j] != 0:
                font = pygame.font.Font(None, 60)
                if(j,i) not in default_value_4x4:
                    text = font.render(str(current_sudoku_board[i][j]), True, (144, 238, 144))
                else:
                    text = font.render(str(current_sudoku_board[i][j]), True, white)
                screen.blit(text, ((horizontal_size - board_size) + j * cell_size + cell_size // 2 - 7, vertical_size - board_size + i * cell_size + cell_size // 2 - 7))  
                
# Drawing code for a 9x9 board
def draw_board_9x9(screen, current_sudoku_board):
    board_size = 450
    cell_size = board_size / len(current_sudoku_board)

    for i in range(len(current_sudoku_board) + 1):
        if i % 3 == 0:
            pygame.draw.line(screen, white, (i * cell_size, vertical_size - board_size), (i * cell_size, vertical_size), 3)
            pygame.draw.line(screen, white, (0, i * cell_size + (vertical_size - board_size)), (board_size, i * cell_size + (vertical_size - board_size)), 3)
        else:
            pygame.draw.line(screen, white, (i * cell_size, vertical_size - board_size), (i * cell_size, vertical_size))
            pygame.draw.line(screen, white, (0, i * cell_size + (vertical_size - board_size)), (board_size, i * cell_size + (vertical_size - board_size)))

    for i in range(len(current_sudoku_board)):
        for j in range(len(current_sudoku_board)):
            if current_sudoku_board[i][j] != 0:
                font = pygame.font.Font(None, 50)
                text = font.render(str(current_sudoku_board[i][j]), True, white)
                screen.blit(text, (j * cell_size + cell_size // 2 - 7, vertical_size - board_size + i * cell_size + cell_size // 2 - 7))

def draw_board_16x16(screen, current_sudoku_board):
    board_size = 450
    cell_size = board_size / len(current_sudoku_board)

    for i in range(len(current_sudoku_board) + 1):
        if i % 4 == 0:
            pygame.draw.line(screen, white, (i * cell_size, vertical_size - board_size), (i * cell_size, vertical_size), 3)
            pygame.draw.line(screen, white, (0, i * cell_size + (vertical_size - board_size)), (board_size, i * cell_size + (vertical_size - board_size)), 3)
        else:
            pygame.draw.line(screen, white, (i * cell_size, vertical_size - board_size), (i * cell_size, vertical_size))
            pygame.draw.line(screen, white, (0, i * cell_size + (vertical_size - board_size)), (board_size, i * cell_size + (vertical_size - board_size)))

    for i in range(len(current_sudoku_board)):
        for j in range(len(current_sudoku_board)):
            if current_sudoku_board[i][j] != 0:
                font = pygame.font.Font(None, 30)
                text = font.render(str(current_sudoku_board[i][j]), True, white)
                screen.blit(text, (j * cell_size + cell_size // 2 - 7, vertical_size - board_size + i * cell_size + cell_size // 2 - 7))

# Cấu hình font chữ
font_title = pygame.font.Font(None, 80)
font_button = pygame.font.Font(None, 36)

# Cấu hình màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
font_color = (0, 191, 255)
button_color = (50, 50, 50)  # Màu của nút
border_color = (0, 0, 255)  # Màu của viền
border_width = 2  # Độ rộng của viền
# Modify the main draw_board function
def draw_board(screen):
    board_size = 450
    cell_size = board_size / len(current_sudoku_board)
    screen.blit(background_image,(0,0))
    # screen.blit(icon_main, icon_rect)
    # Call the appropriate draw function based on the board size
    if current_sudoku_board == sudoku_4x4:
        draw_board_4x4(screen, current_sudoku_board)
        draw_board_4x4_coop(screen, current_sudoku_board)
    elif current_sudoku_board == sudoku_9x9:
        draw_board_9x9(screen, current_sudoku_board)
    elif current_sudoku_board == sudoku_16x16:
        draw_board_16x16(screen, current_sudoku_board)

    # pygame.draw.rect(screen, lightgray, (board4x4_btn_x, board4x4_btn_y, btn_width, btn_height))
    # pygame.draw.rect(screen, lightgray, (board9x9_btn_x, board9x9_btn_y, btn_width, btn_height))
    # pygame.draw.rect(screen, lightgray, (board16x16_btn_x, board16x16_btn_y, btn_width, btn_height))
    # pygame.draw.rect(screen, lightgray, (exit_btn_x, exit_btn_y, btn_width, btn_height))
    # font = pygame.font.Font(None, 26)
    # board4x4_txt = font.render("4x4", True, black)
    # board9x9_txt = font.render("9x9", True, black)
    # board16x16_txt = font.render("16x16", True, black)
    # exit_txt = font.render("Exit Game", True, black)
    # screen.blit(board4x4_txt, (board_size + btn_width / 5 * 1.1, (vertical_size - board_size / 2) - btn_height / 2 * 3 - 20 + (btn_height / 5 * 1.8)))
    # screen.blit(board9x9_txt, (board_size + btn_width / 5 * 1.1, (vertical_size - board_size / 2) - btn_height / 2 + (btn_height / 5 * 1.8)))
    # screen.blit(board16x16_txt, (board_size + btn_width / 5 * 1.1, (vertical_size - board_size / 2) - btn_height / 2 * 3 - 80 + (btn_height / 5 * 1.8)))
    # screen.blit(exit_txt, (board_size + btn_width / 5 * 1.1, (vertical_size - board_size / 2) + btn_height / 2 + 20 + (btn_height / 5 * 1.8)))
    #pygame.draw.rect(screen, white, board_rect)

    # Vẽ tiêu đề "SUDOKU"
    title_text = font_title.render("SUDOKU", True, (127,0,255))
    title_rect = title_text.get_rect(center=(horizontal_size // 2, vertical_size - 600))
    screen.blit(title_text, title_rect)
    # Vẽ các nút chế độ
    button_texts_mode = ["4x4", "9x9", "16x16"] 
    # Vẽ các nút về game
    button_texts_game = ["Start", "New game", "Exit"]
    # Vẽ các nút giải
    button_texts_solve = ["DFS", "UCS", "BFS"]

    button_rects = []

    for i, text in enumerate(button_texts_mode):
        button_text = font_button.render(text, True, font_color)
        button_rect = button_text.get_rect(center=(horizontal_size  // 2 - 100 + i * 100, vertical_size // 2 ))
        expanded_rect = button_rect.inflate(border_width * 15, border_width * 10)
        # pygame.draw.rect(screen, button_color, expanded_rect)
        pygame.draw.rect(screen, border_color, expanded_rect, border_width)
        button_rects.append(button_rect)
        screen.blit(button_text, button_rect)
    for i, text in enumerate(button_texts_game):
        button_text = font_button.render(text, True, font_color)
        button_rect = button_text.get_rect(center=(horizontal_size  // 2 - 100 + i * 100, vertical_size // 2 + 100 ))
        expanded_rect = button_rect.inflate(border_width * 8, border_width * 8)
        # pygame.draw.rect(screen, button_color, expanded_rect)
        pygame.draw.rect(screen, border_color, expanded_rect, border_width)
        button_rects.append(button_rect)
        screen.blit(button_text, button_rect)
    for i, text in enumerate(button_texts_solve):
        button_text = font_button.render(text, True, font_color)
        button_rect = button_text.get_rect(center=(horizontal_size  // 2 - 100 + i * 100, vertical_size // 2 + 200 ))
        expanded_rect = button_rect.inflate(border_width * 15, border_width * 10)
        # pygame.draw.rect(screen, button_color, expanded_rect)
        pygame.draw.rect(screen, border_color, expanded_rect, border_width)
        button_rects.append(button_rect)
        screen.blit(button_text, button_rect)
    return button_rects


def Suggest_Value_4x4_column(i,j):
    another_in_column = []
    not_suggest_value_4x4 = []
    suggest_value_4x4 = []
    string = ' '
    for ii in range(4):
        if ii != j:
            if sudoku_4x4[i][ii] != sudoku_4x4[int(i)][int(j)]:
                another_in_column.append((i,ii))
    print(another_in_column)
    for suggest in another_in_column:
        i,j = suggest
        value = sudoku_4x4[int(j)][int(i)]
        not_suggest_value_4x4.append(value)
    for kk in range(1,5):
        if kk in not_suggest_value_4x4:
            continue
        else:
            suggest_value_4x4.append(kk)
    print(suggest_value_4x4)
    DisplayMessage(f'Suggest: {suggest_value_4x4}', 500, (255, 255, 255))

def IsValueValid(i, j):
    for ii in range(4):
        if ii != j:
            if sudoku_4x4[i][ii] == sudoku_4x4[int(i)][int(j)]:  # checks cols and rows
                return False
    for ii in range(4):
        if ii != i:
            if sudoku_4x4[ii][j] == sudoku_4x4[int(i)][int(j)]:  # checks cols and rows
                return False
    # checks the box/block
    ii = i // 2
    jj = j // 2
    for a in range(ii * 2, ii * 2 + 2):
        for b in range(jj * 2, jj * 2 + 2):
            if a != j:
                if sudoku_4x4[i][a] == sudoku_4x4[int(i)][int(j)]:
                    return False
    for a in range(ii * 2, ii * 2 + 2):
        for b in range(jj * 2, jj * 2 + 2):
            if b != i:
                if sudoku_4x4[b][j] == sudoku_4x4[int(i)][int(j)]:
                    return False
    return True

def IsUserWin():
    for i in range(4):
        for j in range(4):
            if IsValueValid(i,j) == False:
                return False
    for i in range(4):
        for j in range(4):
            if sudoku_4x4[int(i)][int(j)] == 0:
                return False
    return True

# message
def DisplayMessage(Message, Interval, Color):
    screen.blit(a_font.render(Message, True, Color), (112, 210))
    pygame.display.update()
    pygame.time.delay(Interval)

# insert value entered by user
def InsertValue(Value):
    global default_value_4x4
    if (x,y) not in default_value_4x4:
        sudoku_4x4[int(y)][int(x)] = Value
        if Value != 0:
            text = a_font.render(str(Value), True, (144, 238, 144))
        else:
            text = a_font.render('', True, (0, 0, 0))
        # screen.blit(text, (x * inc + 15, y * inc + 15))
        screen.blit(text, (x * inc + 15, y * inc + 250 + 15))
    print(default_value_4x4)
# setting the initial position
def SetMousePosition(p):
    global x, y
    if p[0] < 450 and p[1] < 700 and p[1] >250:
        print(p[0])
        print(p[1])
        x = p[0] // inc
        y = (p[1]-280) // inc
        Suggest_Value_4x4_column(x,y)
def DrawSelectedBox():
    for i in range(2):
        pygame.draw.line(screen, (0, 0, 255), (x * inc, (y + i) * inc + 250), (x * inc + inc, (y + i) * inc+250), 5)
        pygame.draw.line(screen, (0, 0, 255), ((x + i) * inc, y * inc+250), ((x + i) * inc, y * inc + inc+250), 5)
def DrawUserValue():
    global UserValue
    if UserValue >= 0 and UserValue <5:
        InsertValue(UserValue)
        if IsUserWin():
            DisplayMessage("YOU WON!!!!", 5000, (255, 255, 255))
        # if IsUserValueValid(grid, x, y, UserValue):
        #     if grid[int(x)][int(y)] == 0:
        #         InsertValue(UserValue)
        #         UserValue = 0
        #         if IsUserWin():
        #             IsSolving = False
        #             DisplayMessage("YOU WON!!!!", 5000, (0, 255, 0))
        #     else:
        #         UserValue = 0
        # else:
        #     DisplayMessage("Incorrect Value", 500, (255, 0, 0))
        #     UserValue = 0
# Main function
def main():
    global IsRunning, grid, x, y, UserValue, inc, ind, screen, a_font
    global current_sudoku_board
    global default_value_4x4
    default_value_4x4 = []
    set_default_4x4(current_sudoku_board)
    # Initialize the Pygame screen
    screen = pygame.display.set_mode((horizontal_size, vertical_size + 1))
    pygame.display.set_caption("Sudoku")
    inc = 450//4
    x = 0
    y = 0
    a_font = pygame.font.SysFont("times", 30, "bold")
    UserValue = 0
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.set_mode((600,400))
                homepage.main()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                SetMousePosition(mouse_pos)
                for i, rect in enumerate(button_rectangles):
                    if rect.collidepoint(mouse_pos):
                        if i == 0: 
                            current_sudoku_board = sudoku_4x4
                        elif i==1:
                            current_sudoku_board = sudoku_9x9
                        elif i==2:
                            current_sudoku_board = sudoku_16x16
                        elif i==3:
                            current_sudoku_board = sudoku_9x9
                        elif i==4:
                            current_sudoku_board = sudoku_9x9
                        elif i==5:# Exit button
                            pygame.quit()
                            sys.exit()
                        elif i==6:
                            current_sudoku_board = sudoku_9x9
                        elif i==7:
                            current_sudoku_board = sudoku_9x9
                        elif i == 8:  
                            current_sudoku_board = sudoku_9x9
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    UserValue = 1
                    DrawUserValue()
                if event.key == pygame.K_2:
                    UserValue = 2
                    DrawUserValue()
                if event.key == pygame.K_3:
                    UserValue = 3
                    DrawUserValue()
                if event.key == pygame.K_4:
                    UserValue = 4
                    DrawUserValue()
                if event.key == pygame.K_5:
                    UserValue = 5
                    DrawUserValue()
                if event.key == pygame.K_6:
                    UserValue = 6
                    DrawUserValue()
                if event.key == pygame.K_7:
                    UserValue = 7
                    DrawUserValue()
                if event.key == pygame.K_8:
                    UserValue = 8
                    DrawUserValue()
                if event.key == pygame.K_9:
                    UserValue = 9
                    DrawUserValue()
                if event.key == pygame.K_DELETE:
                    UserValue = 0
                    DrawUserValue()

        # Draw the Sudoku board based on the current selected board
        button_rectangles = draw_board(screen)
        DrawSelectedBox()
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()