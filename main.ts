namespace SpriteKind {
    export const pet = SpriteKind.create()
    export const vehichle = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    tiles.setTileAt(location, sprites.dungeon.floorDark2)
    music.baDing.play()
    info.startCountdown(10)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.doorLockedNorth, function (sprite, location) {
    if (key == 3) {
        Riley.destroy()
        scene.setBackgroundColor(1)
        tiles.setTilemap(tilemap`level9`)
        winning_points += 1
        info.stopCountdown()
    } else {
        game.splash("door is locked")
    }
    if (winning_points2 == 1) {
        game.splash("press the spacebar to continue")
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.doorClosedEast, function (sprite, location) {
    if (key == 2) {
        music.smallCrash.play()
        tiles.setTilemap(tilemap`level8`)
        tiles.placeOnRandomTile(Riley, sprites.dungeon.stairEast)
        key = 0
        winning_points2 = 0
        info.startCountdown(10)
    } else {
        game.splash("door is locked")
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (losing_points == 1) {
        game.over(false)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (winning_points == 1) {
        game.over(true)
    }
})
info.onCountdownEnd(function () {
    music.stopAllSounds()
    scene.setBackgroundColor(15)
    tiles.setTilemap(tilemap`level2`)
    tiles.placeOnRandomTile(Riley, assets.tile`transparency16`)
    Riley.destroy()
    scene.cameraShake(4, 2000)
    losing_points += 1
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.doorClosedSouth, function (sprite, location) {
    if (key == 2) {
        music.smallCrash.play()
        tiles.setTilemap(tilemap`level7`)
        tiles.placeOnRandomTile(Riley, sprites.dungeon.stairSouth)
        key = 0
        info.startCountdown(10)
    } else {
        game.splash("door is locked")
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile2`, function (sprite, location) {
    tiles.setTileAt(location, sprites.dungeon.floorDark2)
    key += 1
    music.beamUp.play()
})
let winning_points2 = 0
let winning_points = 0
let losing_points = 0
let key = 0
let Riley: Sprite = null
let camera_shake = 0
tiles.setTilemap(tilemap`level1`)
Riley = sprites.create(img`
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
    `, SpriteKind.Player)
key = 0
losing_points = 0
winning_points = 0
let death_point = 0
tiles.placeOnRandomTile(Riley, sprites.dungeon.stairSouth)
info.setLife(1)
controller.moveSprite(Riley, 100, 100)
scene.cameraFollowSprite(Riley)
info.startCountdown(10)
forever(function () {
    music.playMelody("G C G B G B C5 B ", 180)
})
