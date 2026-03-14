label scene_three:

    scene bg room_full 
    show luzhin test at left
    l "more"
    show anastasia test at right
    l "Yea, so super cool stuff happens here"

    menu:
        "Humiliate the General":
            $ ooc_reckless += 2
            l "So... our beloved General xyz provoked xyz...?"    
            a "General here will crash out"    

            jump after_three

        "Agree with The General": 
            $ anastasia_animosity += 2
            jump after_three    
    
label after_three:
    if ooc_reckless >= 2:
        l "crowd gasps, general is fuming" 
    else:
        a "placeholder but im mad"
        
    
    jump scene_four