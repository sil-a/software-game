screen stats_screen():

    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20

    vbox:
        spacing 10

        text "Recklessness: [ooc_reckless]"
        text "Compassion: [ooc_compassionate]"
        text "Suspicion: [ooc_suspicion]"
        text "Anastasia's Trust: [anastasia_trust]"
        textbutton "Return":
            action Return()
