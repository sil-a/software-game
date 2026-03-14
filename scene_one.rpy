label scene_one:
    scene bg room_full #replace with an image of court
    show luzhin test at left
    l "Super cool text here"
    show anastasia test at right
    a "pretend there's an old priest dude here" #create old dude sprite
    l "Yea, so super cool stuff happens here"
    l "..."

    menu:
        "Stay Silent":
            $ not_ooc += 1
            a "Again, imagine im old and glazing Luzhin up"    
                
            jump after_one

        "More Details": 
            $ not_ooc = 0
            call screen stats_screen
            #display a page with whats going on/chapter1
            jump after_one
        
label after_one:
    if not_ooc >= 1:
        l "insert yap or menu option to see stats/story/recount" #place quotes here and elaborate
    else:
        a "User will have the opportunity to open a stats menu and listen"

        #regardless, user can open menu here HOWEVER their score is effected
    
    jump scene_two