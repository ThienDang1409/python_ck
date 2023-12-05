import pygame
import sys
import index


# Khởi tạo Pygame
pygame.init()
history_player = []
# Cấu hình màn hình
width, height = 600, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Home")
#Cấu hình background
background_image_path = "image/history.png"
background_image_load = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image_load, (width,height))
# Cấu hình màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
font_color = (32,216,75)

# Cấu hình font chữ
font_title = pygame.font.Font(None, 40)
font_button = pygame.font.Font(None, 30)
font_history = pygame.font.Font(None, 22)
# Hàm vẽ trang chủ
def draw_home():
    screen.fill(white)
    screen.blit(background_image,(0,0))
    # Vẽ tiêu đề "SUDOKU"
    title_text = font_title.render("HISTORY", True, font_color)
    title_rect = title_text.get_rect(center=(width // 2, 30))
    screen.blit(title_text, title_rect)
    
    # Vẽ các nút
    button_rects = []

    button_text = font_button.render("Exit", True, font_color)
    button_rect = button_text.get_rect(center=(width // 2, 680))
    button_rects.append(button_rect)
    screen.blit(button_text, button_rect)

    return button_rects

# Hàm chính
def main():
    for i, entry in enumerate(history_player, 1):
        print(f"Game {entry.board}: Start Time: {entry.algorithm}, End Time: {entry.count_step}, Solved Correctly: {entry.time_play}")
      # Điều chỉnh vị trí dựa trên số lượng mục

    pygame.display.flip()
    while True:
        screen.blit(background_image,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                index.main()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(button_rectangles):
                    if rect.collidepoint(mouse_pos):
                        if i == 0: 
                            index.main()
        button_rectangles = draw_home()
        for i, entry in enumerate(history_player, 1):
            text = font_history.render(f"[{i}]   Board: {entry.board} Algorithm: {entry.algorithm} Count step: {entry.count_step} Time play: {entry.time_play}", True, (223,238,197))
            screen.blit(text, (95 , 40 + i * 30))
        pygame.display.flip()

if __name__ == "__main__":
    main()
