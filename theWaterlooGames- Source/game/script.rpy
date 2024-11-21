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
image cornicopiabg = "conicopiabg.png"
image forestbg:
    "forestbg.png"
    zoom 4
image justin: 
    "justin.png"
    zoom 2
image pendar cornicopia = "pendar cornicopia.png"
image tam cornicopia = "tam cornicopia.png"
image tam fighting = "tam cornicopia fighting.png"
image tam tree = "tam tree.png"
image marlyn:
    "marlyn.png"
    zoom 0.75
image aucoin cornicopia = "aucoin cornicopia.png"
image aucoin zino fight: 
    "aucoin zino fight.png"
    zoom 1.1
image zino cornicopia = "zino cornicopia.png"
image dean mary wells end = "dean mary wells end.png"
image kamkar cornicopia = "kamkar cornicopia.png"
image kamkar intro = "kamkar intro.png"

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


    # We run off the platform and face off with Azevedo. At the end, he disappears. (snack)


    # After the fight, we rush off to a river, drink water, go to sleep in a tree(these can just be images of a river, tree, then black) (spruha)


    # We wake up to a thud, who's that? It's Tam at the bottom! He tells us to come down and fight him(write some threats here) (spruha)


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
    z "ready for another question huh,"
    z '''Determine the equilibrium constant for a synthesis of ammonia reaction if the concentrations at equilibrium are 
    \[N2] = 0.025M  \[H2] = 0.0013M \[NH3] = 0.028M '''
    label z_q2:
        menu:
            '14274':
                jump z2_correct

            '45242':
                jump z2_incorrect_1
        
            '0.4525':
                jump z2_incorrect_2

        label z2_incorrect_1:
            $ menu_flag = False
            z "C'mon, the rate law equation isn't that hard, try again!"
            jump z_q2

        label z2_correct:
            $ menu_flag = True
            z "You appear to be more of a worthy opponent than I thought."
            jump z2_done
     
        label z2_incorrect_2:
            $ menu_flag = False
            z "that answer makes no sense at all!"
            jump z_q2
    label z2_done: 
    a "alright, im getting bored. Let's turn this up a notch"
    a "What is the organisation responsible for accrediting engineering programs? (acronym)"
    label a_q2:
        $ ans_aq2 = renpy.input("Answer: ")
        $ is_true = (ans_aq2.strip().upper() == "CEAB")

    # Display the result (True or False)
    if is_true:
        a "yas queen"
        jump a2_done
    else:
        b "hmmmm someone doesn't seem to care if their education is accredited"
        jump a_q2

    label a2_done:
    a "Now you're really asking for trouble, i'm going full force for this last question"
    a "When making a hard bar of soap, is using KOH as lye is a better choice over NaOH?"
    label a_q3:
        menu:
            'Yes':
                jump a3_incorrect

            'No':
                jump a3_correct
        

        label a3_incorrect:
            $ menu_flag = False
            a "You're bound to make an awful mushy soap!"
            jump a_q3

        label a3_correct:
            $ menu_flag = True
            a "Noooo!!! I've lost to a master soap maker - Zino, destroy them!!!"
            jump a3_done
            
    label a3_done:
    z "It appears you've defeated my partner, don't assume i'll go down that easily"
    z "for my final question: 2 gasses are separated by a barrier in a container. One side contains 2L of H2 (g) at 0.5 atm and the other side contains 1 L of N2 (g) at 2 atm. When the barrier is removed, what is the total pressure of the container?"
    label z_q3:
        $ ans_zq3 = renpy.input("How many atm? (1 sig. fig.): ")
        $ is_true = (ans_zq3.strip() == "1")

    # Display the result (True or False)
    if is_true:
        z "It...it can't be! I lost?! Nooooo!!!!"
        jump z3_done
    else:
        z "I knew I had you with that question!!"
        jump z_q3

    label z3_done:

        # ... the game continues here.
 

    # Looks into the sky, and there's 22 cannons. Looks like it's just me and Pendar left. The Gamemakers make an announcement that they replenished the Cornucopia. We decide to go, since we're running out of supplies. We go to the Cornucopia. Pendar is behind us and challenges us to a fight. (spruha)


    # Pendar fight. She doesn't disappear tho, just fades into the next scene. (spruha)


    # Dean MW says we won and offers us admission! (cameron)

    # This ends the game.

    return



