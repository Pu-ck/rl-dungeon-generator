# Player-walls collision detection
def collision(player, wall_list, current_x, current_y):
    for wall in wall_list:
        if current_x > wall.position_x:
            if (
                player.position_x == wall.position_x
                and player.position_y == wall.position_y
            ):
                player.position_x += 1
        if current_x < wall.position_x:
            if (
                player.position_x == wall.position_x
                and player.position_y == wall.position_y
            ):
                player.position_x -= 1
        if current_y < wall.position_y:
            if (
                player.position_x == wall.position_x
                and player.position_y == wall.position_y
            ):
                player.position_y -= 1
        if current_y > wall.position_y:
            if (
                player.position_x == wall.position_x
                and player.position_y == wall.position_y
            ):
                player.position_y += 1
