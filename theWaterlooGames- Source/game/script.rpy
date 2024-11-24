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
define g = Character("Gamemakers")

image stagebg:
     "stagebg.png"
     zoom 1.5
image black:
     "blackscreen.jpg"
     zoom 4
image map:
     "waterloomap.png"
     zoom 1
image intro = Text("This is a text displayable.", size=30)
image waterloo = "waterloobg.jpg"
image edcombg = "edcombg.png"
image toolbg:
     "toolbg.png"
     zoom 2
image nightbg:
     "nightbg.jpg"
     zoom 3
image fallen:
     "the fallen.jpg"
     zoom 10
#image cornucopiabg:
#   "cornucopiabg.png"
image forestbg:
    "forestbg.png"
    zoom 4
image jhforest: 
    'jh forest.jpg'
    zoom 2
image justin: 
    "justin.png"
    zoom 2
image tool:
    "toolpose.png"
    zoom 0.75

image pendar cornucopia:
     "pendar cornucopia.png"
     zoom 0.35
image pendar cornucopiatwo:
     "pendar cornucopia.png"
     zoom 0.6
image pendar fighting:
     "pendar fighting.png"
     zoom 3
image p q3:
     "p q3.png"
     zoom 2


image tam cornucopia:
     "tam cornucopia.png"
     zoom 1.23
image tam cornucopiatwo:
     "tam cornucopia.png"
     zoom 1.6
image tam fighting:
     "tam fighting.png"
     zoom 1.75
image tam tree:
     "tam tree.png"
     zoom 3.5



image intro:
     "firstintroscene.png"
     zoom 0.65
image marlyn:
     "marlyn.png"
     zoom 0.75


image aucoin cornucopia:
     "aucoin cornucopia.png"
     zoom 0.3
image aucoin cornucopiatwo:
     "aucoin cornucopia.png"
     zoom 0.7
image aucoin zino fight: 
    "aucoin zino fight.png"
    zoom 0.7


image zino cornucopia:
     "zino cornucopia.png"
     zoom 0.27
image zino cornucopiatwo:
     "zino cornucopia.png"
     zoom 0.6


image dean mary wells end = "dean mary wells end.png"
image kamkar cornucopia:
     "kamkar cornucopia.png"
     zoom 0.72
image kamkar cornucopiatwo:
     "kamkar cornucopiatwo.png"
     zoom 1.2
image kamkar intro:
     "kamkar intro.png"
     zoom 1.1


image jamilton cornucopia:
     "jamilton cornucopia.png"
     zoom 0.31
image jamilton cornucopiatwo:
     "jamilton cornucopia.png"
     zoom 0.5


image jamilton talk = "jamilton talk.png"
image bg river:
    "bg river.jpg"
    zoom 3.25
image sleep:
    "sleep.jpg"
    zoom 4
image bush:
    "bush final.png"

define nvle = Character("~", color="#ffffff", kind=nvl)
 

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
    play music "entering name music.mp3"
    scene map:
        xalign 0.0
        yalign 0.4
    nvle "Welcome, students of Waterloo. Welcome to District 12's reaping of the 29th annual Hunger Games." 
    nvle "As you may know, disaster struck what used to be Old Waterloo, and what rose from the ashes came the new land of Great Waterloo."
    nvle "Great Waterloo is the land we all stand on now."
    nvle "Great Waterloo was a shining capitol ringed by students and professors, each contributing to one specialty in the majority."
    nvl clear
    nvle "That is, until the Dark Days. The districts began rebelling against the capitol which obviously resulted into the unfortunate event of a total duel of wit breaking out."
    nvle "And yet, the capitol predictably took the title of “winner” by taking total destruction seriously and erasing District 13's civilization forever."
    nvle "Now, the Waterloo Games was the result of this happening and must go on. In the event of the uprising, each class must offer one student tribute to participate in the Waterloo Games..."
    nvl clear
    scene waterloo
    show kamkar intro:
        xalign 0.999
        yalign -0.9
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Player"
    define n = Character("[name]")
    play sound "i volunteer as tribute.mp3"
    with Dissolve(1)

    scene waterloo
    nvle "Well, isn't this a shock..."
    nvle "There hasn't been a volunteer since the 2024 games 5 years ago"
    nvle "Good Luck [name], and may the odds be ever in your favor..."
    nvl clear
    stop music fadeout 1
    with Dissolve(0.5)
    play sound "may the odds.mp3"
    with Dissolve(2.5)

    # Justin and Marlyn explain how the games work, and then usher you off the go on the Tool show (maddy)
    scene stagebg   
    show justin:
        xalign 0.0 
        yalign 0.4
    show marlyn:
        xalign 1.0 
        yalign 0.2

    show marlyn behind justin
    j "There you are! C'mon, you're supposed to be on The Tool Show in 5 minutes!!!"
    n "Wait! I don't even know what's happening right now" 
    j "Y'know what, I so resonate with that"
    y "Don't worry, you seem like a tough fighter. When the Games begin, you'll face off your opponents and defeat them by answering their questions, but beware, I've heard there's some tough professors from the districts this year."
    play sound "audience clapping.mp3" 
    j "Now i'd love to chit chat some more, but you've gotta head on stage now"
    n "stage?!?!"
    scene sleep
    stop sound fadeout 1.0
    with Dissolve(.5)

    # The Tool asks you a bunch of questions; just interactive not for points (snack)
    scene toolbg
    show tool
    t "Welcome to the Tool show! With your beloved host, Tool, me!"
    t "Today we have a very special guest joining us, please welcome [name]!"
    play sound "toolclap.mp3"
    with Dissolve(1)

    t "So why don't you tell us a bit about yourself?"
    python:
        prog = renpy.input("What program are you in?")
        prog = prog.strip() or "None"

    t "Wow... in [prog], quite impressive don't you think?"
    n "Well, it's definetly tough but so am I, that's why I have no doubt that I can win this years Waterloo Games..."
    











































    # Cut to the Cornucopia; go through each tribute and look at their stats(the player is the one thinking things about them, so there should be no name in the overhead part) (cameron)
    scene intro
    with pixellate
    show pendar cornucopia:
        xalign 0.0
        yalign 0.7
    show tam cornucopia:
        xalign 1.0
        yalign 0.7
    show aucoin cornucopia:
        xalign 0.48
        yalign 0.2
    show jamilton cornucopia:
        xalign 0.8
        yalign 0.57
    show zino cornucopia:
        xalign 0.29
        yalign 0.3
    show kamkar cornucopia:
        xalign 0.02
        yalign 0.2
    #show azevedo cornucopia:
        #xalign 1.0
        #yalign 0.0
    "Wow, I didn't think that there would be so many other tributes to face off against."
    "Some of them look like really tough opponents."
    "Hmmm... I think I might recognize some of these people..."


    scene intro
    with wipeup
    show pendar cornucopiatwo:
        xalign 0.5
        yalign 0.5
    with zoomin
    "{b} Pendar Mahmoudi | District 3 | Technology"
    "Pendar Mahmoudi is a tech whizz, her computer skills are impeccable. Although she's not from a career district, she's been training and is sneaky like a Python. If you encounter her, don’t try to trick her, you might just end up in an infinite loop of regret."
    "{i} Strengths: Coding, Debugging, Rubber duck distribution \nWeaknesses: Syntax Errors, Semantic Errors"


    scene intro
    with wipedown
    show kamkar cornucopiatwo:
        xalign 0.5
        yalign 0.85
    with zoomin
    "{b} Milad Kamkar | District 4 | Fishing"
    "Milad Kamkar is here to take names and kick ass. Despite his area of expertise, he’s no nano-challenge. Before you attack, make sure you draw a flow-chart and complete a degree of freedom analysis. Facing off with this opponent will send you into a continuous, steady-state of misery."
    "{i} Strengths: Material balance, Recycling \nWeaknesses: When accumulation is not zero."


    scene intro
    with wipeup
    show zino cornucopiatwo:
        xalign 0.5
        yalign 0.5
    with zoomin
    "{b} Zino Ojogbo | District 1 | Luxury"
    "Zino Ojogbo is a fierce fighter. She’s from a Career district, so she’s been training for the games all her life. When you’re fighting her, make sure you know your chemistry concepts. You don’t want to test her when she’s in her element."
    "{i} Strengths: Charisma, Combustion analysis \nWeaknesses: pH over 14"

    scene intro
    with wipedown
    show aucoin cornucopiatwo:
        xalign 0.5
        yalign 0.5
    with zoomin
    "{b} Marc Aucoin | District 2 | Masonry"
    "Marc Aucoin is a jack of all trades. Whether it's formulating a luxurious soap or harnessing the power of Acylglycerophosphate acyltransferase 4, he’s always got something up his sleeve. Make sure you scrub up on your soap knowledge when facing off Aucoin, or face the PEO misconduct committee."
    "{i} Strengths: Perry's Chemical Engineering Handbook, Line calculations \nWeaknesses: Copilot"

    scene intro
    with wipeup
    show azevedo cornucopiatwo:
        xalign 0.5
        yalign 0.5
    with zoomin
    "{b} Matheus Azevedo | District 11 | Agriculture"
    "Matheus Azevedo is sly like a fox. With the power of calculus, he’s honed his mathematics skills and won’t go down without a fight. Hopefully you know your optimization, integration, and trigonometry. Don’t test his limits, or you might end up in the l’Hopital!"
    "{i} Strengths: Controlling geese, Implicit differentiation \nWeaknesses: Division by zero"

    scene intro
    with wipedown
    show jamilton cornucopiatwo:
        xalign 0.5
        yalign 0.5
    with zoomin
    "{b} Jordan Hamilton | District 8 | Textiles"
    "Jordan Hamilton is not to be trifled with. Don’t let his friendly demeanor fool you, because everyone here is in it to win it. Make sure to practice your row reducing, vector operations, and never let your guard down!"
    "{i} Strengths: Taming cats, Calculating determinants \nWeaknesses: Visualizing R7"

    scene intro
    with wipeup
    show tam cornucopiatwo:
        xalign 0.5
        yalign 0.5
    with zoomin
    "{b} Micheal Tam | District 5 | Power"
    "Michael Tam is one of the most knowledgeable of the tributes. He’s well known in Waterloo for his grasp on process data analysis, manometers, and density. Be wary while you’re facing off with this tribute, and don’t fold under pressure!"
    "{i} Strengths: Strengths: Strength of a tank, His handy manometer \nWeaknesses: Finding mass fraction from mole fraction"


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
    yalign 0.5 
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
            jump m2_correct

        "4.0 K/kPa":
            jump m2_incorrect_2

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
    hide tam fighting with Fade(0.1, 0.0, 0.1, color='#fff')
    show forestbg

    # We run away, and after like one frame of just getting away, we spot Jamilton, and fight him. (snack)
    scene jhforest
    show jamilton talk:
        yalign 0.35
        xalign 0.5
    "I barely escaped Tam's wrath, running further into a hillier part of the forest. After nearly tripping over a large root, I spotted him. Jordan Hamilton—and he spotted me."
    h "You really thought you could sneak up on me, huh?"
    n "What—no, it's not like that!"
    h "You're not fooling me that easily! Come here and fight!"
    label j_q2:
        python:
            matrix_A = [[1],[2],[3]]
            matrix_B = [[-1],[1],[2]]
            correct_proj = [['-7/6'],['7/6'],['7/3']]
            wrong_b = [['13/6'],['5/6'],['2/3']]
            wrong_c = [[0],[3],[5]]
            wrong_d = [[1,-1],[2,1],[3,2]]
        h "Fine, let's make this tougher. What's the projection of B onto A? A is [matrix_A], and B is [matrix_B]."
        menu:
            "[correct_proj]":
                jump j_q2_correct
            "[wrong_b]":
                jump j_q2_wb
            "[wrong_c]":
                jump j_q2_wc
            "[wrong_d]":
                jump j_q2_wd
        label j_q2_correct:
            h "Alright, so you're not trivial."
            jump j_q3
        label j_q2_wb:
            h "ermmmm"
            jump j_q2
        label j_q2_wc:
            h "bro.... that's not..."
            jump j_q2
        label j_q2_wd:
            h "what the sigma"
            jump j_q2
    # fight will happen here
    # After fighting Hamilton, he's like "wait wait wait let's just team up and take down Zino and Aucoin! They're too powerful for either of us to fight them alone. We're better together." (snack)
    

    # We approach Zino and Aucoin and Hamilton fights them. Hamilton disappears! (maddy)
    scene forestbg 
    show aucoin zino fight:
        zoom 0.75
        yalign 0.5
        xalign 1.0
    show bush:
        zoom 2
        yalign 1.3
        xalign 0.8

    show jamilton talk:
        yalign 0.1
        xalign -0.5
        xzoom -1
        zoom 0.8 
    z "Oh look - it's another tribute!"
    a "That's Jordan Hamilton. Don't worry about him, his attack questions can't hurt us - he works in a different dimension."
    h "oh no"
    h "I don't know if I can fight 2 tributes at once."
    scene sleep
    with Dissolve(0.7)
    scene forestbg 
    
    show aucoin zino fight:
        zoom 0.75
        yalign 0.5
        xalign 1.0
    show bush:
        zoom 2
        yalign 1.3
        xalign 0.8
   
    z "Hamilton put up more of a fight than I thought."
    a "Yeah, I almost lost in our third round - cross products always trip me up."
    "Oh no! can't believe they got Hamilton!"
    play sound "leaves.mp3"
    z "What was that sound?"
    stop sound 
    "uh oh I hope they didn't hear me."
    a "Who's there?!!!"

    # Zino and Aucoin approach us and start to fight us. At the end, they disappear. (maddy)
    scene forestbg
    show aucoin zino fight:
        yalign 0.2
        xalign 0.5
    a "Well well well"
    a "why isn't it [name] the mystery tribute."
    n "you must be Zino Ojobo and Marc Aucoin"
    z "Good guess"
    a "Enough chit chat!"
    a "Are you ready to meet the same fate as your friend Hamilton?"
    n "We'll see about that!" 
    a " First question: How many grams of NaOH are required to saponify 500g of Corn oil (SAP value = 137)"
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
            play sound "oof.wav"
            a "Wow - i'm impressed." with vpunch 
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
            play sound "oof.wav"
            z "Well that was a warm up question." with vpunch
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
            play sound "oof.wav"
            z "You appear to be more of a worthy opponent than I thought." with vpunch
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
        play sound "oof.wav"
        a "Wow I'm suprised someone like you would care to know that." with vpunch
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
            play sound "oof.wav"
            a "Noooo!!! I've lost to [name] the master soap maker - Zino, destroy them!!!" with vpunch
            jump a3_done
            
    label a3_done:
    z "It appears you've defeated my partner, don't assume i'll go down that easily"
    z "for my final question: 2 gasses are separated by a barrier in a container. One side contains 2L of H2 (g) at 0.5 atm and the other side contains 1 L of N2 (g) at 2 atm. When the barrier is removed, what is the total pressure of the container?"
    label z_q3:
        $ ans_zq3 = renpy.input("How many atm? (1 sig. fig.): ")
        $ is_true = (ans_zq3.strip() == "1")

    # Display the result (True or False)
    if is_true:
        play sound "oof.wav"
        z "It...it can't be! I lost?! Nooooo!!!!" with vpunch
        jump z3_done
    else:
        z "I see you can't handle the pressure of that question!!"
        jump z_q3

    label z3_done:
    define flashbulb = Fade(0.1, 0.0, 0.1, color='#fff')

    hide aucoin zino fight with flashbulb

    show forestbg
    ""
        # ... the game continues here.
 

# Looks into the sky, and there's 22 cannons. Looks like it's just me and Pendar left. The Gamemakers make an announcement that they replenished the Cornucopia. We decide to go, since we're running out of supplies. We go to the Cornucopia. Pendar is behind us and challenges us to a fight. (spruha)
scene nightbg with Dissolve(.5)
"By the time the fight with Zino and Aucoin was over, it was already night time."
"I'm so tired. I can't believe it's only been two days."
scene the fallen with Dissolve(.5)
play sound "cannon.mp3"
play sound "cannon.mp3"
play sound "cannon.mp3"
"I heard 22 cannons, I think it's just me and Pendar left now."
play music "anthem.mp3"
"Looks like the Gamemakers have an announcement to make."
g "What a riveting first day we've had! This might be our fastest game yet!"
g "A message for the remaining tributes:"
g "The Cornucopia will be replenished tomorrow morning."
scene nightbg with Dissolve(.5)
"Hmmm, I guess I should head there. I don't have much left."
"Tomorrow morning, I'll go to the Cornucopia."
stop music fadeout 1
scene intro with Fade(0.5, 0.5, 0.5)
"Okay, I just need to get some supplies and quickly leave."
p "Funny seeing you here"
"She's right behind me, isn't she..."
# Pendar fight. She doesn't disappear tho, just fades into the next scene. (spruha)
show pendar fighting:
     xalign 0.5
     yalign 0.0
p "Look kid, I don't take any pleasure in fighting you."
n "Then why are you doing this?!"
n "It's my first time here. I have no idea what I'm doing. I don't want to be eliminated."
p "I know, but I can't afford to get eliminated either."
p "So let's see if you have what it takes."

label p_q1:
     p "Where does the caption on a figure go?"
     menu:
        "Beside it":
            jump p1_incorrect1
                
        "Above it":
            jump p1_incorrect_2

        "Below it":
            jump p1_correct

label p1_correct:
     $ menu_flag = True
     p "Hm. You might make a worthy opponent after all."
     jump p_q2

label p1_incorrect_1:
     $ menu_flag = False
     p "That answer is nonsense."
     jump p_q1

label p1_incorrect_2:
     $ menu_flag = False
     p "[name], you silly little tribute."
     jump p_q1

label p_q2:
     p "What is the value of p2 as it is defined:" 
     p "p2 = ((True and False) and (True or True)) or ((False or True) and (True or False))"
     menu:
        "False":
            jump p2_incorrect

        "True":
            jump p2_correct

label p2_incorrect:
     $ menu_flag = False
     p "Someone doesn't know how booleans work..."
     jump p_q2

label p2_correct:
     $ menu_flag = True
     p "Well you had a fifty-fifty chance, so it's not that big of a deal..."
     jump p_q3

label p_q3:
     show p q3:
        xalign 0.0
        yalign 1.0
     p "Which of the following evaluates this function using python?"
     menu:
        "(40*(x**3) + 13*(x**2) -5*x + 17)*42*(x**4))/(((48*x + 56)**0.5) - (12*(x**(3/2))))":
            jump p3_correct

        "(40*(x^3) + 13*(^2) -5*x + 17)*42*(x^4))/(((48*x + 56)^0.5) - (12(x^(3/2))))":
            jump p3_incorrect_1

        "(40x**3 + 13x**2 -5x + 17)*42x**4))/(((48x + 56)**0.5) - (12(x**(3/2))))":
            jump p3_incorrect_2

label p3_correct:
     $ menu_flag = True
     jump p_end

label p3_incorrect_1:
     $ menu_flag = False
     p "You tried, and that's what counts.."
     jump p_q3

label p3_incorrect_2:
     $ menu_flag = False
     p "You tried, and that's what counts.."
     jump p_q3

label p_end:
     hide pendar fighting with Fade(0.1, 0.0, 0.1, color='#fff')

# Dean MW says we won and offers us admission! (cameron)

# This ends the game.

return

