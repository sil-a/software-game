
label start:
    scene bg room_full
    show luzhin test at left
    
    l "There will be Lance here, and just images, no sprites yet."
    l "The more the user clicks, the more dialogue is shown."
    l "Ultimately, I will be like whatever. Then my phone will flash white with a question"
    l "Testing if I can edit from Visual Studio"
    
    pause 0.5

    #lets see phone thing
    scene white with dissolve
    #have music here like a buzz

    
    l "WTH?!"

    jump the_question
    

label the_question:
    scene bg room_full
    show luzhin test at left
    show anastasia test at right
    a "Wanna isekai except phone asks"

    show screen yes_button
    pause

    menu:
        "Yes, lets go!!":
            $ choice = "yes"
            l "Stuff happens here after I pick yes"
                
            jump after_choice

        "No": 
            $ choice = "no"
            a "Stuff happens here after you pick no"
            jump after_choice
                  
    
label after_choice:
    hide screen yes_button
    l "A neutral event will happen here, but the next evets are determined by the answer to the previous question."
    if choice == "yes":
        l "My story changes here if i picked Yes previously" #elaborate
    else:
        l "My story changes here if I picked no previously"
    
    l "Kim Dokja wannabe"    
    jump scene_one

    