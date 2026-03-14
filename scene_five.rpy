label scene_five:
    scene bg room_full 
    show luzhin test at left
    l "etc.."
    show anastasia test at right
    l "General asks Who will guard you in absence?"
    #turn to Anastasia, study him, high angle
    #internal dialogue before deciding
    #THIS SCENE IS IMPORTANT SO EMPHASIZE THE CINEMATOGRAPHY/CHOICE, LAST ONE
    l "As for this man, I will take him as my..."

    menu:
        "Prisoner":
            $ anastasia_animosity += 3
            l "idk i do sum here, everyone gasps"    
                
            jump after_five

        "Private Guard": #or protector
            $ choice = "no"
            jump after_five      
    
label after_five:
    if anastasia_animosity >= 4:
        a "text" 
    else:
        a "text"

       
    
    return    

    # This ends the game.

    return