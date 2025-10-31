from pygame import*
init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image_normal = transform.scale(image.load(player_image), (size_x, size_y))
        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.active = False
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
    def update(self, mouse_pos, player_image_active,size_x,size_y):
        if self.rect.collidepoint(mouse_pos):
            self.active = not self.active
            self.image = self.image_active = transform.scale(image.load(player_image_active), (size_x, size_y)) if self.active else self.image_normal
    def reset(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))