import pygame
import sys
import singleplayer
import coopplayer


# Khởi tạo Pygame
pygame.init()

# Cấu hình màn hình
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Home")
#Cấu hình background
background_image_path = "image/playervsma.jpg"
background_image_load = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image_load, (width,height))
# Cấu hình màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
font_color = (153, 51, 255)

# Cấu hình font chữ
font_title = pygame.font.Font(None, 64)
font_button = pygame.font.Font(None, 36)

# Hàm vẽ trang chủ
def draw_home():
    screen.fill(white)
    screen.blit(background_image,(0,0))
    # Vẽ tiêu đề "SUDOKU"
    title_text = font_title.render("SUDOKU", True, (127,0,255))
    title_rect = title_text.get_rect(center=(width // 2, height // 4))
    screen.blit(title_text, title_rect)
    
    # Vẽ các nút
    button_texts = ["1 Player", "2 Player", "Exit"]
    button_rects = []

    for i, text in enumerate(button_texts):
        button_text = font_button.render(text, True, font_color)
        button_rect = button_text.get_rect(center=(width // 2, height // 2 + i * 50))
        button_rects.append(button_rect)
        screen.blit(button_text, button_rect)

    return button_rects

# Hàm chính
def main():
    pygame.mixer.music.load("music/music.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(10)
    while True:
        screen.blit(background_image,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(button_rectangles):
                    if rect.collidepoint(mouse_pos):
                        if i == 0: 
                            pygame.mixer.music.stop()
                            singleplayer.main()
                        if i == 1:
                            pygame.mixer.music.stop()
                            coopplayer.main()
                        if i == 2:  # Exit button
                            pygame.quit()
                            sys.exit()

        button_rectangles = draw_home()
        pygame.display.flip()

if __name__ == "__main__":
    main()
