import pygame
import random
import sys

# Pygame-ce'yi başlat
pygame.init()

# Sabitler ve Ayarlar
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20

# Renkler (RGB)
BLACK = (20, 20, 20)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
WHITE = (236, 240, 241)
GRAY = (127, 140, 141)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Yılan Oyunu (Pygame-ce)")
clock = pygame.time.Clock()

# Fontlar
font_score = pygame.font.SysFont("arial", 22, bold=True)
font_game_over = pygame.font.SysFont("arial", 36, bold=True)

def spawn_food(snake):
    while True:
        x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        # Yem yılanın gövdesinde çıkmasın
        if (x, y) not in snake:
            return (x, y)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def game_loop():
    # Yılanın gövdesi: [Baş, Gövde, Kuyruk] -> Sağa doğru sıralı
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0) # Sağa doğru hareket
    next_direction = direction # Hızlı tuş basımlarında çakışmayı önlemek için
    
    food = spawn_food(snake)
    score = 0
    game_over = False

    while True:
        # 1. ETKİNLİK DÖNGÜSÜ
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_SPACE:
                        game_loop()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                else:
                    # Bir kare içinde tek yön değişimi için next_direction kullanıyoruz
                    if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                        next_direction = (0, -GRID_SIZE)
                    elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                        next_direction = (0, GRID_SIZE)
                    elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                        next_direction = (-GRID_SIZE, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                        next_direction = (GRID_SIZE, 0)

        # 2. OYUN MANTIĞI
        if not game_over:
            direction = next_direction # Yönü güncelle
            head_x, head_y = snake[0]
            dir_x, dir_y = direction
            new_head = (head_x + dir_x, head_y + dir_y)

            # Çarpmaları Kontrol Et (Duvarlar)
            if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT):
                game_over = True

            # Çarpmaları Kontrol Et (Kendi Gövdesi - Son kuyruk parçası hariç çünkü o adımda kayacak)
            elif new_head in snake[:-1]:
                game_over = True

            if not game_over:
                snake.insert(0, new_head)

                # Yem Yenme Kontrolü
                if new_head == food:
                    score += 10
                    food = spawn_food(snake)
                else:
                    snake.pop()

        # 3. EKRAN ÇİZİMİ
        screen.fill(BLACK)

        # Yılanı Çiz
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE - 1, GRID_SIZE - 1))

        # Yemi Çiz
        pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE - 1, GRID_SIZE - 1))

        # Skoru Çiz
        score_text = font_score.render(f"Skor: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Game Over Ekranı
        if game_over:
            draw_text("OYUN BİTTİ!", font_game_over, RED, screen, WIDTH // 2, HEIGHT // 2 - 30)
            draw_text("Yeniden Başlamak İçin SPACE'e Basın", font_score, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 10)
            draw_text("Çıkmak İçin ESC'ye Basın", font_score, GRAY, screen, WIDTH // 2, HEIGHT // 2 + 40)

        pygame.display.flip()
        
        # Oyun Hızı (10 FPS)
        clock.tick(10)

if __name__ == "__main__":
    game_loop()