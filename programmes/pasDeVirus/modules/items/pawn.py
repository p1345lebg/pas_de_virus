import pygame
from programmes.components import Button


class Part(Button):
    def __init__(self, screen : pygame.Surface, positionPercent : tuple[int,int], pathTexture : str) -> None:
        """
            :param coordonates: coordonnnée du centre du cercle
            :param radius:      rayon du cercle
        """
        super().__init__(screen, positionPercent, (5,(1,1)), texture=pathTexture)

        self.hitbox = self.texture.get_rect()


    def get_hitbox(self) -> pygame.rect.Rect:
        return self.hitbox
    
    def is_touching_cursor(self):        
        return self.hitbox.collidepoint(pygame.mouse.get_pos())
    
    def move(self, x,y):
        self.position = (self.position[0]+x,self.position[1]+y)




class Pawn():
    def __init__(self, screen, coordonatesList : list[tuple], PATH_TEXTURE : str, canMove = True, player : bool = False):
        """
        pawn dans le jeu.

        Args:
            coordonatesList (list): Liste des coordonnées de chaque parties du pion.
            PATH_TEXTURE (str): chemin vers la texture du pions

        """
        self.screen = screen
        self.parts : list = []
        for coordonate in coordonatesList:
            self.parts.append(Part(self.screen, ))
        self.TEXTURE = pygame.image.load(PATH_TEXTURE).convert_alpha()
        self.pawns : list[Part] = []
        self.isMoving = False

        self.moveR = False


    def is_touching_cursor(self):
        """
            regarde si le pion touche un point
        """
        for pawn in self.pawns:
            if pawn.get_hitbox().collidepoint(pygame.mouse.get_pos()):
                return True
        return False


    def colliding(self, rect: pygame.rect.Rect):
        """
            regarde si un carré entre en colision avec le point
        """
        for pawn in self.pawns:
            if pawn.get_hitbox().colliderect(rect):
                return True
        return False

    
    def move(self, d: int, otherPawns: list):
        """
            Moves the pawn.

            Args:
                d (int): Distace de deplacement du pion.
                otherPawns (list(Pawn)): Liste des pions du niveau.
        """
        if self in otherPawns:
            otherPawns.remove(self)

        d = int(d)
        dSign = -1 if d < 0 else 1
        d *= dSign

        move = True
        doBreak = False

        for i in range(d):
            self.apply_move(dSign)
            for otherPawn in otherPawns:
                otherPawn : Pawn
                otherPawn.moveR = self.moveR
                for part in self.pawns:
                    if otherPawn.colliding(part.get_hitbox()):                    
                        if (not otherPawn.canMove) or (not otherPawn.move(dSign, otherPawns)):
                            self.apply_move(-dSign)
                            move = False
                            doBreak = True

                            
                if doBreak:
                    break
            if doBreak:
                break
        return move

    def apply_move(self, distance):
        for pawn in self.pawns:
            if self.movep:
                pawn.move(distance,-distance)
            else:
                pawn.move(distance,distance)


    def draw(self):
        for pawn in self.pawns:
            pawn.draw()