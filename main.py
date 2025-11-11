#!/usr/bin/env python3
import pygame
from src.state.state import State
from src.screens.menu import Menu

def main():
    # Initialize pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Jetpac")
    
    # Create game state
    state = State()
    
    # Initialize screens
    menu = Menu(screen, state)
    
    clock = pygame.time.Clock()
    running = True
    
    # Main game loop
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                # Route events to current screen based on location
                match state.location:
                    case 'menu':
                        menu.handle_event(event)
                    case 'l1':
                        # TODO: Add l1 screen event handling
                        pass
        
        # Update game state
        match state.location:
            case 'menu':
                menu.update()
            case 'l1':
                # TODO: Add l1 screen update
                pass
        
        # Render based on current location
        match state.location:
            case 'menu':
                menu.render()
            case 'l1':
                # TODO: Add l1 screen rendering
                screen.fill((0, 0, 0))
        
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(60)
    
    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()

