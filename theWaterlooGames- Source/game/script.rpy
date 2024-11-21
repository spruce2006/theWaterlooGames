# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define k = Character("Milad Kamkar")
define p = Character("Pendar Mahmoudi")
define a = Character("Marc Aucoin")
define h = Character("Jordan Hamilton")
define v = Character("Matheus Azevedo")
define z = Character("Zino Ojogbo")
define m = Character("Michael Tam")
define j = Character("J-Money")
define y = Character("Marlyn")
define d = Character("Dean Mary Wells")
define t = Character("Tool")

image stagebg = "stagebg.png"
image edcombg = "edcombg.png"
image toolbg = "toolbg.png"
image cornucopuabg = "cornucopiabg.png"
image forestbg:
    "forestbg.png"
    zoom 4
image justin: 
    "justin.png"
    zoom 2
image pendar cornucopia = "pendar cornucopia.png"
image tam cornucopia = "tam cornucopia.png"
image tam fighting = "tam cornucopia fighting.png"
image tam tree:
    "tam tree.png"
    zoom 3.5
image marlyn:
    "marlyn.png"
    zoom 0.75
image aucoin cornucopia = "aucoin cornucopia.png"
image aucoin zino fight: 
    "aucoin zino fight.png"
    zoom 1.1
image zino cornucopia = "zino cornucopia.png"
image dean mary wells end = "dean mary wells end.png"
image kamkar cornucopia = "kamkar cornucopia.png"
image kamkar intro = "kamkar intro.png"
image jamilton = "jamilton cornucopia.png"
image jamilton fight = "jamilton talk.png"
image bg river:
    "bg river.jpg"
    zoom 3.25
image sleep:
    "sleep.jpg"
    zoom 4
# The game starts here.

#label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

   # show eileen happy

    # These display lines of dialogue.

   # e "You've created a new Ren'Py game."

  #  e "Once you add a story, pictures, and music, you can release it to the world!"

label start:
    # Blurb about the lore of the Waterloo Games, show title, Kamkar asks for name (cameron)

    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Player"
    define n = Character("[name]")
    # Justin and Marlyn explain how the games work, and then usher you off the go on the Tool show (maddy)
    scene stagebg   
    show justin:
        xalign 0.0 
        yalign 0.4

    show marlyn:
        xalign 1.0 
        yalign 0.2

    show marlyn behind justin
    j "whats good fam"

    # The Tool asks you a bunch of questions; just interactive not for points (snack)


    # Cut to the Cornucopia; go through each tribute and look at their stats(the player is the one thinking things about them, so there should be no name in the overhead part) (cameron)
    scene cornicopiabg
    show pendar cornucopia:
        xalign 0.0
        yalign 0.0
    show tam cornucopia:
        xalign 0.2
        yalign 0.2
    show aucoin cornucopia:
        xalign 0.3
        yalign 0.3
    show jamilton cornucopia:
        xalign 0.5
        yalign 0.5
    show zino cornucopia:
        xalign 0.7
        yalign 0.3
    show kamkar cornucopia:
        xalign 0.8
        yalign 0.2
    #show azevedo cornucopia:
        #xalign 1.0
        #yalign 0.0


    # We run off the platform and face off with Azevedo. At the end, he disappears. (snack)


    # After the fight, we rush off to a river, drink water, go to sleep in a tree(these can just be images of a river, tree, then black) (spruha)
    scene bg river
    "After the long fight with Azevedo, I went to a nearby stream to calm down."
    "It was my first time ever fighting someone. How am I going to get through the rest of the games?"
    "Maybe I can just sleep it off. I'll climb a nearby tree and sleep there, to be safe."
    scene sleep
    with Dissolve(.5)
    # end this one w a black screen/fade thing
    # We wake up to a thud, who's that? It's Tam at the bottom! He tells us to come down and fight him(write some threats here) (spruha)
    play sound "thud.mp3"
    "What was that sound?"
    scene forestbg
    with Dissolve(.5)
    play sound "thud.mp3"
    scene tam tree
    m "COME DOWN HERE AND FIGHT!"
    n "No!! Please!!"
    m "Come down and challenge me you coward! Or I'll chop this tree down where it stands."
    "Oh no..."

    # Face off with Tam. At the end, he disappears. (spruha)


    # We run away, and after like one frame of just getting away, we spot Jamilton, and fight him. (snack)


    # After fighting Hamilton, he's like "wait wait wait let's just team up and take down Zino and Aucoin! They're too powerful for either of us to fight them alone. We're better together." (snack)


    # We approach Zino and Aucoin and Hamilton fights them. Hamilton disappears! (maddy)

    
    # Zino and Aucoin approach us and start to fight us. At the end, they disappear. (maddy)
    scene forestbg
    show aucoin zino fight:
        yalign 0.2
        xalign 0.5
    a "why isn't the water boiling???"
    z "because of the latent heat of vapourization"
    a "How many grams of NaOH are required to saponify 500g of Corn oil (SAP value = 137)"
    label a_q1:
        menu:
            '75.4g':
                jump a1_incorrect_1

            '65.6g':
                jump a1_correct
        
            '72.8g':
                jump a1_incorrect_2

        label a1_incorrect_1:
            $ menu_flag = False
            a "Hmmmm, someone hasnt been studying Perry's Chemical Engineering Handbook - try again."
            jump a_q1

        label a1_correct:
            $ menu_flag = True
            a "Wow - i'm impressed."
            jump a1_done
     
        label a1_incorrect_2:
            $ menu_flag = False
            a "You're gonna burn someone with that soap - try again."
            jump a_q1
   
    label a1_done:
    z "it seems my partner here may have underestimated you, I won't make the same mistake."
    z "balance this equation!, _ CH4 + _ O2 -> CO2 + 2H2O"
    label z_q1:
        menu:
            '1,2':
                jump z1_correct

            '1,1':
                jump z1_incorrect_1
        
            '3,4':
                jump z1_incorrect_2

        label z1_incorrect_1:
            $ menu_flag = False
            z "How are you going to get anywhere in life if you can't balance a simple chemical equation!"
            jump z_q1

        label z1_correct:
            $ menu_flag = True
            z "Well that was a warm up question."
            jump z1_done
     
        label z1_incorrect_2:
            $ menu_flag = False
            z "How are you going to get anywhere in life if you can't balance a simple chemical equation!"
            jump z_q1
    label z1_done:


        # ... the game continues here.
 

    # Looks into the sky, and there's 22 cannons. Looks like it's just me and Pendar left. The Gamemakers make an announcement that they replenished the Cornucopia. We decide to go, since we're running out of supplies. We go to the Cornucopia. Pendar is behind us and challenges us to a fight. (spruha)


    # Pendar fight. She doesn't disappear tho, just fades into the next scene. (spruha)


    # Dean MW says we won and offers us admission! (cameron)

    # This ends the game.

    return



