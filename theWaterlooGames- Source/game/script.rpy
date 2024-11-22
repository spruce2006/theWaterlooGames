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
image jhforest: 
    'jh forest.jpg'
    zoom 2
image justin: 
    "justin.png"
    zoom 2
image pendar cornucopia = "pendar cornucopia.png"
image tam cornucopia = "tam cornucopia.png"
image tam fighting:
    "tam fighting.png"
    zoom 1.5
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
image jamilton talk = "jamilton talk.png"
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
    j "There you are! C'mon, you're supposed to be on The Tool Show in 5 minutes!!! Have they explained what you're gonna be doing?"
    n "...no I'm even sure how to fight my oponents when the time comes."
    j "Y'know what, I so resonate with that"
    y "Don't worry, you seem like a tough fighter. When the Games begin, you'll face off your opponents and defeat them by answering their questions, but beware, I've heard there's some tough proffessors from the districts this year."
    j "Now i'd love to chit chat some more, but you've gotta head on stage now"

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
scene forestbg
show tam fighting:
    yalign 0.45 
    xalign 0.55
m "If you really have what it takes to win these games, then answer these questions."
label m_q1:
    m "Convert 360 kg/K to lb/R. Answer with the correct number of significant digits."
    menu:
        "440 lb/R":
            jump m1_correct
            
        "450 lb/R":
            jump m1_incorrect_1

        "430 lb/R":
            jump m1_incorrect_2

    label m1_correct:
        $ menu_flag = True
        m "It's correct, but don't celebrate so prematurely."
        jump m_q2

    label m1_incorrect_1:
        $ menu_flag = False
        m "Hah! You can't even answer such a simple question?"
        jump m_q1

    label m1_incorrect_2:
        $ menu_flag = False
        m "Hah! You can't even answer such a simple question?"
        jump m_q1

label m_q2:
    m "A graph of temperature(K) against pressure(kPa) has has the following plotted points:" 
    m "(256, 132), (275, 208), and (294, 284). What is the slope of this graph?"
    menu:
        "3.9 k/kPa":
            jump m2_incorrect_1

        "4.0 kPa/K":
            jump m2_incorrect_2

        "4.0 K/kPa":
            jump m2_correct 

    label m2_incorrect_1:
        $ menu_flag = False
        m "I didn't realize it was possible to meet someone this stupid. Try again."
        jump m_q2

    label m2_incorrect_2:
        $ menu_flag = False
        m "I didn't realize it was possible to meet someone this stupid. Try again."
        jump m_q2

    label m2_correct:
        $ menu_flag = True
        m "Urgh! You'll never get this last one!"
        jump m_q3

label m_q3:
    m "Mercury has an SG of 13.6. How many pounds of mercury are there in a 300 mL sample?"
    menu:
        "8.99 lbm":
            jump m3_correct

        "7.64 lbm":
            jump m3_incorrect_1

        "6.87 lbm":
            jump m3_incorrect_2

    label m3_correct:
        $ menu_flag = True
        m "No! No! It's not possible! You couldn't have beat me!"
        jump m_end

    label m3_incorrect_1:
        $ menu_flag = False
        m "I knew you weren't good enough to compete here."
        jump m_q3

    label m3_incorrect_2:
        $ menu_flag = False
        m "I knew you weren't good enough to compete here."
        jump m_q3

label m_end:
    m "I suppose I underestimated you."
    m "But mark my words..."
    m "You will rue this day."

    # We run away, and after like one frame of just getting away, we spot Jamilton, and fight him. (snack)
    scene jhforest
    show jamilton talk:
        yalign 0.35
        xalign 0.5
    "I barely escaped Tam's wrath, running further into a hillier part of the forest. After nearly tripping over a large root, I spotted him. Jordan Hamilton—and he spotted me."
    h "You really thought you could sneak up on me, huh?"
    n "What—no, it's not like that!"
    # fight will happen here
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
        a "hmmmm someone doesn't seem to care if their education is accredited"
        jump a_q2

    label a2_done:
    a "Now you're really asking for trouble, i'm going full force for this last question"
    a "When making a hard bar of soap, is using KOH as lye a better choice over NaOH?"
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
            a "Noooo!!! I've lost to [name] the master soap maker - Zino, destroy them!!!"
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



