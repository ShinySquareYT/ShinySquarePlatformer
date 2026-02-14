@namespace
class SpriteKind:
    PlayerComboPower = SpriteKind.create()
    DMGProj = SpriteKind.create()

def on_overlap_tile(sprite52, location5):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile2
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    global myEnemy
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile2
        """)):
        tiles.set_wall_at(value, True)
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile
        """)):
        for index in range(7):
            myEnemy = sprites.create(img("""
                    ........................
                    ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    .......f11111111f.......
                    ......fd11111111df......
                    ......fd11111111df......
                    ......fddd1111dddf......
                    ......fbdbfddfbdbf......
                    ......fcdcf11fcdcf......
                    .......fb111111bf.......
                    ......fffcdb1bdffff.....
                    ....fc111cbfbfc111cf....
                    ....f1b1b1ffff1b1b1f....
                    ....fbfbffffffbfbfbf....
                    .........ffffff.........
                    ...........fff..........
                    ........................
                    ........................
                    ........................
                    ........................
                    """),
                SpriteKind.enemy)
            tiles.place_on_tile(myEnemy, value2)
            myEnemy.ay = 500
            enemyMove()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
        """),
    on_overlap_tile2)

def enemyMove():
    if randint(1, 2) == 1:
        animation.run_image_animation(myEnemy,
            [img("""
                    ........................
                    ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    .......f1111111df.......
                    ......fd1111111ddf......
                    ......fd111111dddf......
                    ......fd111ddddddf......
                    ......fd1dfbddddbf......
                    ......fbddfcdbbbcf......
                    .......f11111bbcf.......
                    .......f1b1fffff........
                    .......fbfc111bf........
                    ........ff1b1bff........
                    .........fbfbfff.f......
                    ..........ffffffff......
                    ............fffff.......
                    ........................
                    ........................
                    ........................
                    ........................
                    """),
                img("""
                    ........................
                    ........................
                    ........................
                    ........................
                    .........fffff..........
                    ........f11111ff........
                    .......fb111111bf.......
                    .......f1111111dbf......
                    ......fd111111dddf......
                    ......fd11111ddddf......
                    ......fd11dddddddf......
                    ......f111dddddddf......
                    ......f11fcddddddf......
                    .....fb1111bdddbf.......
                    .....f1b1bdfcfff........
                    .....fbfbffffffff.......
                    ......fffffffffff.ff....
                    ...........ffffffff.....
                    ........f1b1bffffff.....
                    ........fbfbffffff......
                    ........................
                    ........................
                    ........................
                    ........................
                    """)],
            200,
            True)
        myEnemy.vx = -30
    else:
        animation.run_image_animation(myEnemy,
            [img("""
                    ........................
                    ........................
                    ........................
                    ........................
                    ..........fffff.........
                    ........ff11111f........
                    .......fb111111bf.......
                    ......fbd1111111f.......
                    ......fddd111111df......
                    ......fdddd11111df......
                    ......fddddddd11df......
                    ......fddddddd111f......
                    ......fddddddcf11f......
                    .......fbdddb1111bf.....
                    ........fffcfdb1b1f.....
                    .......ffffffffbfbf.....
                    ....ff.fffffffffff......
                    .....ffffffff...........
                    .....ffffffb1b1f........
                    ......ffffffbfbf........
                    ........................
                    ........................
                    ........................
                    ........................
                    """),
                img("""
                    ........................
                    ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    .......fd1111111f.......
                    ......fdd1111111df......
                    ......fddd111111df......
                    ......fdddddd111df......
                    ......fbddddbfd1df......
                    ......fcbbbdcfddbf......
                    .......fcbb11111f.......
                    ........fffff1b1f.......
                    ........fb111cfbf.......
                    ........ffb1b1ff........
                    ......f.fffbfbf.........
                    ......ffffffff..........
                    .......fffff............
                    ........................
                    ........................
                    ........................
                    ........................
                    """)],
            200,
            True)
        myEnemy.vx = 30

def on_up_pressed():
    if mySprite.vy == 0:
        mySprite.vy = -200
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_combos_attach_combo():
    pass
controller.combos.attach_combo("a", on_combos_attach_combo)

def on_on_overlap(sprite62, otherSprite3):
    otherSprite3.destroy()
    if sprite62.bottom < otherSprite3.y:
        sprite62.vy = -100
    else:
        hpbar.value += -20
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite3, otherSprite):
    sprites.destroy(sprite3)
    sprites.destroy(projectile)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap2)

def on_combos_attach_combo2():
    pass
controller.combos.attach_combo("b", on_combos_attach_combo2)

def on_on_overlap3(sprite6, otherSprite2):
    if randint(1, 2) == 1:
        animation.run_image_animation(otherSprite2,
            [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . 7 . 2 7 . . . . . .
                . . . . . . 7 2 . 7 . . . . . .
                . . . . . . 7 . 2 7 . . . . . .
                . . . . . . 7 2 . 7 . . . . . .
                . . . . . . 7 . 2 7 . . . . . .
                . . . . . . 7 2 . 7 . . . . . .
                . . . . . . 7 . 2 7 . . . . . .
                . . . . . . 7 2 2 7 . . . . . .
                . . . . . . 7 2 2 7 . . . . . .
                """)],
            500,
            False)
        hpbar.value += -20
        sprites.destroy(otherSprite2)
    else:
        sprites.destroy(otherSprite2)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

def on_overlap_tile3(sprite32, location3):
    tiles.set_tile_at(location3, assets.tile("""
        transparency16
        """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile6
        """),
    on_overlap_tile3)

def on_a_pressed():
    global projectile, dashing
    if not (dashing) and statusbar.value == statusbar.max:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            mySprite,
            0,
            0)
        projectile.set_scale(5, ScaleAnchor.MIDDLE)
        animation.run_image_animation(projectile,
            [img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . 4 4 . . . . . . .
                    . . . . . . 4 5 5 4 . . . . . .
                    . . . . . . 2 5 5 2 . . . . . .
                    . . . . . . . 2 2 . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . 4 . . . . .
                    . . . . 2 . . . . 4 4 . . . . .
                    . . . . 2 4 . . 4 5 4 . . . . .
                    . . . . . 2 4 d 5 5 4 . . . . .
                    . . . . . 2 5 5 5 5 4 . . . . .
                    . . . . . . 2 5 5 5 5 4 . . . .
                    . . . . . . 2 5 4 2 4 4 . . . .
                    . . . . . . 4 4 . . 2 4 4 . . .
                    . . . . . 4 4 . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . 3 . . . . . . . . . . . 4 . .
                    . 3 3 . . . . . . . . . 4 4 . .
                    . 3 d 3 . . 4 4 . . 4 4 d 4 . .
                    . . 3 5 3 4 5 5 4 4 d d 4 4 . .
                    . . 3 d 5 d 1 1 d 5 5 d 4 4 . .
                    . . 4 5 5 1 1 1 1 5 1 1 5 4 . .
                    . 4 5 5 5 5 1 1 5 1 1 1 d 4 4 .
                    . 4 d 5 1 1 5 5 5 1 1 1 5 5 4 .
                    . 4 4 5 1 1 5 5 5 5 5 d 5 5 4 .
                    . . 4 3 d 5 5 5 d 5 5 d d d 4 .
                    . 4 5 5 d 5 5 5 d d d 5 5 4 . .
                    . 4 5 5 d 3 5 d d 3 d 5 5 4 . .
                    . 4 4 d d 4 d d d 4 3 d d 4 . .
                    . . 4 5 4 4 4 4 4 4 4 4 4 . . .
                    . 4 5 4 . . 4 4 4 . . . 4 4 . .
                    . 4 4 . . . . . . . . . . 4 4 .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . b b . b b b . . . . .
                    . . . . b 1 1 b 1 1 1 b . . . .
                    . . b b 3 1 1 d d 1 d d b b . .
                    . b 1 1 d d b b b b b 1 1 b . .
                    . b 1 1 1 b . . . . . b d d b .
                    . . 3 d d b . . . . . b d 1 1 b
                    . b 1 d 3 . . . . . . . b 1 1 b
                    . b 1 1 b . . . . . . b b 1 d b
                    . b 1 d b . . . . . . b d 3 d b
                    . b b d d b . . . . b d d d b .
                    . b d d d d b . b b 3 d d 3 b .
                    . . b d d 3 3 b d 3 3 b b b . .
                    . . . b b b d d d d d b . . . .
                    . . . . . . b b b b b . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """)],
            100,
            False)
        dashing = True
        controller.move_sprite(mySprite, 0, 0)
        if controller.up.is_pressed():
            if standingStill:
                mySprite.set_velocity(0, 0 - dashSpeed)
            elif isFacingLeft:
                mySprite.set_velocity(0 - Math.sqrt(2) / 2 * dashSpeed,
                    0 - Math.sqrt(2) / 2 * dashSpeed)
            else:
                mySprite.set_velocity(Math.sqrt(2) / 2 * dashSpeed,
                    0 - Math.sqrt(2) / 2 * dashSpeed)
        elif isFacingLeft:
            mySprite.set_velocity(0 - dashSpeed, 0)
        else:
            mySprite.set_velocity(dashSpeed, 0)
        mySprite.start_effect(effects.trail)
        mySprite.start_effect(effects.trail)
        mySprite.start_effect(effects.trail)
        statusbar.value = 0
        
        def on_after():
            global dashing, projectile
            dashing = False
            mySprite.vx = 0
            controller.move_sprite(mySprite, 100, 0)
            effects.clear_particles(mySprite)
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                mySprite,
                0,
                0)
            projectile.set_scale(5, ScaleAnchor.MIDDLE)
            animation.run_image_animation(projectile,
                [img("""
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . 4 4 . . . . . . .
                        . . . . . . 4 5 5 4 . . . . . .
                        . . . . . . 2 5 5 2 . . . . . .
                        . . . . . . . 2 2 . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        """),
                    img("""
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . 4 . . . . .
                        . . . . 2 . . . . 4 4 . . . . .
                        . . . . 2 4 . . 4 5 4 . . . . .
                        . . . . . 2 4 d 5 5 4 . . . . .
                        . . . . . 2 5 5 5 5 4 . . . . .
                        . . . . . . 2 5 5 5 5 4 . . . .
                        . . . . . . 2 5 4 2 4 4 . . . .
                        . . . . . . 4 4 . . 2 4 4 . . .
                        . . . . . 4 4 . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        """),
                    img("""
                        . 3 . . . . . . . . . . . 4 . .
                        . 3 3 . . . . . . . . . 4 4 . .
                        . 3 d 3 . . 4 4 . . 4 4 d 4 . .
                        . . 3 5 3 4 5 5 4 4 d d 4 4 . .
                        . . 3 d 5 d 1 1 d 5 5 d 4 4 . .
                        . . 4 5 5 1 1 1 1 5 1 1 5 4 . .
                        . 4 5 5 5 5 1 1 5 1 1 1 d 4 4 .
                        . 4 d 5 1 1 5 5 5 1 1 1 5 5 4 .
                        . 4 4 5 1 1 5 5 5 5 5 d 5 5 4 .
                        . . 4 3 d 5 5 5 d 5 5 d d d 4 .
                        . 4 5 5 d 5 5 5 d d d 5 5 4 . .
                        . 4 5 5 d 3 5 d d 3 d 5 5 4 . .
                        . 4 4 d d 4 d d d 4 3 d d 4 . .
                        . . 4 5 4 4 4 4 4 4 4 4 4 . . .
                        . 4 5 4 . . 4 4 4 . . . 4 4 . .
                        . 4 4 . . . . . . . . . . 4 4 .
                        """),
                    img("""
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . b b . b b b . . . . .
                        . . . . b 1 1 b 1 1 1 b . . . .
                        . . b b 3 1 1 d d 1 d d b b . .
                        . b 1 1 d d b b b b b 1 1 b . .
                        . b 1 1 1 b . . . . . b d d b .
                        . . 3 d d b . . . . . b d 1 1 b
                        . b 1 d 3 . . . . . . . b 1 1 b
                        . b 1 1 b . . . . . . b b 1 d b
                        . b 1 d b . . . . . . b d 3 d b
                        . b b d d b . . . . b d d d b .
                        . b d d d d b . b b 3 d d 3 b .
                        . . b d d 3 3 b d 3 3 b b b . .
                        . . . b b b d d d d d b . . . .
                        . . . . . . b b b b b . . . . .
                        """),
                    img("""
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        """)],
                100,
                False)
        timer.after(200, on_after)
        
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . c c c c c c . . . . . .
                . . . c 6 7 7 7 7 6 c . . . . .
                . . c 7 7 7 7 7 7 7 7 c . . . .
                . c 6 7 7 7 7 7 7 7 7 6 c . . .
                . c 7 c 6 6 6 6 c 7 7 7 c . . .
                . f 7 6 f 6 6 f 6 7 7 7 f . . .
                . f 7 7 7 7 7 7 7 7 7 7 f . . .
                . . f 7 7 7 7 6 c 7 7 6 f c . .
                . . . f c c c c 7 7 6 f 7 7 c .
                . . c 7 2 7 7 7 6 c f 7 7 7 7 c
                . c 7 7 2 7 7 c f c 6 7 7 6 c c
                c 1 1 1 1 7 6 f c c 6 6 6 c . .
                f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
                f 6 1 1 1 1 1 6 6 6 6 6 c f . .
                . f 6 1 1 1 1 1 1 6 6 6 f . . .
                . . c c c c c c c c c f . . . .
                """),
            img("""
                . . . c c c c c c . . . . . . .
                . . c 6 7 7 7 7 6 c . . . . . .
                . c 7 7 7 7 7 7 7 7 c . . . . .
                c 6 7 7 7 7 7 7 7 7 6 c . . . .
                c 7 c 6 6 6 6 c 7 7 7 c . . . .
                f 7 6 f 6 6 f 6 7 7 7 f . . . .
                f 7 7 7 7 7 7 7 7 7 7 f . . . .
                . f 7 7 7 7 6 c 7 7 6 f . . . .
                . . f c c c c 7 7 6 f c c c . .
                . . c 6 2 7 7 7 f c c 7 7 7 c .
                . c 6 7 7 2 7 7 c f 6 7 7 7 7 c
                . c 1 1 1 1 7 6 6 c 6 6 6 c c c
                . c 1 1 1 1 1 6 6 6 6 6 6 c . .
                . c 6 1 1 1 1 1 6 6 6 6 6 c . .
                . . c 6 1 1 1 1 1 7 6 6 c c . .
                . . . c c c c c c c c c c . . .
                """)],
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def startNextLevel():
    global currentLevel, mySprite
    hpbar.value = 100
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    currentLevel += 1
    if currentLevel == 1:
        tiles.set_tilemap(tilemap("""
            platformer1
            """))
        mySprite = sprites.create(img("""
                . . . . c c c c c c . . . . . .
                . . . c 6 7 7 7 7 6 c . . . . .
                . . c 7 7 7 7 7 7 7 7 c . . . .
                . c 6 7 7 7 7 7 7 7 7 6 c . . .
                . c 7 c 6 6 6 6 c 7 7 7 c . . .
                . f 7 6 f 6 6 f 6 7 7 7 f . . .
                . f 7 7 7 7 7 7 7 7 7 7 f . . .
                . . f 7 7 7 7 6 c 7 7 6 f c . .
                . . . f c c c c 7 7 6 f 7 7 c .
                . . c 7 2 7 7 7 6 c f 7 7 7 7 c
                . c 7 7 2 7 7 c f c 6 7 7 6 c c
                c 1 1 1 1 7 6 f c c 6 6 6 c . .
                f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
                f 6 1 1 1 1 1 6 6 6 6 6 c f . .
                . f 6 1 1 1 1 1 1 6 6 6 f . . .
                . . c c c c c c c c c f . . . .
                """),
            SpriteKind.player)
        controller.move_sprite(mySprite, 100, 0)
        mySprite.ay = 500
        hpbar.attach_to_sprite(mySprite, 1, 0)
        scene.camera_follow_sprite(mySprite)
        tiles.place_on_random_tile(mySprite, assets.tile("""
            tile3
            """))
        spawnEnemies()
    elif currentLevel == 2:
        tiles.set_current_tilemap(tilemap("""
            level9
            """))
        mySprite = sprites.create(img("""
                . . . . c c c c c c . . . . . .
                . . . c 6 7 7 7 7 6 c . . . . .
                . . c 7 7 7 7 7 7 7 7 c . . . .
                . c 6 7 7 7 7 7 7 7 7 6 c . . .
                . c 7 c 6 6 6 6 c 7 7 7 c . . .
                . f 7 6 f 6 6 f 6 7 7 7 f . . .
                . f 7 7 7 7 7 7 7 7 7 7 f . . .
                . . f 7 7 7 7 6 c 7 7 6 f c . .
                . . . f c c c c 7 7 6 f 7 7 c .
                . . c 7 2 7 7 7 6 c f 7 7 7 7 c
                . c 7 7 2 7 7 c f c 6 7 7 6 c c
                c 1 1 1 1 7 6 f c c 6 6 6 c . .
                f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
                f 6 1 1 1 1 1 6 6 6 6 6 c f . .
                . f 6 1 1 1 1 1 1 6 6 6 f . . .
                . . c c c c c c c c c f . . . .
                """),
            SpriteKind.player)
        controller.move_sprite(mySprite, 100, 0)
        mySprite.ay = 500
        hpbar.attach_to_sprite(mySprite, 1, 0)
        scene.camera_follow_sprite(mySprite)
        tiles.place_on_random_tile(mySprite, assets.tile("""
            tile3
            """))
        spawnEnemies()
        SpawnSpineEnemies()
    else:
        game.over(True)

def on_overlap_tile4(sprite4, location4):
    startNextLevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile4
        """),
    on_overlap_tile4)

def on_hit_wall(sprite2, location2):
    if mySprite.tile_kind_at(TileDirection.BOTTOM, sprites.dungeon.hazard_water):
        mySprite.vy = -200
        hpbar.value += -33.333333333333336
scene.on_hit_wall(SpriteKind.player, on_hit_wall)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . c c c c c c . . . .
                . . . . . c 6 7 7 7 7 6 c . . .
                . . . . c 7 7 7 7 7 7 7 7 c . .
                . . . c 6 7 7 7 7 7 7 7 7 6 c .
                . . . c 7 7 7 c 6 6 6 6 c 7 c .
                . . . f 7 7 7 6 f 6 6 f 6 7 f .
                . . . f 7 7 7 7 7 7 7 7 7 7 f .
                . . c f 6 7 7 c 6 7 7 7 7 f . .
                . c 7 7 f 6 7 7 c c c c f . . .
                c 7 7 7 7 f c 6 7 7 7 2 7 c . .
                c c 6 7 7 6 c f c 7 7 2 7 7 c .
                . . c 6 6 6 c c f 6 7 1 1 1 1 c
                . . f 6 6 6 6 c 6 6 1 1 1 1 1 f
                . . f c 6 6 6 6 6 1 1 1 1 1 6 f
                . . . f 6 6 6 1 1 1 1 1 1 6 f .
                . . . . f c c c c c c c c c . .
                """),
            img("""
                . . . . . . . c c c c c c . . .
                . . . . . . c 6 7 7 7 7 6 c . .
                . . . . . c 7 7 7 7 7 7 7 7 c .
                . . . . c 6 7 7 7 7 7 7 7 7 6 c
                . . . . c 7 7 7 c 6 6 6 6 c 7 c
                . . . . f 7 7 7 6 f 6 6 f 6 7 f
                . . . . f 7 7 7 7 7 7 7 7 7 7 f
                . . . . f 6 7 7 c 6 7 7 7 7 f .
                . . c c c f 6 7 7 c c c c f . .
                . c 7 7 7 c c f 7 7 7 2 6 c . .
                c 7 7 7 7 6 f c 7 7 2 7 7 6 c .
                c c c 6 6 6 c 6 6 7 1 1 1 1 c .
                . . c 6 6 6 6 6 6 1 1 1 1 1 c .
                . . c 6 6 6 6 6 1 1 1 1 1 6 c .
                . . c c 6 6 7 1 1 1 1 1 6 c . .
                . . . c c c c c c c c c c . . .
                """)],
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap4(sprite5, otherSprite4):
    sprites.destroy(otherSprite4)
    hpbar.value += -20
sprites.on_overlap(SpriteKind.player, SpriteKind.DMGProj, on_on_overlap4)

def spawnEnemies():
    global myEnemy
    for value12 in tiles.get_tiles_by_type(assets.tile("""
        tile5
        """)):
        myEnemy = sprites.create(img("""
                ........................
                ........................
                ........................
                ........................
                ..........ffff..........
                ........ff1111ff........
                .......fb111111bf.......
                .......f11111111f.......
                ......fd11111111df......
                ......fd11111111df......
                ......fddd1111dddf......
                ......fbdbfddfbdbf......
                ......fcdcf11fcdcf......
                .......fb111111bf.......
                ......fffcdb1bdffff.....
                ....fc111cbfbfc111cf....
                ....f1b1b1ffff1b1b1f....
                ....fbfbffffffbfbfbf....
                .........ffffff.........
                ...........fff..........
                ........................
                ........................
                ........................
                ........................
                """),
            SpriteKind.enemy)
        tiles.place_on_tile(myEnemy, value12)
        myEnemy.ay = 500
        enemyMove()
        for value3 in tiles.get_tiles_by_type(assets.tile("""
            tile5
            """)):
            tiles.set_tile_at(value3, assets.tile("""
                myTile0
                """))
def SpawnSpineEnemies():
    global mySprite2
    for value4 in tiles.get_tiles_by_type(assets.tile("""
        myTile10
        """)):
        mySprite2 = sprites.create(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . 2 . 2 . 2 . 2 2 2 . 2 . 2 . 2
                7 7 7 7 7 7 7 2 2 7 7 7 7 7 7 7
                """),
            SpriteKind.food)
        tiles.place_on_tile(mySprite2, value4)
        tiles.set_tile_at(value4, assets.tile("""
            transparency16
            """))
mySprite2: Sprite = None
standingStill = False
dashing = False
projectile: Sprite = None
mySprite: Sprite = None
myEnemy: Sprite = None
currentLevel = 0
hpbar: StatusBarSprite = None
statusbar: StatusBarSprite = None
isFacingLeft = False
dashSpeed = 0
dashSpeed = 350
isFacingLeft = True
statusbar = statusbars.create(40, 6, StatusBarKind.energy)
hpbar = statusbars.create(30, 5, StatusBarKind.health)
statusbar.set_bar_border(1, 12)
statusbar.value = 0
statusbar.max = 60
statusbar.set_color(7, 8, 9)
hpbar.set_bar_border(1, 12)
hpbar.set_color(7, 2)
statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
statusbar.bottom = 118
statusbar.left = 2
game.set_dialog_frame(img("""
    ..bbbbbbbbbbbbbbbbbbbb..
    .bd111111111111111111db.
    bd1dbbbbbbbbbbbbbbbbd1db
    b1dbbbbbbbbbbbbbbbbbbd1b
    b1bd1111111111111111db1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1b111111111111111111b1b
    b1bd1111111111111111db1b
    bd1bbbbbbbbbbbbbbbbbb1db
    bbd111111111111111111dbb
    .bbbbbbbbbbbbbbbbbbbbbb.
    ..bbbbbbbbbbbbbbbbbbbb..
    """))
game.set_dialog_text_color(15)
currentLevel = 0
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999111199999999999999999999999999999999999999999999999999999999999999999999999999999911119999999999999999999999999999999999999999999999999999
    9999999999999999999991111119999999999999999999999999999999999999999999999999999999999999999999999999999111111999999999999999999999999999999999999999999999999999
    9999999999999999999991111119911999999999999999999999999999999999999999999999999999999999999999999999999111111991199999999999999999999999999999999999999999999999
    9999999999999999991111111119111119999999999999999999999999999999999999999999999999999999999999999999111111111911111999999999999999999999999999999999999999999999
    9999999999999999911111111111111119999999999999999999999999999999999999999999999999999999999999999991111111111111111999999999999999999999999999999999999999999999
    9999999999999999111111111111111111199999999999999999999999999999999999999999999999999999999999999911111111111111111119999999999999999999999999999999999999999999
    9999999999999999111111111111111111119999999999999999999999999999999999999999999999999999999999999911111111111111111111999999999999999999999999999999999999999999
    9999999999999999911111111111111111119991199999999999999999999999999999999999999999999999999999999991111111111111111111999119999999999999999999999999999999999999
    9999999999999111191111111111111111119911111999999999999999999999999999999999999999999999999999911119111111111111111111991111199999999999999999999999999999999999
    9999999999991111119111111111111111199911111999999999999999999999999999999999999999999999999999111111911111111111111119991111199999999999999999999999999999999999
    9999999999991111111111111111111111911111111199999999999999999999999999999999999999999999999999111111111111111111111191111111119999999999999999999999999999999999
    9999999999991111111111111111111111111111111199999999999999999999999999999999999999999999999999111111111111111111111111111111119999999999999999999999999999999999
    9999999999999111111111111111111111111111111199999999999999999999999999999999999999999999999999911111111111111111111111111111119999999999999999999999999999999999
    9911199991111911111111111111111111111111111991199999999999991111999999999999999999991119999111191111111111111111111111111111199119999999999999111199999999999999
    9111119911111111111111111111111111111111111911119999999999911111199999999999999999911111991111111111111111111111111111111111191111999999999991111119999999999999
    9111119111111111111111111111111111111111111911119999999999911111191119999999999999911111911111111111111111111111111111111111191111999999999991111119111999999999
    9911111111111111111111111111111111111111111111119999999999999111111111999999999999991111111111111111111111111111111111111111111111999999999999911111111199999999
    9111111111111111111111111111111111111111111111199999999911119111111111999999999999911111111111111111111111111111111111111111111119999999991111911111111199999999
    1111111111111111111111111111111111111111111111119999999111111111111119999999999199111111111dd1111111111111111111111111111111111111999999911111111111111999999999
    1111111111111111111111111111111111111111111111111911199111111111111111111999999ddd111111111ddd111111111111111111111111111111111111191119911111111111111111199999
    1111111111111111111111111111111111111111111111111111111111111111111111111199991ddd111111111ddd111111111111111111111111111111111111111111111111111111111111119999
    11111111111111111111111111111111111111111111111111111111111111111111111111999ddddddd111111ddddd11111111111111111111111111111111111111111111111111111111111119999
    11111111111111111111111111111111111111111ddddddddd111111111111111111111111111ddddddd111111ddddd111111111111111111111111111111111111111111dddddddddd1111111111111
    11111111111111111111111111111111111111111ddddddddd111111111111111111111111111ddddddd111111ddddd111111111111111111111111111111111111111111dddddddddd1111111111111
    1111111111111111111ddd1111111111111111111d11dddddd111111111111111111111111111d11dddd11111ddddddd11111111111111111111dd1111111111111111111dd1d1ddddd1111111111111
    111111111111111111ddddd111111111111111111ddddddd1d111111111111111111111111111ddddddd11111ddddddd1111111111111111111dddd111111111111111111dddddd11dd1111111111111
    11111111111111111dddddd111111111111111111ddddddddd1111111111d11111111ddddd111d1ddddd11111ddddddd11111111111111111dddddd111111111111111111dddddddddd1111111111111
    11111111111111111ddd1d111111d111111111111ddddddddd111111111dd11111111ddddd111ddddddd11111ddddddd11111111111111111ddd1d111111dd11111111111dddd1ddddd11111111dd111
    11111111111111111dddddd11111d111111111111ddddddd1d111111111dd11111111ddddd111ddddddd11111ddddddd11111111111111111dddddd11111dd11111111111ddddddd1dd11111111dd111
    11111111ddd111111dd11d11111ddd11111111111ddddddddd11dddddd1dd11111111ddddd111ddddddd11111ddddddd111111111dd111111ddd1d11111ddd11111111111dddddddddd1ddddddddd111
    d1dd1111ddddddddddd1ddd111ddddd1111111111ddddddd1d11d11ddd1dd111111111dd1dd11ddddddd111dddddddddd1dd1111ddddddddddddd1d1111dddd1111111111dddddd11dd1d11dddddd111
    dddd11111d1dd1ddddddddd111ddddd1111111111ddddddddd11dddd1d1dd11111111dddddd11dd1dddd111ddddddddddddd1111dd1ddd1dddddddd1111dddd1111111111dddddddddd1dddd1dddd111
    dd1d11111ddd1111ddddddd111ddddd1111111111ddddddddd11dddd1dddd11111111dddddd11ddddddd111ddddddddddd1d1111dddd1d11ddddddd1111dddd1111111111dddddddddd1dddd1dddd111
    dddd1111dddddddddddddddd11dddddd11dd1dd1ddddddddddd1d11dddddd11111111dddddd11ddddddd111ddddddddddddd1111dddddddddddddddd11dddddd111d11ddddddddddddd1d11dddddd111
    dd1d1111dddddddddddddddd11dddddd11ddddddddddddddddd1ddddddddd11d11d11dddddd11ddddddd111ddddddddddd1d1111dddddddddddddddd11dddddd111dddddddddddddddd1ddddddddd111
    ddddd1dd1d1ddddddddddddd11ddddddd1dddd11ddddddddddddd11bbddddddd1ddd11dd1dd11ddddddd111ddddddddddddddd1ddd1ddddddddddddd11ddddddd111d11ddddddbddddddd11bbbddd1dd
    ddddd1dddddddddddddddddddd1dddddd1dddddddddbbbdddddddddbbbdddddd1ddd1dddddd11ddddddd111ddddddddddddddd1dddddddddddddddddddddddddd1ddddddddddbbdddddddddbbbddd1dd
    ddddd1ddddddddddddddddddddddddddd1dddddddddbbbdddddddddbbbdddddddddddddddddddddddddd111ddddddddddddddd1dddddddddddddddddddddddddd1ddddddddddbbdddddddddbbbdddddd
    ddddd1ddddddddddddddddddddddddddd1dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd1ddddddddddddddd1dddddddddddddddddddddddddd1d1ddddddbbbbbbbdddddbbbbbddddd
    dddddbbbbbbbbbddddddddddddddddddd1dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd1ddddddddddddddbbbbbbbbbbdddddddddddddddddd1ddddddddbbbbbbbdddddbbbbbddddd
    dddddbbbbbbbbbddddddddddddddddddd1dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd1ddddddddddddddbbbbbbbbbbdddddddddddddddddd1ddddddddbbbbbbbdddddbbbbbddddd
    dddddbddbbbbbbddddddddddddddddddd1dddddddbddbbbbdddddbbbbbbbdd111dddddddddddddddbbdddd1ddddddddddddddbbdbdbbbbbdddddddddddddddddd1ddddddddbbbbbbbddddbbbbbbbb11d
    dddddbbbbbbbdbddddddddddddddddddd1dddddddbbbbbbbdddddbbbbbbbddd11ddddddddddddddbbbbddd1ddddddddddddddbbbbbbddbbdddddddddddddddddd1ddddddddbbbbbbbddddbbbbbbbbddd
    dddddbbbbbbbbbddddddddddbddddddddbbbbbdddbdbbbbbdddddbbbbbbbddddddddddd1dddddbbbbbbddd1ddddddddddddddbbbbbbbbbbdddddddddddddddddddbbbbddddbbbdbbbddddbbbbbbbbddd
    dddddbbbbbbbbbdddddddddbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdd1ddddddddddddddbbbdbddddddbbdddddddddddbbbbdbbbbbddddddddbbdddddddddbbbbddddbbbdbbbddddbbbbbbbbd1d
    dddddbbbbbbbdbdddddddddbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdd111ddddddddddddbbbbbbdddddbbdddddddddddbbbbbbbdbbddddddddbbddddddddbbbbbbdddbbbbbbbddddbbbbbbbb11d
    dddddbbbbbbbbbddbbbbbbdbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdddddddddbb1dddddbbbdbdddddbbbdddddddddddbbbbbbbbbbdbbbbbbbbbddddddddbbbbbbdddbbbdbbbddddbbbbbbbbddd
    dddddbbbbbbbdbddbddbbbdbbdddddddddbbdbbddbbbbbbbdddbbbbbbbbbbdbbddddbbbbbbbbbbbbbdbddddbbbbddddddddddbbbbbbddbbdbddbbbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
    dddddbbbbbbbbbddbbbbdbdbbddddddddbbbbbbddbbdbbbbdddbbbbbbbbbbbbbddddbbdbbbdbbbbbbbbddddbbbbddddddddddbbbbbbbbbbdbbbbdbbbbddddddddbbbbbbbddbbbbdbbddbbbbbbbbbbbbb
    dddddbbbbbbbbbddbbbbdbbbbddddddddbbbbbbddbbbbbbbdddbbbbbbbbbbbdbddddbbbbdbddbbbbbbbddddbbbbddddddddddbbbbbbbbbbdbbbbdbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
    dbbdbbbbbbbbbbbdbddbbbbbbddddddddbbbbbbddbbbbbbbdddbbbbbbbbbbbbbddddbbbbbbbbbbbbbbbbddbbbbbbdddbddbbbbbbbbbbbbbdbddbbbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbdbbbbbbbbbddbddbddbbbbbbddbbbbbbbdddbbbbbbbbbbbdbddddbbbbbbbbbbbbbbbbddbbbbbbdddbbbbbbbbbbbbbbbbdbbbbbbbbbdddddbddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
    bbddbbbbbbbbbbbbbddddbbbbbbbdbbbddbbdbbddbbbbbbbdddbbbbbbbbbbbbbbbdbbbdbbbbbbbbbbbbbddbbbbbbbdddbddbbbbbbbbbbbbbbddbdbbbbdbbdbbbdbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbdbbbbbbddbbbbbbbdddbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbdbbbbbbbbbbbddbbbbdbbddbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbddbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbddbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbb
    bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7
    bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77
    bb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777b
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    """))
startNextLevel()

def on_on_update():
    for value13 in sprites.all_of_kind(SpriteKind.enemy):
        if value13.is_hitting_tile(CollisionDirection.BOTTOM):
            if value13.vx < 0 and (value13.tile_kind_at(TileDirection.LEFT, assets.tile("""
                tile1
                """)) or (value13.tile_kind_at(TileDirection.LEFT, sprites.builtin.forest_tiles3) or (value13.tile_kind_at(TileDirection.LEFT, sprites.builtin.forest_tiles11) or value13.tile_kind_at(TileDirection.LEFT, sprites.builtin.forest_tiles7)))):
                value13.vy = -175
            elif value13.vx > 0 and (value13.tile_kind_at(TileDirection.RIGHT, assets.tile("""
                tile1
                """)) or (value13.tile_kind_at(TileDirection.RIGHT, sprites.builtin.forest_tiles1) or (value13.tile_kind_at(TileDirection.RIGHT, sprites.builtin.forest_tiles9) or value13.tile_kind_at(TileDirection.RIGHT, sprites.builtin.forest_tiles5)))):
                value13.vy = -175
        elif value13.is_hitting_tile(CollisionDirection.LEFT):
            value13.vx = 30
            animation.run_image_animation(value13,
                [img("""
                        ........................
                        ........................
                        ........................
                        ........................
                        ..........fffff.........
                        ........ff11111f........
                        .......fb111111bf.......
                        ......fbd1111111f.......
                        ......fddd111111df......
                        ......fdddd11111df......
                        ......fddddddd11df......
                        ......fddddddd111f......
                        ......fddddddcf11f......
                        .......fbdddb1111bf.....
                        ........fffcfdb1b1f.....
                        .......ffffffffbfbf.....
                        ....ff.fffffffffff......
                        .....ffffffff...........
                        .....ffffffb1b1f........
                        ......ffffffbfbf........
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......fd1111111f.......
                        ......fdd1111111df......
                        ......fddd111111df......
                        ......fdddddd111df......
                        ......fbddddbfd1df......
                        ......fcbbbdcfddbf......
                        .......fcbb11111f.......
                        ........fffff1b1f.......
                        ........fb111cfbf.......
                        ........ffb1b1ff........
                        ......f.fffbfbf.........
                        ......ffffffff..........
                        .......fffff............
                        ........................
                        ........................
                        ........................
                        ........................
                        """)],
                200,
                True)
        elif value13.is_hitting_tile(CollisionDirection.RIGHT):
            value13.vx = -30
            animation.run_image_animation(value13,
                [img("""
                        ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f1111111df.......
                        ......fd1111111ddf......
                        ......fd111111dddf......
                        ......fd111ddddddf......
                        ......fd1dfbddddbf......
                        ......fbddfcdbbbcf......
                        .......f11111bbcf.......
                        .......f1b1fffff........
                        .......fbfc111bf........
                        ........ff1b1bff........
                        .........fbfbfff.f......
                        ..........ffffffff......
                        ............fffff.......
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        ........................
                        ........................
                        ........................
                        ........................
                        .........fffff..........
                        ........f11111ff........
                        .......fb111111bf.......
                        .......f1111111dbf......
                        ......fd111111dddf......
                        ......fd11111ddddf......
                        ......fd11dddddddf......
                        ......f111dddddddf......
                        ......f11fcddddddf......
                        .....fb1111bdddbf.......
                        .....f1b1bdfcfff........
                        .....fbfbffffffff.......
                        ......fffffffffff.ff....
                        ...........ffffffff.....
                        ........f1b1bffffff.....
                        ........fbfbffffff......
                        ........................
                        ........................
                        ........................
                        ........................
                        """)],
                200,
                True)
        elif not (tiles.tile_at_location_is_wall(tiles.get_tile_location(value13.x - 1, value13.y - 1))):
            value13.vx = 30
            animation.run_image_animation(value13,
                [img("""
                        ........................
                        ........................
                        ........................
                        ........................
                        ..........fffff.........
                        ........ff11111f........
                        .......fb111111bf.......
                        ......fbd1111111f.......
                        ......fddd111111df......
                        ......fdddd11111df......
                        ......fddddddd11df......
                        ......fddddddd111f......
                        ......fddddddcf11f......
                        .......fbdddb1111bf.....
                        ........fffcfdb1b1f.....
                        .......ffffffffbfbf.....
                        ....ff.fffffffffff......
                        .....ffffffff...........
                        .....ffffffb1b1f........
                        ......ffffffbfbf........
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......fd1111111f.......
                        ......fdd1111111df......
                        ......fddd111111df......
                        ......fdddddd111df......
                        ......fbddddbfd1df......
                        ......fcbbbdcfddbf......
                        .......fcbb11111f.......
                        ........fffff1b1f.......
                        ........fb111cfbf.......
                        ........ffb1b1ff........
                        ......f.fffbfbf.........
                        ......ffffffff..........
                        .......fffff............
                        ........................
                        ........................
                        ........................
                        ........................
                        """)],
                200,
                True)
        elif not (tiles.tile_at_location_is_wall(tiles.get_tile_location(value13.x + 1, value13.y - 1))):
            value13.vx = -30
            animation.run_image_animation(value13,
                [img("""
                        ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f1111111df.......
                        ......fd1111111ddf......
                        ......fd111111dddf......
                        ......fd111ddddddf......
                        ......fd1dfbddddbf......
                        ......fbddfcdbbbcf......
                        .......f11111bbcf.......
                        .......f1b1fffff........
                        .......fbfc111bf........
                        ........ff1b1bff........
                        .........fbfbfff.f......
                        ..........ffffffff......
                        ............fffff.......
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        ........................
                        ........................
                        ........................
                        ........................
                        .........fffff..........
                        ........f11111ff........
                        .......fb111111bf.......
                        .......f1111111dbf......
                        ......fd111111dddf......
                        ......fd11111ddddf......
                        ......fd11dddddddf......
                        ......f111dddddddf......
                        ......f11fcddddddf......
                        .....fb1111bdddbf.......
                        .....f1b1bdfcfff........
                        .....fbfbffffffff.......
                        ......fffffffffff.ff....
                        ...........ffffffff.....
                        ........f1b1bffffff.....
                        ........fbfbffffff......
                        ........................
                        ........................
                        ........................
                        ........................
                        """)],
                200,
                True)
game.on_update(on_on_update)

def on_on_update2():
    if not (dashing):
        statusbar.value += 1
game.on_update(on_on_update2)

def on_on_update3():
    global isFacingLeft, standingStill
    if mySprite.vx > 0:
        isFacingLeft = False
        standingStill = False
    elif mySprite.vx < 0:
        isFacingLeft = True
        standingStill = False
    else:
        standingStill = True
game.on_update(on_on_update3)

def on_on_update4():
    if hpbar.value == 0:
        game.set_game_over_message(False, "Oh no! You died...")
        game.game_over(False)
game.on_update(on_on_update4)
def lasersprite(sprite:Sprite, loc:tiles.Location):
    
    sprite.set_position(loc)
    sprite.ay = 600
    def on_background():
        def onPause_until():
            return sprite.tile_kind_at(TileDirection.BOTTOM, assets.tile("""tile1"""))
        pause_until(onPause_until)
        animation.run_image_animation(sprite, [img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . 2 1 2 . . . . . .
            . . . . . . . 2 1 2 . . . . . .
            . . . . . . . 2 1 2 . . . . . .
            . . . . . . . 3 1 3 . . . . . .
            . . . . . . 2 3 1 3 2 . . . . .
            . . . . . . 2 1 1 1 2 . . . . .
            . . . . . . 2 1 1 1 3 . . . . .
            . . . . . . 3 1 1 1 3 . . . . .
            . . . . . . 3 1 1 1 3 . . . . .
            . . . . . . 3 1 1 1 3 . . . . .
            . . . . . . 2 3 1 3 2 . . . . .
            . . . . . . . 2 2 2 . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . 2 3 3 3 3 3 2 . . . .
            . . . . 3 1 1 1 1 1 1 1 3 . . .
            . . . . 1 1 1 1 1 1 1 1 1 . . .
            . . . 2 1 1 1 1 1 1 1 1 1 2 . .
            . . . 2 3 1 1 1 1 1 1 3 3 2 . .
            . . . . . . 2 2 2 2 2 . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . 4 4 4 4 4 . . . . . .
            . . . 4 4 4 5 5 5 d 4 4 4 4 . .
            . . 4 d 5 d 5 5 5 d d d 4 4 . .
            . . 4 5 5 1 1 1 d d 5 5 5 4 . .
            . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 .
            . 4 d d 1 1 5 5 5 1 1 5 5 d 4 .
            . 4 5 5 1 1 5 1 1 5 5 d d d 4 .
            . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 .
            . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 .
            . . 2 4 d d 5 5 5 5 d d 5 4 . .
            . . . 2 2 4 d 5 5 d d 4 4 . . .
            . . 2 2 2 2 2 4 4 4 2 2 2 . . .
            . . . 2 2 4 4 4 4 4 4 2 2 . . .
            . . . . . 2 2 2 2 2 2 . . . . .
        """),
        img("""
            . . . . 2 2 2 2 2 2 2 2 . . . .
            . . . 2 4 4 4 5 5 4 4 4 2 2 2 .
            . 2 2 5 5 d 4 5 5 5 4 4 4 4 2 .
            . 2 4 5 5 5 5 d 5 5 5 4 5 4 2 2
            . 2 4 d d 5 5 5 5 5 5 d 4 4 4 2
            2 4 5 5 d 5 5 5 d d d 5 5 5 4 4
            2 4 5 5 4 4 4 d 5 5 d 5 5 5 4 4
            4 4 4 4 . . 2 4 5 5 . . 4 4 4 4
            . . b b b b 2 4 4 2 b b b b . .
            . b d d d d 2 4 4 2 d d d d b .
            b d d b b b 2 4 4 2 b b b d d b
            b d d b b b b b b b b b b d d b
            b b d 1 1 3 1 1 d 1 d 1 1 d b b
            . . b b d d 1 1 3 d d 1 b b . .
            . . 2 2 4 4 4 4 4 4 4 4 2 2 . .
            . . . 2 2 4 4 4 4 4 2 2 2 . . .
        """),
        img("""
            . . . . . . . . b b . . . . . .
            . . . . . . . . b b . . . . . .
            . . . b b b . . . . . . . . . .
            . . b d d b . . . . . . . b b .
            . b d d d b . . . . . . b d d b
            . b d d b . . . . b b . b d d b
            . b b b . . . . . b b . . b b .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . b b b d d d d d d b b b . .
            . b d c c c b b b b c c d d b .
            b d d c b . . . . . b c c d d b
            c d d b b . . . . . . b c d d c
            c b d d d b b . . . . b d d c c
            . c c b d d d d b . c c c c c c
            . . . c c c c c c . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
        """)], 100)
    timer.background(on_background)
    
    return 0
def on_update_intervadl():
    for value5 in tiles.get_tiles_by_type(assets.tile("""
        myTile11
        """)):
        lasersprite(sprites.create(img("""
            . . . . . . . 2 1 2 . . . . . .
            . . . . . . . 2 1 2 . . . . . .
            . . . . . . . 2 1 3 . . . . . .
            . . . . . . . 2 1 2 . . . . . .
            . . . . . . . 3 1 2 . . . . . .
            . . . . . . . 3 1 2 . . . . . .
            . . . . . . . 2 1 2 . . . . . .
            . . . . . . . 2 1 3 . . . . . .
            . . . . . . . 2 1 2 . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
        """)), value5)

    return None
game.on_update_interval(2000, on_update_intervadl())

def on_forever():
    for value32 in tiles.get_tiles_by_type(assets.tile("""
        myTile3
        """)):
        tiles.set_tile_at(value32, assets.tile("""
            transparency16
            """))
forever(on_forever)

def on_forever2():
    pass
forever(on_forever2)
