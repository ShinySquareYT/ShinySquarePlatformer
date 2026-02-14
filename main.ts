namespace SpriteKind {
    export const PlayerComboPower = SpriteKind.create()
    export const DMGProj = SpriteKind.create()
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        tile2
        `, function on_overlap_tile(sprite52: Sprite, location5: tiles.Location) {
    game.over(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile1
        `, function on_overlap_tile2(sprite: Sprite, location: tiles.Location) {
    
    for (let value of tiles.getTilesByType(assets.tile`
        myTile2
        `)) {
        tiles.setWallAt(value, true)
    }
    for (let value2 of tiles.getTilesByType(assets.tile`
        myTile
        `)) {
        for (let index = 0; index < 7; index++) {
            myEnemy = sprites.create(img`
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
                    `, SpriteKind.Enemy)
            tiles.placeOnTile(myEnemy, value2)
            myEnemy.ay = 500
            enemyMove()
        }
    }
})
function enemyMove() {
    if (randint(1, 2) == 1) {
        animation.runImageAnimation(myEnemy, [img`
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
                    `, img`
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
                    `], 200, true)
        myEnemy.vx = -30
    } else {
        animation.runImageAnimation(myEnemy, [img`
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
                    `, img`
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
                    `], 200, true)
        myEnemy.vx = 30
    }
    
}

controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    if (mySprite.vy == 0) {
        mySprite.vy = -200
    }
    
})
controller.combos.attachCombo("a", function on_combos_attach_combo() {
    
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap(sprite62: Sprite, otherSprite3: Sprite) {
    otherSprite3.destroy()
    if (sprite62.bottom < otherSprite3.y) {
        sprite62.vy = -100
    } else {
        hpbar.value += -20
    }
    
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function on_on_overlap2(sprite3: Sprite, otherSprite: Sprite) {
    sprites.destroy(sprite3)
    sprites.destroy(projectile)
})
controller.combos.attachCombo("b", function on_combos_attach_combo2() {
    
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function on_on_overlap3(sprite6: Sprite, otherSprite2: Sprite) {
    if (randint(1, 2) == 1) {
        animation.runImageAnimation(otherSprite2, [img`
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
                `], 500, false)
        hpbar.value += -20
        sprites.destroy(otherSprite2)
    } else {
        sprites.destroy(otherSprite2)
    }
    
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile6
        `, function on_overlap_tile3(sprite32: Sprite, location3: tiles.Location) {
    tiles.setTileAt(location3, assets.tile`
        transparency16
        `)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    if (!dashing && statusbar.value == statusbar.max) {
        projectile = sprites.createProjectileFromSprite(img`
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
                `, mySprite, 0, 0)
        projectile.setScale(5, ScaleAnchor.Middle)
        animation.runImageAnimation(projectile, [img`
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
                    `, img`
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
                    `, img`
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
                    `, img`
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
                    `, img`
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
                    `], 100, false)
        dashing = true
        controller.moveSprite(mySprite, 0, 0)
        if (controller.up.isPressed()) {
            if (standingStill) {
                mySprite.setVelocity(0, 0 - dashSpeed)
            } else if (isFacingLeft) {
                mySprite.setVelocity(0 - Math.sqrt(2) / 2 * dashSpeed, 0 - Math.sqrt(2) / 2 * dashSpeed)
            } else {
                mySprite.setVelocity(Math.sqrt(2) / 2 * dashSpeed, 0 - Math.sqrt(2) / 2 * dashSpeed)
            }
            
        } else if (isFacingLeft) {
            mySprite.setVelocity(0 - dashSpeed, 0)
        } else {
            mySprite.setVelocity(dashSpeed, 0)
        }
        
        mySprite.startEffect(effects.trail)
        mySprite.startEffect(effects.trail)
        mySprite.startEffect(effects.trail)
        statusbar.value = 0
        timer.after(200, function on_after() {
            
            dashing = false
            mySprite.vx = 0
            controller.moveSprite(mySprite, 100, 0)
            effects.clearParticles(mySprite)
            projectile = sprites.createProjectileFromSprite(img`
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
                    `, mySprite, 0, 0)
            projectile.setScale(5, ScaleAnchor.Middle)
            animation.runImageAnimation(projectile, [img`
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
                        `, img`
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
                        `, img`
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
                        `, img`
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
                        `, img`
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
                        `], 100, false)
        })
    }
    
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    animation.runImageAnimation(mySprite, [img`
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
                `, img`
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
                `], 100, true)
})
function startNextLevel() {
    
    hpbar.value = 100
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    currentLevel += 1
    if (currentLevel == 1) {
        tiles.setTilemap(tilemap`
            platformer1
            `)
        mySprite = sprites.create(img`
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
                `, SpriteKind.Player)
        controller.moveSprite(mySprite, 100, 0)
        mySprite.ay = 500
        hpbar.attachToSprite(mySprite, 1, 0)
        scene.cameraFollowSprite(mySprite)
        tiles.placeOnRandomTile(mySprite, assets.tile`
            tile3
            `)
        spawnEnemies()
    } else if (currentLevel == 2) {
        tiles.setCurrentTilemap(tilemap`
            level9
            `)
        mySprite = sprites.create(img`
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
                `, SpriteKind.Player)
        controller.moveSprite(mySprite, 100, 0)
        mySprite.ay = 500
        hpbar.attachToSprite(mySprite, 1, 0)
        scene.cameraFollowSprite(mySprite)
        tiles.placeOnRandomTile(mySprite, assets.tile`
            tile3
            `)
        spawnEnemies()
        SpawnSpineEnemies()
    } else {
        game.over(true)
    }
    
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        tile4
        `, function on_overlap_tile4(sprite4: Sprite, location4: tiles.Location) {
    startNextLevel()
})
scene.onHitWall(SpriteKind.Player, function on_hit_wall(sprite2: Sprite, location2: tiles.Location) {
    if (mySprite.tileKindAt(TileDirection.Bottom, sprites.dungeon.hazardWater)) {
        mySprite.vy = -200
        hpbar.value += -33.333333333333336
    }
    
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    animation.runImageAnimation(mySprite, [img`
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
                `, img`
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
                `], 100, true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.DMGProj, function on_on_overlap4(sprite5: Sprite, otherSprite4: Sprite) {
    sprites.destroy(otherSprite4)
    hpbar.value += -20
})
function spawnEnemies() {
    
    for (let value12 of tiles.getTilesByType(assets.tile`
        tile5
        `)) {
        myEnemy = sprites.create(img`
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
                `, SpriteKind.Enemy)
        tiles.placeOnTile(myEnemy, value12)
        myEnemy.ay = 500
        enemyMove()
        for (let value3 of tiles.getTilesByType(assets.tile`
            tile5
            `)) {
            tiles.setTileAt(value3, assets.tile`
                myTile0
                `)
        }
    }
}

function SpawnSpineEnemies() {
    
    for (let value4 of tiles.getTilesByType(assets.tile`
        myTile10
        `)) {
        mySprite2 = sprites.create(img`
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
                `, SpriteKind.Food)
        tiles.placeOnTile(mySprite2, value4)
        tiles.setTileAt(value4, assets.tile`
            transparency16
            `)
    }
}

let mySprite2 : Sprite = null
let standingStill = false
let dashing = false
let projectile : Sprite = null
let mySprite : Sprite = null
let myEnemy : Sprite = null
let currentLevel = 0
let hpbar : StatusBarSprite = null
let statusbar : StatusBarSprite = null
let isFacingLeft = false
let dashSpeed = 0
dashSpeed = 350
isFacingLeft = true
statusbar = statusbars.create(40, 6, StatusBarKind.Energy)
hpbar = statusbars.create(30, 5, StatusBarKind.Health)
statusbar.setBarBorder(1, 12)
statusbar.value = 0
statusbar.max = 60
statusbar.setColor(7, 8, 9)
hpbar.setBarBorder(1, 12)
hpbar.setColor(7, 2)
statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
statusbar.bottom = 118
statusbar.left = 2
game.setDialogFrame(img`
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
    `)
game.setDialogTextColor(15)
currentLevel = 0
scene.setBackgroundImage(img`
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
    `)
startNextLevel()
game.onUpdate(function on_on_update() {
    for (let value13 of sprites.allOfKind(SpriteKind.Enemy)) {
        if (value13.isHittingTile(CollisionDirection.Bottom)) {
            if (value13.vx < 0 && (value13.tileKindAt(TileDirection.Left, assets.tile`
                tile1
                `) || (value13.tileKindAt(TileDirection.Left, sprites.builtin.forestTiles3) || (value13.tileKindAt(TileDirection.Left, sprites.builtin.forestTiles11) || value13.tileKindAt(TileDirection.Left, sprites.builtin.forestTiles7))))) {
                value13.vy = -175
            } else if (value13.vx > 0 && (value13.tileKindAt(TileDirection.Right, assets.tile`
                tile1
                `) || (value13.tileKindAt(TileDirection.Right, sprites.builtin.forestTiles1) || (value13.tileKindAt(TileDirection.Right, sprites.builtin.forestTiles9) || value13.tileKindAt(TileDirection.Right, sprites.builtin.forestTiles5))))) {
                value13.vy = -175
            }
            
        } else if (value13.isHittingTile(CollisionDirection.Left)) {
            value13.vx = 30
            animation.runImageAnimation(value13, [img`
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
                        `, img`
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
                        `], 200, true)
        } else if (value13.isHittingTile(CollisionDirection.Right)) {
            value13.vx = -30
            animation.runImageAnimation(value13, [img`
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
                        `, img`
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
                        `], 200, true)
        } else if (!tiles.tileAtLocationIsWall(tiles.getTileLocation(value13.x - 1, value13.y - 1))) {
            value13.vx = 30
            animation.runImageAnimation(value13, [img`
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
                        `, img`
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
                        `], 200, true)
        } else if (!tiles.tileAtLocationIsWall(tiles.getTileLocation(value13.x + 1, value13.y - 1))) {
            value13.vx = -30
            animation.runImageAnimation(value13, [img`
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
                        `, img`
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
                        `], 200, true)
        }
        
    }
})
game.onUpdate(function on_on_update2() {
    if (!dashing) {
        statusbar.value += 1
    }
    
})
game.onUpdate(function on_on_update3() {
    
    if (mySprite.vx > 0) {
        isFacingLeft = false
        standingStill = false
    } else if (mySprite.vx < 0) {
        isFacingLeft = true
        standingStill = false
    } else {
        standingStill = true
    }
    
})
game.onUpdate(function on_on_update4() {
    if (hpbar.value == 0) {
        game.setGameOverMessage(false, "Oh no! You died...")
        game.gameOver(false)
    }
    
})
function lasersprite(sprite: Sprite, loc: any): number {
    sprite.ay = 600
    sprite.setPosition
    pauseUntil(function onPause_until(): boolean {
        return sprite.tileKindAt(TileDirection.Bottom, assets.tile`tile1`)
    })
    return 0
}

function on_update_intervadl(): () => void {
    for (let value5 of tiles.getTilesByType(assets.tile`
        myTile11
        `)) {
        lasersprite(sprites.create(img`
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
        `), value5)
    }
    return null
}

game.onUpdateInterval(2000, on_update_intervadl())
forever(function on_forever() {
    for (let value32 of tiles.getTilesByType(assets.tile`
        myTile3
        `)) {
        tiles.setTileAt(value32, assets.tile`
            transparency16
            `)
    }
})
forever(function on_forever2() {
    
})
