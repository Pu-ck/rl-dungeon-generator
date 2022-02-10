import tcod.event

# Main Entity parent class
class Entity:
    def __init__(self, position_x, position_y, char, color):
        self.position_x = position_x
        self.position_y = position_y
        self.char = char
        self.color = color


# Player child class
class Player(Entity):
    # Controlling player's object
    def movement(self):
        for event in tcod.event.get():
            if isinstance(event, tcod.event.KeyDown):
                if event.sym == tcod.event.K_w:
                    self.position_y -= 1
                    break
                elif event.sym == tcod.event.K_s:
                    self.position_y += 1
                    break
                elif event.sym == tcod.event.K_d:
                    self.position_x += 1
                    break
                elif event.sym == tcod.event.K_a:
                    self.position_x -= 1
                    break


# Wall child class
class Wall(Entity):
    pass


# Door child class
class Door(Entity):
    pass


# Map tile child class
class MapTile(Entity):
    is_occupied = False


# Room tile child class
class RoomTile(Entity):
    def __init__(self, position_x, position_y, char, color, background_color):
        Entity.__init__(self, position_x, position_y, char, color)
        self.background_color = background_color


# Water child class
class Water(Entity):
    pass


# Stairs leading down (dungeon's exit) child class
class StairsDown(Entity):
    pass


# Stairs leading up (dungeon's entrance) child class
class StairsUp(Entity):
    pass
