@namespace
class SpriteKind:
    pet = SpriteKind.create()
    vehichle = SpriteKind.create()

def on_overlap_tile(sprite, location):
    tiles.set_tile_at(location, sprites.dungeon.floor_dark2)
    music.ba_ding.play()
    info.start_countdown(10)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    global winning_points
    if key == 3:
        Riley.destroy()
        scene.set_background_color(1)
        tiles.set_tilemap(tilemap("""
            level9
        """))
        winning_points += 1
        info.stop_countdown()
    else:
        game.splash("door is locked")
    if winning_points2 == 1:
        game.splash("press the spacebar to continue")
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_locked_north,
    on_overlap_tile2)

def on_overlap_tile3(sprite, location):
    global key, winning_points2
    if key == 2:
        music.small_crash.play()
        tiles.set_tilemap(tilemap("""
            level8
        """))
        tiles.place_on_random_tile(Riley, sprites.dungeon.stair_east)
        key = 0
        winning_points2 = 0
        info.start_countdown(10)
    else:
        game.splash("door is locked")
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_closed_east,
    on_overlap_tile3)

def on_b_pressed():
    if losing_points == 1:
        game.over(False)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    if winning_points == 1:
        game.over(True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    global losing_points
    music.stop_all_sounds()
    scene.set_background_color(15)
    tiles.set_tilemap(tilemap("""
        level2
    """))
    tiles.place_on_random_tile(Riley, assets.tile("""
        transparency16
    """))
    Riley.destroy()
    scene.camera_shake(4, 2000)
    losing_points += 1
info.on_countdown_end(on_countdown_end)

def on_overlap_tile4(sprite, location):
    global key
    if key == 2:
        music.small_crash.play()
        tiles.set_tilemap(tilemap("""
            level7
        """))
        tiles.place_on_random_tile(Riley, sprites.dungeon.stair_south)
        key = 0
        info.start_countdown(10)
    else:
        game.splash("door is locked")
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_closed_south,
    on_overlap_tile4)

def on_overlap_tile5(sprite, location):
    global key
    tiles.set_tile_at(location, sprites.dungeon.floor_dark2)
    key += 1
    music.beam_up.play()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile5)

winning_points2 = 0
winning_points = 0
losing_points = 0
key = 0
Riley: Sprite = None
camera_shake = 0
tiles.set_tilemap(tilemap("""
    level1
"""))
Riley = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . f f f f f f f . . . . . 
            . . . . f f c c c c d f f . . . 
            . . f f f f f c c c c d d f . . 
            . . f f f f f f c c c c d f . . 
            . . f f f f f f f f f c d f . . 
            . . f f f e e f f e e f d f . . 
            . . f f f b 8 4 f 8 b f f f . . 
            . . f f e 1 9 4 4 9 1 e f f . . 
            . . . f f 4 4 4 4 4 4 f f . . . 
            . . . f f f e e e e f f f . . . 
            . . e e f f 9 9 9 9 f f e e . . 
            . . e 4 e 9 9 9 9 9 9 e 4 e . . 
            . . e e e 6 6 6 6 6 6 e e e . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
key = 0
losing_points = 0
winning_points = 0
tiles.place_on_random_tile(Riley, sprites.dungeon.stair_south)
info.set_life(1)
controller.move_sprite(Riley, 100, 100)
scene.camera_follow_sprite(Riley)
info.start_countdown(10)

def on_forever():
    music.play_melody("E G D F B A F D ", 320)
forever(on_forever)
