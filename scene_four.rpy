label scene_four:
    scene bg room_full 
    show luzhin test at left
    l "more"
    show anastasia test at right
    l "General XYZ... you are to "

    menu:
        "...be placed on house arrest.":
            $ ooc_suspicion += 2
            l "ELABORATEEE"    
                
            jump after_four

        "...be forgiven.": 
            $ anastasia_animosity += 2
            $ ooc_compassionate += 1
            jump after_four  

        "...resume your position.": 
            $ anastasia_animosity += 1 
            jump after_four  
    
label after_four:
    if ooc_suspicion >= 3:
        a "dude asks if luzhin is alright/feverish" # and continue the plot
    if anastasia_animosity >= 2:
        a "idk i make a noise" #baaad choice, char goes down, ooc good
    else: 
        l "stuff" #bad for plot, change    

        
    jump scene_five