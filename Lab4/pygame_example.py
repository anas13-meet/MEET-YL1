import pygame 

class MySurface(pygame.Surface):
	screen_size = 400
	main_screen = pygame.display.set_mode((400, 400))
	main_screen.fill((0,0,144))
	polygon= pygame.draw.polygon(screen, colors[body.type], vertices, 1)


if __name__=="__main__":
    pygame.init()
    screen_size = 400
    main_screen = pygame.display.set_mode((screen_size, screen_size))
    main_screen.fill((255,255,255))
    square = pygame.Surface([20, 20])

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            if square.get_bounding_rect().collidepoint(x, y):
                print "clicked"
        main_screen.blit(square, (0, 0))
        pygame.display.flip()