import pygame
import sys
import random
import time
import homepage
import math
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

def solve_sudoku_dfs(current_sudoku_board):
    lenght = len(current_sudoku_board[0])
    for i in range(lenght):
        for j in range(lenght):
            if current_sudoku_board[i][j] == 0:
                for k in range(1,lenght + 1):
                    current_sudoku_board[i][j] = k
                    draw_board(screen)
                    pygame.display.flip()
                    time.sleep(0.01)
                    if is_valid(i,j,k,current_sudoku_board):
                        if solve_sudoku_dfs(current_sudoku_board):      
                            return True
                    current_sudoku_board[i][j] = 0
                    draw_board(screen)
                    pygame.display.flip()
                    time.sleep(0.01)
                return False
    return True
def is_valid(a,b,c,current_sudoku_board):
    lenght = len(current_sudoku_board[0])
    rows = int(math.sqrt(lenght) * (a//math.sqrt(lenght))) 
    columns = int(math.sqrt(lenght) * (b//math.sqrt(lenght)))  
    for i in range(lenght):
        if i != b:
            if c == current_sudoku_board[a][i]:
                return False
        if i != a:
            if c == current_sudoku_board[i][b]:
                return False
    for i in range(rows,int(rows+math.sqrt(lenght))):
        for j in range(columns,int(columns+math.sqrt(lenght))):
            if i != a and j != b:
                if c == current_sudoku_board[i][j]:
                    return False
    return True  

sudoku_4x4 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

sudoku_9x9 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

sudoku_16x16 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

entry_list = [[],[],[]]
def clear_4x4():
    global sudoku_4x4
    sudoku_4x4 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#xáo trộn
def scramble_4x4():
    global sudoku_4x4
    clear_4x4()
    for a in entry_list:
        for b in a:
            b.delete(first=0,last=100)
    amount = 7
    for i in range(amount):
        y = random.randint(0,len(sudoku_4x4)-1)
        x = random.randint(0,len(sudoku_4x4)-1)
        num = random.randint(1,len(sudoku_4x4))
        allow = 0
        for e in range(len(sudoku_4x4)):
            if num not in sudoku_4x4[x] and num != sudoku_4x4[e][y]:
                allow +=1
        sudoku_4x4[x][y] = num
        tempo = sudoku_4x4     
        tempo = rearrange_4x4(tempo)
        
        for e in range(len(sudoku_4x4)):
            if(duplicate_checker_4x4(tempo[e])):
                allow = 0
        if allow !=len(sudoku_4x4):
            sudoku_4x4[x][y] = 0


def rearrange_4x4(a):
    temp=[[],[],[],[]]
    count =0
    ch = 0
    for e in range(len(a)):
        for x in range(2):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count == 2):
            ch+=1
            count = 0
    for e in range(len(a)):
        for x in range(2,4):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count == 2):
            ch+=1
            count = 0
    return temp

def duplicate_checker_4x4(a):
        b = set(a)
        result = len(a) != len(b)
        #print(result)
        if(result == True):
            return True

def clear_9x9():
    global sudoku_9x9
    sudoku_9x9 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#xáo trộn
def scramble_9x9():
    global sudoku_9x9
    clear_9x9()
    for a in entry_list:
        for b in a:
            b.delete(first=0,last=100)
    amount = 40
    for i in range(amount):
        y = random.randint(0,len(sudoku_9x9)-1)
        x = random.randint(0,len(sudoku_9x9)-1)
        num = random.randint(1,len(sudoku_9x9))
        allow = 0
        for e in range(len(sudoku_9x9)):
            if num not in sudoku_9x9[x] and num != sudoku_9x9[e][y]:
                allow +=1
        sudoku_9x9[x][y] = num
        tempo = sudoku_9x9     
        tempo = rearrange_9x9(tempo)
        
        for e in range(len(sudoku_9x9)):
            if(duplicate_checker_9x9(tempo[e])):
                allow = 0
        if allow !=len(sudoku_9x9):
            sudoku_9x9[x][y] = 0


def rearrange_9x9(a):
    temp=[[],[],[],[],[],[],[],[],[]]
    count =0
    ch = 0
    for e in range(len(a)):
        for x in range(3):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count ==3):
            ch+=1
            count = 0
    for e in range(len(a)):
        for x in range(3,6):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count ==3):
            ch+=1
            count = 0
    for e in range(len(a)):
        for x in range(6,9):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count ==3):
            ch+=1
            count = 0
    return temp

def duplicate_checker_9x9(a):
        b = set(a)
        result = len(a) != len(b)
        #print(result)
        if(result == True):
            return True

def clear_16x16():
    global sudoku_16x16
    sudoku_16x16 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#xáo trộn
def scramble_16x16():
    global sudoku_16x16
    clear_16x16()
    for a in entry_list:
        for b in a:
            b.delete(first=0,last=100)
    amount = 100
    for i in range(amount):
        y = random.randint(0,len(sudoku_16x16)-1)
        x = random.randint(0,len(sudoku_16x16)-1)
        num = random.randint(1,len(sudoku_16x16))
        allow = 0
        for e in range(len(sudoku_16x16)):
            if num not in sudoku_16x16[x] and num != sudoku_16x16[e][y]:
                allow +=1
        sudoku_16x16[x][y] = num
        tempo = sudoku_16x16     
        tempo = rearrange_16x16(tempo)
        
        for e in range(len(sudoku_16x16)):
            if(duplicate_checker_16x16(tempo[e])):
                allow = 0
        if allow !=len(sudoku_16x16):
            sudoku_16x16[x][y] = 0


def rearrange_16x16(a):
    temp=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    count =0
    ch = 0
    for e in range(len(a)):
        for x in range(4):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count == 4):
            ch+=1
            count = 0
    for e in range(len(a)):
        for x in range(4,8):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count == 4):
            ch+=1
            count = 0
    for e in range(len(a)):
        for x in range(8,12):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count == 4):
            ch+=1
            count = 0
    for e in range(len(a)):
        for x in range(12,16):
            if(a[e][x]!=0):
                temp[ch].append(a[e][x])
        count+=1
        if(count == 4):
            ch+=1
            count = 0
    return temp

def duplicate_checker_16x16(a):
        b = set(a)
        result = len(a) != len(b)
        #print(result)
        if(result == True):
            return True



# Selected Sudoku board
current_sudoku_board = sudoku_4x4
def set_default_4x4(current_sudoku_board):
    global default_value_4x4
    for i in range(len(current_sudoku_board)):
            for j in range(len(current_sudoku_board)):
                if current_sudoku_board[i][j] != 0:
                    default_value_4x4.append((j,i))
def set_default_9x9(current_sudoku_board):
    global default_value_9x9
    for i in range(len(current_sudoku_board)):
            for j in range(len(current_sudoku_board)):
                if current_sudoku_board[i][j] != 0:
                    default_value_9x9.append((j,i))
def set_default_16x16(current_sudoku_board):
    global default_value_16x16
    for i in range(len(current_sudoku_board)):
            for j in range(len(current_sudoku_board)):
                if current_sudoku_board[i][j] != 0:
                    default_value_16x16.append((j,i))
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
                if(j,i) not in default_value_4x4:
                    text = font.render(str(current_sudoku_board[i][j]), True, (144, 238, 144))
                else:
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
    elif current_sudoku_board == sudoku_9x9:
        draw_board_9x9(screen, current_sudoku_board)
    elif current_sudoku_board == sudoku_16x16:
        draw_board_16x16(screen, current_sudoku_board)


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
    not_suggest_value_4x4 = []
    suggest_value_4x4 = []
    for ii in range(4):
        if(ii != j):
            if sudoku_4x4[ii][i] != sudoku_4x4[int(j)][int(i)]:
                not_suggest_value_4x4.append(sudoku_4x4[ii][i])
    for kk in range(1,5):
        if kk in not_suggest_value_4x4:
            continue
        else:
            suggest_value_4x4.append(kk)
    DisplayMessage(f'Suggest: {suggest_value_4x4}', 500, (255, 255, 255))

def Suggest_Value_9x9_column(i,j):
    not_suggest_value_9x9 = []
    suggest_value_9x9 = []
    for ii in range(4):
        if(ii != j):
            if sudoku_9x9[ii][i] != sudoku_9x9[int(j)][int(i)]:
                not_suggest_value_9x9.append(sudoku_9x9[ii][i])
    for kk in range(1,5):
        if kk in not_suggest_value_9x9:
            continue
        else:
            suggest_value_9x9.append(kk)
    DisplayMessage(f'Suggest: {suggest_value_9x9}', 500, (255, 255, 255))

def Suggest_Value_16x16_column(i,j):
    not_suggest_value_16x16 = []
    suggest_value_16x16 = []
    for ii in range(4):
        if(ii != j):
            if sudoku_16x16[ii][i] != sudoku_16x16[int(j)][int(i)]:
                not_suggest_value_16x16.append(sudoku_16x16[ii][i])
    for kk in range(1,5):
        if kk in not_suggest_value_16x16:
            continue
        else:
            suggest_value_16x16.append(kk)
    DisplayMessage(f'Suggest: {suggest_value_16x16}', 500, (255, 255, 255))


def IsValueValid_4x4(i, j):
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
def IsValueValid_9x9(i, j):
    for ii in range(4):
        if ii != j:
            if sudoku_9x9[i][ii] == sudoku_9x9[int(i)][int(j)]:  # checks cols and rows
                return False
    for ii in range(4):
        if ii != i:
            if sudoku_9x9[ii][j] == sudoku_9x9[int(i)][int(j)]:  # checks cols and rows
                return False
    # checks the box/block
    ii = i // 2
    jj = j // 2
    for a in range(ii * 2, ii * 2 + 2):
        for b in range(jj * 2, jj * 2 + 2):
            if a != j:
                if sudoku_9x9[i][a] == sudoku_9x9[int(i)][int(j)]:
                    return False
    for a in range(ii * 2, ii * 2 + 2):
        for b in range(jj * 2, jj * 2 + 2):
            if b != i:
                if sudoku_9x9[b][j] == sudoku_9x9[int(i)][int(j)]:
                    return False
    return True
def IsValueValid_16x16(i, j):
    for ii in range(4):
        if ii != j:
            if sudoku_16x16[i][ii] == sudoku_16x16[int(i)][int(j)]:  # checks cols and rows
                return False
    for ii in range(4):
        if ii != i:
            if sudoku_16x16[ii][j] == sudoku_16x16[int(i)][int(j)]:  # checks cols and rows
                return False
    # checks the box/block
    ii = i // 2
    jj = j // 2
    for a in range(ii * 2, ii * 2 + 2):
        for b in range(jj * 2, jj * 2 + 2):
            if a != j:
                if sudoku_16x16[i][a] == sudoku_16x16[int(i)][int(j)]:
                    return False
    for a in range(ii * 2, ii * 2 + 2):
        for b in range(jj * 2, jj * 2 + 2):
            if b != i:
                if sudoku_16x16[b][j] == sudoku_16x16[int(i)][int(j)]:
                    return False
    return True

def IsUserWin_4x4():
    for i in range(4):
        for j in range(4):
            if IsValueValid_4x4(i,j) == False:
                return False
    for i in range(4):
        for j in range(4):
            if sudoku_4x4[int(i)][int(j)] == 0:
                return False
    return True
def IsUserWin_9x9():
    for i in range(9):
        for j in range(9):
            if IsValueValid_9x9(i,j) == False:
                return False
    for i in range(9):
        for j in range(9):
            if sudoku_9x9[int(i)][int(j)] == 0:
                return False
    return True
def IsUserWin_16x16():
    for i in range(16):
        for j in range(16):
            if IsValueValid_16x16(i,j) == False:
                return False
    for i in range(16):
        for j in range(16):
            if sudoku_16x16[int(i)][int(j)] == 0:
                return False
    return True

# message
def DisplayMessage(Message, Interval, Color):
    screen.blit(a_font.render(Message, True, Color), (112, 210))
    pygame.display.update()
    pygame.time.delay(Interval)

# insert value entered by user 4x4
def InsertValue_4x4(Value):
    global default_value_4x4
    if (x,y) not in default_value_4x4:
        sudoku_4x4[int(y)][int(x)] = Value
        if Value != 0:
            text = a_font.render(str(Value), True, (144, 238, 144))
        else:
            text = a_font.render('', True, (0, 0, 0))
        # screen.blit(text, (x * inc + 15, y * inc + 15))
        screen.blit(text, (x * inc_4x4 + 15, y * inc_4x4 + 250 + 15))
    print(default_value_4x4)
# insert value entered by user 9x9
def InsertValue_9x9(Value):
    global default_value_9x9
    if (x,y) not in default_value_9x9:
        sudoku_9x9[int(y)][int(x)] = Value
        if Value != 0:
            text = a_font.render(str(Value), True, (144, 238, 144))
        else:
            text = a_font.render('', True, (0, 0, 0))
        # screen.blit(text, (x * inc + 15, y * inc + 15))
        screen.blit(text, (x * inc_9x9 + 8, y * inc_9x9 + 250 + 8))
    print(default_value_9x9)
# insert value entered by user 16x16
def InsertValue_16x16(Value):
    global default_value_16x16
    if (x,y) not in default_value_16x16:
        sudoku_16x16[int(y)][int(x)] = Value
        if Value != 0:
            text = a_font.render(str(Value), True, (144, 238, 144))
        else:
            text = a_font.render('', True, (0, 0, 0))
        # screen.blit(text, (x * inc + 15, y * inc + 15))
        screen.blit(text, (x * inc_16x16 + 3, y * inc_16x16 + 250 + 3))
    print(default_value_16x16)
# setting the initial position
def SetMousePosition_4x4(p):
    global x, y
    if p[0] < 450 and p[1] < 700 and p[1] >250:
        print(p[0])
        print(p[1])
        x = p[0] // inc_4x4
        y = (p[1]-280) // inc_4x4
        Suggest_Value_4x4_column(x,y)
# setting the initial position
def SetMousePosition_9x9(p):
    global x, y
    if p[0] < 450 and p[1] < 700 and p[1] >250:
        print(p[0])
        print(p[1])
        x = p[0] // inc_9x9
        y = (p[1]-260) // inc_9x9
        Suggest_Value_9x9_column(x,y)
# setting the initial position
def SetMousePosition_16x16(p):
    global x, y
    if p[0] < 450 and p[1] < 700 and p[1] >250:
        print(p[0])
        print(p[1])
        x = p[0] // inc_16x16
        y = (p[1]-250) // inc_16x16
        Suggest_Value_16x16_column(x,y)
def DrawSelectedBox_4x4():
    for i in range(2):
        pygame.draw.line(screen, (0, 0, 255), (x * inc_4x4, (y + i) * inc_4x4 + 250), (x * inc_4x4 + inc_4x4, (y + i) * inc_4x4+250), 5)
        pygame.draw.line(screen, (0, 0, 255), ((x + i) * inc_4x4, y * inc_4x4+250), ((x + i) * inc_4x4, y * inc_4x4 + inc_4x4+250), 5)
def DrawSelectedBox_9x9():
    for i in range(2):
        pygame.draw.line(screen, (0, 0, 255), (x * inc_9x9, (y + i) * inc_9x9 + 250), (x * inc_9x9 + inc_9x9, (y + i) * inc_9x9+250), 3)
        pygame.draw.line(screen, (0, 0, 255), ((x + i) * inc_9x9, y * inc_9x9+250), ((x + i) * inc_9x9, y * inc_9x9 + inc_9x9+250), 3)
def DrawSelectedBox_16x16():
    for i in range(2):
        pygame.draw.line(screen, (0, 0, 255), (x * inc_16x16, (y + i) * inc_16x16 + 250), (x * inc_16x16 + inc_16x16, (y + i) * inc_16x16+250), 2)
        pygame.draw.line(screen, (0, 0, 255), ((x + i) * inc_16x16, y * inc_16x16+250), ((x + i) * inc_16x16, y * inc_16x16 + inc_16x16+250), 2)
def DrawUserValue():
    global UserValue
    if(current_sudoku_board == sudoku_4x4):
        if UserValue >= 0 and UserValue <=4:
            InsertValue_4x4(UserValue)
            if IsUserWin_4x4():
                DisplayMessage("YOU WON!!!!", 5000, (255, 255, 255))
    elif(current_sudoku_board == sudoku_9x9):
        if UserValue >= 0 and UserValue <=9:
            InsertValue_9x9(UserValue)
            if IsUserWin_9x9():
                DisplayMessage("YOU WON!!!!", 5000, (255, 255, 255))
    else:
        if UserValue >= 0 and UserValue <=16:
            InsertValue_16x16(UserValue)
            if IsUserWin_16x16():
                DisplayMessage("YOU WON!!!!", 5000, (255, 255, 255))
# Main function
def main():
    # scramble()
    global x, y, UserValue, screen, a_font, inc_4x4, inc_9x9, inc_16x16
    global current_sudoku_board, sudoku_4x4, sudoku_9x9, sudoku_16x16
    global default_value_4x4, default_value_9x9, default_value_16x16
    global board_mode 
    board_mode = 0
    default_value_4x4 = []
    default_value_9x9 = []
    default_value_16x16 = []
    if board_mode == 1:
        current_sudoku_board = sudoku_4x4
    elif board_mode == 2:
        current_sudoku_board = sudoku_9x9
    elif board_mode == 3:
        current_sudoku_board = sudoku_16x16
    else:
        current_sudoku_board = sudoku_4x4


    if(current_sudoku_board == sudoku_4x4):
        set_default_4x4(current_sudoku_board)
    elif(current_sudoku_board == sudoku_9x9):
        set_default_9x9(current_sudoku_board)
    else:
        set_default_16x16(current_sudoku_board)
    
    # Initialize the Pygame screen
    screen = pygame.display.set_mode((horizontal_size, vertical_size + 1))
    pygame.display.set_caption("Sudoku")
    inc_4x4 = 450//4
    inc_9x9 = 450//9
    inc_16x16 = 450//16
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
                if(current_sudoku_board == sudoku_4x4):
                    SetMousePosition_4x4(mouse_pos)
                elif(current_sudoku_board == sudoku_9x9):
                    SetMousePosition_9x9(mouse_pos)
                else:
                    SetMousePosition_16x16(mouse_pos)
                for i, rect in enumerate(button_rectangles):
                    if rect.collidepoint(mouse_pos):
                        if i == 0: 
                            current_sudoku_board = sudoku_4x4
                            board_mode = 1
                        elif i==1:
                            current_sudoku_board = sudoku_9x9
                            board_mode = 2
                        elif i==2:
                            current_sudoku_board = sudoku_16x16
                            board_mode = 3
                        elif i==3:
                            if(current_sudoku_board == sudoku_4x4):
                                scramble_4x4()
                                board_mode = 1
                                main()
                            elif(current_sudoku_board == sudoku_9x9):
                                scramble_9x9()
                                board_mode = 2
                                main()
                            else:
                                scramble_16x16()
                                board_mode = 3
                                main()
                        elif i==4:
                            clear_4x4()
                            clear_9x9()
                            clear_16x16()
                            main()
                        elif i==5:# Exit button
                            pygame.quit()
                            sys.exit()
                        elif i==6:
                            solve_sudoku_dfs(current_sudoku_board)
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
                if event.key == pygame.K_a:
                    UserValue = 10
                    DrawUserValue()
                if event.key == pygame.K_b:
                    UserValue = 11
                    DrawUserValue()
                if event.key == pygame.K_c:
                    UserValue = 12
                    DrawUserValue()
                if event.key == pygame.K_d:
                    UserValue = 13
                    DrawUserValue()
                if event.key == pygame.K_e:
                    UserValue = 14
                    DrawUserValue()
                if event.key == pygame.K_f:
                    UserValue = 15
                    DrawUserValue()
                if event.key == pygame.K_g:
                    UserValue = 16
                    DrawUserValue()
                if event.key == pygame.K_DELETE:
                    UserValue = 0
                    DrawUserValue()

        # Draw the Sudoku board based on the current selected board
        button_rectangles = draw_board(screen)
        if(current_sudoku_board == sudoku_4x4):
            DrawSelectedBox_4x4()
        elif(current_sudoku_board == sudoku_9x9):
            DrawSelectedBox_9x9()
        else:
            DrawSelectedBox_16x16()
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()

