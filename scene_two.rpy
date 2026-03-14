label scene_two:
    scene bg room_full 
    #effects from scene one put here
    show luzhin test at left
    l "more"
    show anastasia test at right
    l "Yea, so super cool stuff happens here"

    menu:
        "Any Witnesses?":
            $ choice = "yes"
            a "Again, imagine im old and buttering Luzhin up"    
                
            jump after_two

        "I would like to hear from the accused.": 
            $ ooc_suspicion += 2
            $ anastasia_trust += 1
            jump after_two 
       
    
label after_two:
    if ooc_suspicion >= 2:
        a "Dude xyz is like erm what, bros mute" 
    else:
        l "Dude xyz says yes and this dude steps forward"

        
    jump scene_three