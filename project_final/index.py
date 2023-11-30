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
#cell_size = board_size / row_column_size
#background
background_image_path = "image/1player.jpg"
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
    [1, 0, 0, 0],
    [0, 0, 3, 0],
    [0, 0, 0, 0],
    [0, 4, 0, 0]
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
#DrawMode
def DrawModes(screen):
    TitleFont = pygame.font.SysFont("times", 20, "bold")
    AttributeFont = pygame.font.SysFont("times", 20)
    screen.blit(TitleFont.render("Game Settings", True, (0, 0, 0)), (15, 505))
    screen.blit(AttributeFont.render("C: Clear", True, (0, 0, 0)), (30, 530))
    screen.blit(TitleFont.render("Modes", True, (0, 0, 0)), (15, 555))
    screen.blit(AttributeFont.render("E: Easy", True, (0, 0, 0)), (30, 580))
    screen.blit(AttributeFont.render("A: Average", True, (0, 0, 0)), (30, 605))
    screen.blit(AttributeFont.render("H: Hard", True, (0, 0, 0)), (30, 630))
# Selected Sudoku board
current_sudoku_board = sudoku_4x4

# Drawing code for a 4x4 board
def draw_board_4x4(screen, current_sudoku_board):
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
                text = font.render(str(current_sudoku_board[i][j]), True, white)
                screen.blit(text, (j * cell_size + cell_size // 2 - 7, vertical_size - board_size + i * cell_size + cell_size // 2 - 7))

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
                font = pygame.font.Font(None, 40)
                text = font.render(str(current_sudoku_board[i][j]), True, white)
                screen.blit(text, (j * cell_size + cell_size // 2 - 7, vertical_size - board_size + i * cell_size + cell_size // 2 - 7))

# Cấu hình font chữ
font_title = pygame.font.Font(None, 64)
font_button = pygame.font.Font(None, 36)

# Cấu hình màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
font_color = (153, 51, 255)
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
# Main function
def main():
    global current_sudoku_board
    # Initialize the Pygame screen
    screen = pygame.display.set_mode((horizontal_size, vertical_size + 1))
    pygame.display.set_caption("Sudoku")
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.set_mode((600,400))
                homepage.main()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is inside one of the buttons
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Check if 4x4 button is clicked
                if (
                    # board4x4_btn_x <= mouse_x <= board4x4_btn_x + btn_width and
                    # board4x4_btn_y <= mouse_y <= board4x4_btn_y + btn_height
                ):
                    current_sudoku_board = sudoku_4x4

                # Check if 9x9 button is clicked
                elif (
                    # board9x9_btn_x <= mouse_x <= board9x9_btn_x + btn_width and
                    # board9x9_btn_y <= mouse_y <= board9x9_btn_y + btn_height
                ):
                    current_sudoku_board = sudoku_9x9
                # Check if 16x16 button is clicked
                elif (
                    # board16x16_btn_x <= mouse_x <= board16x16_btn_x + btn_width and
                    # board16x16_btn_y <= mouse_y <= board16x16_btn_y + btn_height
                ):
                    current_sudoku_board = sudoku_16x16

                # Check if Exit Game button is clicked
                elif (
                    # exit_btn_x <= mouse_x <= exit_btn_x + btn_width and
                    # exit_btn_y <= mouse_y <= exit_btn_y + btn_height
                ):
                    pygame.quit()
                    sys.exit()

        # Fill the screen with a white background
        #screen.fill(white)

        # Draw the Sudoku board based on the current selected board
        draw_board(screen)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()

