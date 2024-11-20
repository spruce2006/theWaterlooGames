# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define k = Character("Kamkar")
define p = Character("Pendar")
define a = Character("Aucoin")
define j = Character("Hamilton")
define v = Character("Azevedo")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"


# Blurb about the lore of the Waterloo Games, show title, Kamkar asks for name


# Justin and Marlyn explain how the games work, and then usher you off the go on the Tool show


# The Tool asks you a bunch of questions; just interactive not for points


# Cut to the Cornucopia; go through each tribute and look at their stats(the player is the one thinking things about them, so there should be no name in the overhead part)


# We run off the platform and face off with Azevedo. At the end, he disappears.


# After the fight, we rush off to a river, drink water, go to sleep in a tree(these can just be images of a river, tree, then black)


# We wake up to a thud, who's that? It's Tam at the bottom! He tells us to come down and fight him(write some threats here)


# Face off with Tam. At the end, he disappears.


# We run away, and after like one frame of just getting away, we spot Jamilton, and fight him.


# After fighting Hamilton, he's like "wait wait wait let's just team up and take down Zino and Aucoin! They're too powerful for either of us to fight them alone. We're better together."


# We approach Zino and Aucoin and Hamilton fights them. Hamilton disappears!


# Zino and Aucoin approach us and start to fight us. At the end, they disappear.


# Looks into the sky, and there's 22 cannons. Looks like it's just me and Pendar left. The Gamemakers make an announcement that they replenished the Cornucopia. We decide to go, since we're running out of supplies. We go to the Cornucopia. Pendar is behind us and challenges us to a fight.


# Pendar fight. She doesn't disappear tho, just fades into the next scene.


# Dean MW says we won and offers us admission!

    # This ends the game.

    return
