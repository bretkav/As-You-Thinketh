# The script of the game goes in this file.

# this block activates auto-play on dialogue for all characters except the player.

default _is_voiced = False

init python:
    preferences.afm_enable = True
    preferences.afm_time = 15  # default display time for unvoiced lines

    def v(filename):
        store._is_voiced = True
        renpy.music.play(filename, channel="voice")

    def auto_afm_time():
        if store._is_voiced:
            preferences.afm_time = 0.1
            store._is_voiced = False
        else:
            preferences.afm_time = 15

    config.start_interact_callbacks.append(auto_afm_time)

    def u_afm_callback(event, **kwargs):
        if event == "begin":
            preferences.afm_enable = False
        elif event == "end":
            preferences.afm_enable = True

    u = Character("[playername]", color="#3be4f0", callback=u_afm_callback, window_style="player_window")

# defining styles

style subtitle_window:
    background None
    xfill True
    yalign 0.98
    padding (40, 20)

style subtitle_namebox:
    background None
    xalign 0.5
    yanchor 1.0
    ypos 0

style subtitle_name:
    color "#FFFFFF"
    outlines []
    italic True
    textalign 0.5

style subtitle_text:
    color "#FFE800"
    outlines [(3, "#000000", 0, 0)]
    textalign 0.5
    xalign 0.5

style player_window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

# Declare NPCs in this game. The color argument colorizes the
# name of the character.

default playername = "Youthful Reader"
default player_appearance = "option_femme"

define j = Character("James",
    window_style="subtitle_window",
    what_style="subtitle_text",
    namebox_style="subtitle_namebox",
    who_style="subtitle_name"
)

define p = Character("The Poet",
    window_style="subtitle_window",
    what_style="subtitle_text",
    namebox_style="subtitle_namebox",
    who_style="subtitle_name"
)

# The game starts here.

label start:
    $ preferences.afm_enable = True
    $ preferences.afm_time = 15

    menu:
        "When you look in the mirror, what do you see?"
        "Masc":
            $ player_appearance = "option_masc"
        "Femme":
            $ player_appearance = "option_femme"
        "Ambiguous":
            $ player_appearance = "option_ambiguous"
        "I don't know and I don't care":
            pass
    menu:
        "Have you ever truly felt alive?"
        "Yes.":
            pass
        "No, never.":
            pass
        "What kind of question is that?":
            pass
        "I'm not answering that.":
            pass
    menu:
        "Do you believe you know what love is?"
        "Yes.":
            pass
        "No.":
            pass
        "I'm not sure.":
            pass
        "Okay, this is really starting to freak me out.":
            pass
    menu:
        "Do you have a lot of regrets in life?"
        "Yes, too many to count.":
            pass
        "No, I don't believe in having regrets.":
            pass
        "No. I've never done anything wrong in my life.":
            pass
        "What?":
            pass
    menu:
        "Do you have trouble sleeping through the night?"
        "Never.":
            pass
        "Sometimes.":
            pass
        "Always.":
            pass
        "I think I'm asleep right now. I am, aren't I?":
            pass

    "You are dreaming."

    scene bg cafe
    show james standing at center
    with Fade(0.0, 0.0, 3.0)

    "You know that none of this is real, but this cafe and this man seem so familiar..."
    "The man opens his mouth to speak."
    voice "audio/jamesaudio/james_1.mp3"
    j "You yourself are a maker of yourself..."
    voice "audio/jamesaudio/james_2.mp3"
    j "by virtue of the thoughts, which you choose and encourage;"
    voice "audio/jamesaudio/james_3.mp3"
    j "that mind is the master-weaver, both of the inner garment of character and the outer garment of circumstance,"
    voice "audio/jamesaudio/james_4.mp3"
    j "and I hope that, as you may have hitherto woven in ignorance and pain--"
    voice "audio/jamesaudio/james_5.mp3"
    j "you may now weave in enlightenment and happiness."

    "You ponder this."

    voice "audio/jamesaudio/james_6.mp3"
    j "What shall I call you?"
    $ playername = renpy.input("What shall I call you?", length=20)
    $ playername = playername.strip()
    if not playername or not any(c.isalnum() for c in playername):
        $ playername = "Youthful Reader"

    u "You can call me [playername]. Who are you?"
    label choices1:
        default knowsaboutjameslife = False
        voice "audio/jamesaudio/james_7.mp3"
        j "I do not think it is of much import. Do you?"
        menu:
            "Yeah, actually, I do.":
                jump choices1_a
            "No, you're right. It doesn't matter.":
                jump choices1_b

label choices1_a:
    voice "audio/jamesaudio/james_7a1.mp3"
    j "My name is James Allen. I hail from Leicester. I am the first in my family to learn the art of letters; my mother could neither read nor write."
    voice "audio/jamesaudio/james_7a2.mp3"
    j "I am a writer, a journalist, a spiritualist. With the help of my inimitable wife, Lily, I run a magazine. I am currently working on a book."
    voice "audio/jamesaudio/james_7a3.mp3"
    j "I had a sense that a person such as you would be here at this cafe. I lack the callowness of a young person; I must needs borrow your keen ear and your discernment, for I am working on a book."
    voice "audio/jamesaudio/james_7a4.mp3"
    j "I cannot ask my Lily for further revision on my message. We have a great love for one another and she lacks a certain objectivity. You do not know me--although you now know quite a bit about me."

    $ knowsaboutjameslife = True
    jump choices1_common

label choices1_b:
    voice "audio/jamesaudio/james_7b.mp3"
    j "Very good. I shall then continue."
    jump choices1_common

label choices1_common:
    scene bg cafe
    show james sitting at left
    with dissolve
    voice "audio/jamesaudio/james_8.mp3"
    j "Avail yourself of the other seat, [playername]. Let us discuss thought and character."

    u "Alright..."

    show player sitting at right
    show expression "player " + player_appearance + " sitting" as player at right
    with dissolve

# NOTE TO SELF:

# For pose changes later in the game, follow the same pattern:
# show expression "player " + player_appearance + " standing" as player at right
# Your images should be named to match the strings this produces, e.g.:
# image player option_masc sitting = "images/player_masc_sitting.png"
# image player option_masc standing = "images/player_masc_standing.png"
# image player option_femme sitting = "images/player_femme_sitting.png"

# END OF NOTE
    voice "audio/jamesaudio/james_9.mp3"
    j "There is an aphorism."
    voice "audio/jamesaudio/james_10.mp3"
    j "'As a man thinketh in his heart so is he,'"
    voice "audio/jamesaudio/james_11.mp3"
    j "This not only embraces the whole of a man's being,"
    voice "audio/jamesaudio/james_12.mp3"
    j "but is so comprehensive as to reach out to every condition and circumstance of his life."
    voice "audio/jamesaudio/james_13.mp3"
    j "A man is literally what he thinks, his character being the complete sum of all his thoughts."

    u "And a woman?"

    label choices2:
        default drinksrespectwomenjuice = False
        voice "audio/jamesaudio/james_14.mp3"
        j "The same. I use the word 'man', 'mankind', and 'men' to refer to all people."
        menu:
            "We stopped doing that a while ago.":
                jump choices2_a
            "Hell yeah, brother.":
                jump choices2_b
    label choices2_a:
        voice "audio/jamesaudio/james_14a1.mp3"
        j "So you did. I am old, though. I have a certain way of speaking, and I hope you will bear with me."
        u "I will."
        voice "audio/jamesaudio/james_14a2.mp3"
        j "Very good."
        $ drinksrespectwomenjuice = True
        jump choices2_common

    label choices2_b:
        voice "audio/jamesaudio/james_14b1.mp3"
        j "Er... certainly."
        u "Dudes rock."
        voice "audio/jamesaudio/james_14b2.mp3"
        j "Mhm. Yes. Quite."
        u "Boys rule, girls drool."
        voice "audio/jamesaudio/james_14b3.mp3"
        j "I have a wife I am quite fond of."
        u "I'm just kidding."
        voice "audio/jamesaudio/james_14b4.mp3"
        j "Well, then. Ha ha ha. I drown in mirth."
        voice "audio/jamesaudio/james_14b5.mp3"
        j "Let us now move on to graver matters, [playername]. Matters of import."
        jump choices2_common

label choices2_common:
    voice "audio/jamesaudio/james_15.mp3"
    j "As the plant springs from, and could not be without, the seed,"
    voice "audio/jamesaudio/james_15.mp3"
    j "so every act of a man springs from the hidden seeds of thought, and could not have appeared without them."

    u "'I think, therefore I am.'"
    voice "audio/jamesaudio/james_16.mp3"
    j "Quite. Note that this applies equally to those acts called 'spontaneous' and 'unpremeditated' as to those which are deliberately executed."
    voice "audio/jamesaudio/james_17.mp3"
    j "Act is the blossom of thought, and joy and suffering are its fruits; thus does a man garner in the sweet and bitter fruitage of his own husbandry."
    u "My grandfather always said that you reap what you sow..."
    voice "audio/jamesaudio/james_18.mp3"
    j "He was then a wise man indeed."
    voice "audio/jamesaudio/james_19.mp3"
    j "Much like my friend here, as a matter of fact. Pietro, please take the floor--you have such a way with words."

    show pietro poet at center
    with easeinright
    pause(1.0)

# TODO pietro the poet absolutely has to be wearing a beret and a green apron

    voice "audio/ppaudio/pp_1.mp3"
    "Pietro" "Thank you, James. It would be my pleasure."
    voice "audio/jamesaudio/james_20.mp3"
    j "My good man--you do have enough time left on your break, do you not?"
    voice "audio/ppaudio/pp_2.mp3"
    "Pietro" "My friend, there is always time enough for art..."
    voice "audio/ppaudio/pp_3.mp3"
    "The Poet" "Ahem."
    voice "audio/ppaudio/pp_4.mp3"
    "The Poet" "Thought in the mind hath made us what we are"
    voice "audio/ppaudio/pp_5.mp3"
    "The Poet" "By thought was wrought and built. If a man's mind"
    voice "audio/ppaudio/pp_6.mp3"
    "The Poet" "Hath evil thoughts, pain comes on him as comes"
    voice "audio/ppaudio/pp_7.mp3"
    "The Poet" "The wheel the ox behind...."
    voice "audio/ppaudio/pp_8.mp3"
    "The Poet" "..If one endure"
    voice "audio/ppaudio/pp_9.mp3"
    "The Poet" "In purity of thought, joy follows him"
    voice "audio/ppaudio/pp_10.mp3"
    "The Poet" "As his own shadow—sure."
    pause(2.0)
    j "Bravo! Bravo!"
    j "Beautiful words as always, my friend."
    "Pietro" "Thank you, my friend. My colleague in wordsmithery. It was my pleasure to perform my poem."
    "Pietro" "Fare thee well--both of you. My break has ended, and I must return to my post at the espresso machine..."
    hide pietro poet
    with easeoutright
    menu:
        "That was weird.":
            jump choices3_common
        "Wow, what a beautiful poem.":
            jump choices3_common

label choices3_common:
    j "Indeed."
    j "Man is a growth by law, and not a creation by artifice,"
    j "and cause and effect is as absolute and undeviating in the hidden realm of thought as in the world of visible and material things."
    j "A noble and Godlike character is not a thing of favour or chance,"
    j "but is the natural result of continued effort in right thinking,"
    j "the effect of long-cherished association with Godlike thoughts."
    j "An ignoble and bestial character, by the same process, is the result of the continued harbouring of grovelling thoughts."
    j "Man is made or unmade by himself;"
    j "in the armoury of thought he forges the weapons by which he destroys himself;"
    j "he also fashions the tools with which he builds for himself heavenly mansions of joy and strength and peace."
    j "By the right choice and true application of thought, man ascends to the Divine Perfection;"
    j "by the abuse and wrong application of thought, he descends below the level of the beast."
    j "Between these two extremes are all the grades of character, and man is their maker and master."
    j "Of all the beautiful truths pertaining to the soul which have been restored and brought to light in this age,"
    j "none is more gladdening or fruitful of divine promise and confidence than this—"
    j "that man is the master of thought, the moulder of character, and the maker and shaper of condition, environment, and destiny."
    j "As a being of Power, Intelligence, and Love, and the lord of his own thoughts,"
    j "man holds the key to every situation,"
    j "and contains within himself that transforming and regenerative agency by which he may make himself what he wills."
    j "Man is always the master, even in his weaker and most abandoned state;"
    j "but in his weakness and degradation he is the foolish master who misgoverns his 'household.'"
    j "When he begins to reflect upon his condition,"
    j "and to search diligently for the Law upon which his being is established,"
    j "he then becomes the wise master, directing his energies with intelligence, and fashioning his thoughts to fruitful issues."
    j "Such is the conscious master,"
    j "and man can only thus become by discovering within himself the laws of thought;"
    j "which discovery is totally a matter of application, self analysis, and experience."
    j "Only by much searching and mining, are gold and diamonds obtained,"
    j "and man can find every truth connected with his being, if he will dig deep into the mine of his soul;"
    j "and that he is the maker of his character, the moulder of his life, and the builder of his destiny, he may unerringly prove,"
    j "if he will watch, control, and alter his thoughts,"
    j "tracing their effects upon himself, upon others, and upon his life and circumstances,"
    j "linking cause and effect by patient practice and investigation,"
    j "and utilizing his every experience, even to the most trivial, everyday occurrence,"
    j "as a means of obtaining that knowledge of himself which is:"
    j "Understanding, Wisdom, Power."
    j "In this direction, as in no other, is the law absolute that:"
    
    show thebook at top
    with zoominout
    pause(1.0)

    "The Book" "He that seeketh findeth; and to him that knocketh it shall be opened;"

    hide thebook
    with zoominout
    pause(1.0)

    j "for only by patience, practice, and ceaseless importunity can a man enter the Door of the Temple of Knowledge."
    u "Then I will be patient, and I will practice."
    j "I know that you will."
    j "Let us now speak of the effect of Thought on circumstances."
    j "Man's mind may be likened to a garden, which may be intelligently cultivated or allowed to run wild;"
    j "but whether cultivated or neglected,"
    j "it must, and will, bring forth."
    j "If no useful seeds are put into it,"
    j "then an abundance of useless weed-seeds will fall therein, and will continue to produce their kind."
    j "Just as a gardener cultivates his plot, keeping it free from weeds, and growing the flowers and fruits which he requires,"
    j "so may a man tend the garden of his mind,"
    j "weeding out all the wrong, useless, and impure thoughts,"
    j "and cultivating toward perfection the flowers and fruits of right, useful, and pure thoughts."
    j "By pursuing this process, a man sooner or later discovers that he is:"
    j "the master-gardener of his soul,"
    j "and the director of his life."
    j "He also reveals, within himself, the laws of thought,"
    j "and understands, with ever-increasing accuracy,"
    j "how the thought-forces and mind elements operate in the shaping of his character, circumstances, and destiny."
    j "Thought and character are one,"
    j "and as character can only manifest and discover itself through environment and circumstance,"
    j "the outer conditions of a person's life will always be found to be harmoniously related to his inner state."
    u "I've been struggling with things lately, and I haven't been doing well."
    u "I'm not living up to my ideals."
    j "What I have said does not mean that a man's circumstances at any given time are an indication of his entire character."
    u "So I am more than the person I am in low circumstances?"
    j "Indeed--with the exception of when those circumstances are intimately connected with some vital thought-element within yourself..."
    j "so intimately connected, that, for the time being, they are indispensable to your development..."
    u "Oh, that's not the case."
    j "Then your circumstances right now are not an indication of your entire character."
    j "Every man is where he is by the law of his being;"
    j "the thoughts which he has built into his character have brought him there,"
    j "and in the arrangement of his life there is no element of chance, but all is the result of a law which cannot err."
    j "This is just as true of those who feel 'out of harmony' with their surroundings as of those who are contented with them."
    j "As a progressive and evolving being,"
    j "man is where he is that he may learn that he may grow;"
    j "and as he learns the spiritual lesson which any circumstance contains for him, it passes away and gives place to other circumstances."
    j "Man is buffeted by circumstances so long as he believes himself to be the creature of outside conditions,"
    j "but when he realizes that he is a creative power,"
    j "and that he may command the hidden soil and seeds of his being out of which circumstances grow,"
    j "he then becomes the rightful master of himself."
    j "That circumstances grow out of thought every man knows who has for any length of time practised self-control and self-purification,"
    j "for he will have noticed that the alteration in his circumstances has been in exact ratio with his altered mental condition."
    j "So true is this that when a man earnestly applies himself to remedy the defects in his character, and makes swift and marked progress,"
    j "he passes rapidly through a succession of vicissitudes."
    j "The soul attracts that which it secretly harbours;"
    j "that which it loves, and also that which it fears;"
    j "it reaches the height of its cherished aspirations;"
    j "it falls to the level of its unchastened desires,—and circumstances are the means by which the soul receives its own."
    j "Every thought-seed sown or allowed to fall into the mind,"
    j "and to take root there,"
    j "produces its own,"
    j "blossoming sooner or later into act, and bearing its own fruitage of opportunity and circumstance."
    j "Good thoughts bear good fruit, bad thoughts bad fruit."
    j "The outer world of circumstance shapes itself to the inner world of thought, and both pleasant and unpleasant external conditions are factors,"
    j "which make for the ultimate good of the individual."
    j "As the reaper of his own harvest, man learns both by suffering and bliss."
    j "Following the inmost desires, aspirations, thoughts, by which he allows himself to be dominated,"
    j "--pursuing the will-o'-the-wisps of impure imaginings or steadfastly walking the highway of strong and high endeavour--"
    j "a man at last arrives at their fruition and fulfilment in the outer conditions of his life."
    j "The laws of growth and adjustment everywhere obtains."
    j "A man does not come to the almshouse or the jail by the tyranny of fate or circumstance."
    u "I don't agree with that."
    j "You may disagree. That is fine, of course you may."
    j "I believe that a man finds himself in these places by the pathway of grovelling thoughts and base desires."
    j "A pure-minded man does not fall suddenly into crime by stress of any mere external force;"
    j "the criminal thought had long been secretly fostered in the heart, and the hour of opportunity revealed its gathered power."
    u "Maybe."
    j "This is my philosophy. You may write your own."
    u "I will."
    j "I anticipate reading it. I believe that the philosophies of life are the greatest thing we may put our minds to."
    j "I sometimes fear that your generation does not value this science--"
    u "Writing is an art."
    j "Philosophy is an art and a science."
    j "In any case, I encourage you to put your thoughts to paper, or canvas, or perhaps the digital realm that we find ourselves in now."
    u "I will."
    j "Good."
    u "So... you were saying?"
    j "Indeed. Ahem."
    j "Circumstance does not make the man; it reveals him to himself."
    j "No such conditions can exist as descending into vice and its attendant sufferings apart from vicious inclinations,"
    j "or ascending into virtue and its pure happiness without the continued cultivation of virtuous aspirations;"
    j "and man, therefore, as the lord and master of thought, is the maker of himself the shaper and author of environment."
    j "Even at birth the soul comes to its own,"
    j "and through every step of its earthly pilgrimage,"
    j "it attracts those combinations of conditions which reveal itself,"
    j "which are the reflections of its own purity and impurity,"
    j "its strength and weakness."
    j "There are some books you may be familiar with--"
    u "Self-help books?"
    j "Indeed--"

    show thelawofattraction at top
    with zoominout
    pause(1.0)
    with dissolve

    j "The Law of Attraction"

    hide thelawofattraction
    show thesecret at top

    j "The Secret"

    hide thesecret
    with zoominout
    pause(1.0)
    with dissolve

    j "Books such as these--have you read them?"
    u "When they came out, I did."
    j "Did you find them useful?"
    u "Not very."
    j "That is to be expected."
    j "Men do not attract that which they want, but that which they are."
    j "Their whims, fancies, and ambitions are thwarted at every step, but their inmost thoughts and desires are fed with their own food, be it foul or clean."
    j "The 'divinity that shapes our ends' is in ourselves; it is our very self."
    j "Only himself manacles man:"
    j "thought and action are the gaolers of Fate—"
    j "they imprison, being base; they are also the angels of Freedom—they liberate, being noble."
    j "Not what he wishes and prays for does a man get, but what he justly earns."
    j "His wishes and prayers are only gratified and answered when they harmonize with his thoughts and actions."
    j "In the light of this truth, what, then, is the meaning of 'fighting against circumstances?'"
    j "It means that a man is continually revolting against an effect without, while all the time he is nourishing and preserving its cause in his heart."
    j "That cause may take the form of a conscious vice or an unconscious weakness;"
    j "but whatever it is, it stubbornly retards the efforts of its possessor, and thus calls aloud for remedy."
    j "Men are anxious to improve their circumstances, but are unwilling to improve themselves;"
    j "they therefore remain bound."
    j "The man who does not shrink from self-crucifixion can never fail to accomplish the object upon which his heart is set."
    j "This is as true of earthly as of heavenly things."
    j "Even the man whose sole object is to acquire wealth must be prepared to make great personal sacrifices before he can accomplish his object; and how much more so he who would realize a strong and well-poised life?"

    show poorman wretched
    with dissolve

    j "Here is a man who is wretchedly poor."
    j " He is extremely anxious that his surroundings and home comforts should be improved,"
    j "yet all the time he shirks his work, and considers he is justified in trying to deceive his employer on the ground of the insufficiency of his wages."
    j "Such a man does not understand the simplest rudiments of those principles which are the basis of true prosperity,"
    j "and is not only totally unfitted to rise out of his wretchedness,"
    j "but is actually attracting to himself a still deeper wretchedness by dwelling in, and acting out, indolent, deceptive, and unmanly thoughts."

    hide poorman wretched
    show richman wretched

    j "Here is a rich man who is the victim of a painful and persistent disease as the result of gluttony."
    j "He is willing to give large sums of money to get rid of it, but he will not sacrifice his gluttonous desires."
    j "He wants to gratify his taste for rich and unnatural viands and have his health as well."
    j "Such a man is totally unfit to have health, because he has not yet learned the first principles of a healthy life."

    hide richman wretched
    show employer wretched

    j "Here is an employer of labour who adopts crooked measures to avoid paying the regulation wage, and, in the hope of making larger profits, reduces the wages of his workpeople."
    j "Such a man is altogether unfitted for prosperity, and when he finds himself bankrupt, both as regards reputation and riches,"
    j "he blames circumstances, not knowing that he is the sole author of his condition."

    hide employer wretched
    with dissolve

    j "I have introduced these three cases merely as illustrative of the truth that man is the causer (though nearly always is unconsciously) of his circumstances,"
    j "and that, whilst aiming at a good end, he is continually frustrating its accomplishment"
    j "by encouraging thoughts and desires which cannot possibly harmonize with that end."
    j "Such cases could be multiplied and varied almost indefinitely,"
    j "but this is not necessary, as the reader can, if he so resolves, trace the action of the laws of thought in his own mind and life,"
    j "and until this is done, mere external facts cannot serve as a ground of reasoning."
    j "Circumstances, however, are so complicated, thought is so deeply rooted,"
    j "and the conditions of happiness vary so, vastly with individuals,"
    j "that a man's entire soul-condition (although it may be known to himself) cannot be judged by another from the external aspect of his life alone."
    j "A man may be honest in certain directions, yet suffer privations;"
    j "a man may be dishonest in certain directions, yet acquire wealth;"
    j "but the conclusion usually formed that the one man fails because of his particular honesty, and that the other prospers because of his particular dishonesty,"
    j "is the result of a superficial judgment,"
    j "which assumes that the dishonest man is almost totally corrupt,"
    j "and the honest man almost entirely virtuous."
    j "In the light of a deeper knowledge and wider experience such judgment is found to be erroneous."
    j "The dishonest man may have some admirable virtues, which the other does not possess;"
    j "and the honest man obnoxious vices which are absent in the other."
    j "The honest man reaps the good results of his honest thoughts and acts; he also brings upon himself the sufferings, which his vices produce."
    j "The dishonest man likewise garners his own suffering and happiness."
    j "It is pleasing to human vanity to believe that one suffers because of one's virtue;"
    j "but not until a man has extirpated every sickly, bitter, and impure thought from his mind, and washed every sinful stain from his soul,"
    j "can he be in a position to know and declare that his sufferings are the result of his good, and not of his bad qualities;"
    j "and on the way to, yet long before he has reached, that supreme perfection,"
    j "he will have found, working in his mind and life, the Great Law which is absolutely just,"
    j "and which cannot, therefore, give good for evil, evil for good."
    j "Possessed of such knowledge, he will then know, looking back upon his past ignorance and blindness, that his life is, and always was, justly ordered,"
    j "and that all his past experiences, good and bad, were the equitable outworking of his evolving, yet unevolved self."
    j "Good thoughts and actions can never produce bad results; bad thoughts and actions can never produce good results."
    j "This is but saying that nothing can come from corn but corn, nothing from nettles but nettles."
    j "Men understand this law in the natural world, and work with it; but few understand it in the mental and moral world"
    j "--though its operation there is just as simple and undeviating--"
    j "and they, therefore, do not co-operate with it."
    j "Suffering is always the effect of wrong thought in some direction."
    j "It is an indication that the individual is out of harmony with himself, with the Law of his being."
    j "The sole and supreme use of suffering is to purify, to burn out all that is useless and impure."
    j "Suffering ceases for him who is pure."
    j "There could be no object in burning gold after the dross had been removed, and a perfectly pure and enlightened being could not suffer."
    j "The circumstances, which a man encounters with suffering, are the result of his own mental inharmony."
    j "The circumstances, which a man encounters with blessedness, are the result of his own mental harmony."
    j "Blessedness, not material possessions, is the measure of right thought;"
    j "wretchedness, not lack of material possessions, is the measure of wrong thought."
    j "A man may be cursed and rich; he may be blessed and poor."
    j "Blessedness and riches are only joined together when the riches are rightly and wisely used; and the poor man only descends into wretchedness when he regards his lot as a burden unjustly imposed."
    j "Indigence and indulgence are the two extremes of wretchedness. They are both equally unnatural and the result of mental disorder."
    j "A man is not rightly conditioned until he is a happy, healthy, and prosperous being;"
    j "and happiness, health, and prosperity are the result of a harmonious adjustment of the inner with the outer, of the man with his surroundings."
    j "A man only begins to be a man when he ceases to whine and revile, and commences to search for the hidden justice which regulates his life."
    j "And as he adapts his mind to that regulating factor, he ceases to accuse others as the cause of his condition, and builds himself up in strong and noble thoughts;"
    j "ceases to kick against circumstances, but begins to use them as aids to his more rapid progress, and as a means of discovering the hidden powers and possibilities within himself."
    j "Law, not confusion, is the dominating principle in the universe;"
    j "justice, not injustice, is the soul and substance of life;"
    j "and righteousness, not corruption, is the moulding and moving force in the spiritual government of the world."
    j "This being so, man has but to right himself to find that the universe is right;"
    j "and during the process of putting himself right he will find that as he alters his thoughts towards things and other people, things and other people will alter towards him."
    j "The proof of this truth is in every person, and it therefore admits of easy investigation by systematic introspection and self-analysis."
    j "Let a man radically alter his thoughts, and he will be astonished at the rapid transformation it will effect in the material conditions of his life."
    j "Men imagine that thought can be kept secret, but it cannot; it rapidly crystallizes into habit, and habit solidifies into circumstance."
    j "Bestial thoughts crystallize into habits of drunkenness and sensuality, which solidify into circumstances of destitution and disease:"
    j "impure thoughts of every kind crystallize into enervating and confusing habits, which solidify into distracting and adverse circumstances:"
    j "thoughts of fear, doubt, and indecision crystallize into weak, unmanly, and irresolute habits, which solidify into circumstances of failure, indigence, and slavish dependence:"
    j "lazy thoughts crystallize into habits of uncleanliness and dishonesty, which solidify into circumstances of foulness and beggary:"
    j "hateful and condemnatory thoughts crystallize into habits of accusation and violence, which solidify into circumstances of injury and persecution:"
    j "selfish thoughts of all kinds crystallize into habits of self-seeking, which solidify into circumstances more or less distressing."
    j "On the other hand, beautiful thoughts of all kinds crystallize into habits of grace and kindliness, which solidify into genial and sunny circumstances:"
    j "pure thoughts crystallize into habits of temperance and self-control, which solidify into circumstances of repose and peace:"
    j "thoughts of courage, self-reliance, and decision crystallize into manly habits, which solidify into circumstances of success, plenty, and freedom:"
    j "energetic thoughts crystallize into habits of cleanliness and industry, which solidify into circumstances of pleasantness:"
    j "gentle and forgiving thoughts crystallize into habits of gentleness, which solidify into protective and preservative circumstances:"
    j "loving and unselfish thoughts crystallize into habits of self-forgetfulness for others, which solidify into circumstances of sure and abiding prosperity and true riches."
    j "A particular train of thought persisted in, be it good or bad, cannot fail to produce its results on the character and circumstances."
    j "A man cannot directly choose his circumstances, but he can choose his thoughts, and so indirectly, yet surely, shape his circumstances."
    j "Nature helps every man to the gratification of the thoughts, which he most encourages, and opportunities are presented which will most speedily bring to the surface both the good and evil thoughts."
    j "Let a man cease from his sinful thoughts, and all the world will soften towards him, and be ready to help him;"
    j "let him put away his weakly and sickly thoughts, and lo, opportunities will spring up on every hand to aid his strong resolves;"
    j "let him encourage good thoughts, and no hard fate shall bind him down to wretchedness and shame."
    j "The world is your kaleidoscope, and the varying combinations of colours, which at every succeeding moment it presents to you are the exquisitely adjusted pictures of your ever-moving thoughts."

    show poet standing

    "The Poet" "So You will be what you will to be;"
    "The Poet" "Let failure find its false content"
    "The Poet" "In that poor word, 'environment,'"
    "The Poet" "But spirit scorns it, and is free."
    "The Poet" "It masters time, it conquers space;"
    "The Poet" "It cowes that boastful trickster, Chance,"
    "The Poet" "And bids the tyrant Circumstance"
    "The Poet" "Uncrown, and fill a servant's place."
    "The Poet" "The human Will, that force unseen,"
    "The Poet" "The offspring of a deathless Soul,"
    "The Poet" "Can hew a way to any goal,"
    "The Poet" "Though walls of granite intervene."
    "The Poet" "Be not impatient in delays"
    "The Poet" "But wait as one who understands;"
    "The Poet" "When spirit rises and commands"
    "The Poet" "The gods are ready to obey."

    hide poet standing

    j "Let us now speak of the effects of thought on your health and your body."
    j "Would you agree that the body is the servant of the mind?"
    u "I'm not sure..."
    j "The body is the servant of the mind."
    u "Why did you even ask me if my opinion didn't matter to you?"
    j "I share the wisdom I possess. You may discard what you wish to discard."
    j "It is of no import to me."
    j "The body obeys the operations of the mind, whether they be deliberately chosen or automatically expressed."
    j "At the bidding of unlawful thoughts the body sinks rapidly into disease and decay; at the command of glad and beautiful thoughts it becomes clothed with youthfulness and beauty."
    j "Disease and health, like circumstances, are rooted in thought."
    j "Sickly thoughts will express themselves through a sickly body."
    j "Thoughts of fear have been known to kill a man as speedily as a bullet, and they are continually killing thousands of people just as surely though less rapidly."
    j "The people who live in fear of disease are the people who get it."
    j "Anxiety quickly demoralizes the whole body, and lays it open to the entrance of disease;"
    j "while impure thoughts, even if not physically indulged, will soon shatter the nervous system."
    "I can't have... you know... desire?"
    j "You do what you wish. What you have the will for."
    j "Strong, pure, and happy thoughts build up the body in vigour and grace."
    j "The body is a delicate and plastic instrument, which responds readily to the thoughts by which it is impressed, and habits of thought will produce their own effects, good or bad, upon it."
    j "Men will continue to have impure and poisoned blood, so long as they propagate unclean thoughts."
    j "Out of a clean heart comes a clean life and a clean body. Out of a defiled mind proceeds a defiled life and a corrupt body."
    j "Thought is the fount of action, life, and manifestation; make the fountain pure, and all will be pure."
    u "This all kind of reminds me of that Christian woman with the big hair who had that faith-based diet group."
    j "I know not of whom you speak."
    u "Gwen... something."
    j "I am not suggesting you subsist upon raw berries and roughage that you forage in the woods."
    u "I think that church group was more about sugar-free pudding and Cool-Whip and fat-free vanilla lattes. Maybe they did eat some actual food for dinner. Like, steamed broccoli or something."
    j "Talk of food is of scant interest to me."
    u "Well, I used to be a food reviewer at the Boston Gazette back when you could still make a living off that, so--"
    j "Sure. What a surfeit of highly useful information you have for me. In any case, and to get back to what I was attempting to communicate:"
    j "--a change of diet will not help a man who will not change his thoughts."
    j "If the diet of Gwen Something significantly changed, it was her thoughts that changed first." 
    j "When a man--or woman--makes his thoughts pure, he no longer desires impure food."
    j "Clean thoughts make clean habits."
    u "Cleanliness is next to Godliness?"
    j "Indeed."
    j "The so-called saint who does not wash his body is not a saint."
    j "He who has strengthened and purified his thoughts does not need to consider the malevolent microbe."
    j "If you would protect your body, guard your mind. If you would renew your body, beautify your mind."
    j "Thoughts of malice, envy, disappointment, despondency, rob the body of its health and grace."
    j "A sour face does not come by chance; it is made by sour thoughts. Wrinkles that mar are drawn by folly, passion, and pride."
    u "So... don't make ugly faces in case your face gets stuck that way?"
    j "I know a woman of ninety-six who has the bright, innocent face of a girl."
    j "I know a man well under middle age whose face is drawn into inharmonious contours."
    j "The one is the result of a sweet and sunny disposition; the other is the outcome of passion and discontent."
    j "As you cannot have a sweet and wholesome abode unless you admit the air and sunshine freely into your rooms,"
    j "so a strong body and a bright, happy, or serene countenance can only result from the free admittance into the mind of thoughts of joy and goodwill and serenity."
    j "On the faces of the aged there are wrinkles made by sympathy, others by strong and pure thought, and others are carved by passion: who cannot distinguish them?"
    j "With those who have lived righteously, age is calm, peaceful, and softly mellowed, like the setting sun."
    j "I have recently seen a philosopher on his deathbed. He was not old except in years. He died as sweetly and peacefully as he had lived."
    j "There is no physician like cheerful thought for dissipating the ills of the body;"
    j "there is no comforter to compare with goodwill for dispersing the shadows of grief and sorrow."
    j "To live continually in thoughts of ill will, cynicism, suspicion, and envy, is to be confined in a self made prison-hole."
    j "But to think well of all, to be cheerful with all, to patiently learn to find the good in all—such unselfish thoughts are the very portals of heaven;"
    j "and to dwell day by day in thoughts of peace toward every creature will bring abounding peace to their possessor."
    "I couldn't agree with you more."
    j "I do not require your approval, but I thank you for your kind words."
    "I may not always agree with you, but I am listening."
    j "Indeed you are. Let us now speak of Thought and Purpose."
    j "Until thought is linked with purpose there is no intelligent accomplishment."
    j "With the majority the bark of thought is allowed to 'drift' upon the ocean of life."
    j "Aimlessness is a vice, and such drifting must not continue for him who would steer clear of catastrophe and destruction."
    "I'm actually really worried that my life lacks purpose and meaning."
    j "They who have no central purpose in their life fall an easy prey to petty worries, fears, troubles, and self-pityings, all of which are indications of weakness,"
    j "which lead, just as surely as deliberately planned sins (though by a different route), to failure, unhappiness, and loss,"
    j "for weakness cannot persist in a power evolving universe."
    j "A man should conceive of a legitimate purpose in his heart, and set out to accomplish it."
    j "He should make this purpose the centralizing point of his thoughts."
    "How do I figure out what my purpose is?"
    j "It may take the form of a spiritual ideal, or it may be a worldly object, according to your nature at the time being."
    j "Whichever it is, you should steadily focus your thought-forces upon the object which you has set before you."
    j "You should make this purpose your supreme duty, and should devote yourself to its attainment, not allowing your thoughts to wander away into ephemeral fancies, longings, and imaginings."
    j "This is the royal road to self-control and true concentration of thought."
    j "Even if you fail again and again to accomplish your purpose (as you necessarily must until weakness is overcome),"
    j "the strength of character gained will be the measure of your true success, and this will form a new starting-point for future power and triumph."
    "Aren't there some people who never figure it out? You know, never know what the purpose of our life should be?"
    j "You fear you are one who is not prepared for the apprehension of a great purpose?"
    "Yeah. I do."
    j "In this case: you should fix your thoughts upon the faultless performance of your duty, no matter how insignificant your tasks may appear."
    j "Only in this way can the thoughts in your head be gathered and focussed, and resolution and energy be developed, which being done, there is nothing which may not be accomplished."
    j "The weakest soul, knowing its own weakness, and believing this truth that strength can only be developed by effort and practice, will, thus believing, at once begin to exert itself,"
    j "and, adding effort to effort, patience to patience, and strength to strength, will never cease to develop, and will at last grow divinely strong."
    j "As the physically weak man can make himself strong by careful and patient training, so the man of weak thoughts can make them strong by exercising himself in right thinking."
    "Right thinking... I'm pretty sure I read about that in a John Kabat-Zinn book."
    j "You appear to very much enjoy making reference to people with whom I have no familiarity."
    "He's pretty famous."
    j "In whose time?"
    "I mean, right now."
    j "But I am not of your time."
    "Wait, what?"
    j "I am of my own time. It is before yours. Allow me to continue. If you lack purpose and duty too, you must put away aimlessness and weakness."
    j "You must begin to think with purpose, to enter the ranks of those strong ones who only recognize failure as one of the pathways to attainment;"
    j "to enter the ranks of those who make all conditions serve them, and who think strongly, attempt fearlessly, and accomplish masterfully."
    j "Having conceived of his purpose, a man should mentally mark out a straight pathway to its achievement, looking neither to the right nor the left."
    j "Doubts and fears should be rigorously excluded; they are disintegrating elements, which break up the straight line of effort, rendering it crooked, ineffectual, useless."
    j "Thoughts of doubt and fear never accomplished anything, and never can."
    j "They always lead to failure."
    j "Purpose, energy, power to do, and all strong thoughts cease when doubt and fear creep in."
    "Fear is the mind-killer."
    j "Well-put."
    "I stole that from Dune."
    j "..."
    "Sorry."
    j "..."
    "Well. I do like the line, though. And I agree with it."
    j "Tell me... do you feel that you are capable of a great many things?"
    "Some days, yeah. Other days..."
    j "I understand."
    j "The will to do springs from the knowledge that we can do."
    j "Doubt and fear are the great enemies of knowledge, and he who encourages them, who does not slay them, thwarts himself at every step."
    j "He who has conquered doubt and fear has conquered failure. His every thought is allied with power, and all difficulties are bravely met and wisely overcome."
    j "His purposes are seasonably planted, and they bloom and bring forth fruit, which does not fall prematurely to the ground."
    j "Thought allied fearlessly to purpose becomes creative force:"
    j "he who knows this is ready to become something higher and stronger than a mere bundle of wavering thoughts and fluctuating sensations;"
    j "he who does this has become the conscious and intelligent wielder of his mental powers."
    j "With achievement, there is a thought-factor to consider."
    j "All that a man achieves and all that he fails to achieve is the direct result of his own thoughts."
    j "In a justly ordered universe, where loss of equipoise would mean total destruction, individual responsibility must be absolute."
    j "A man's weakness and strength, purity and impurity, are his own, and not another man's;"
    j "they are brought about by himself, and not by another; and they can only be altered by himself, never by another."
    j "His condition is also his own, and not another man's. His suffering and his happiness are evolved from within."
    j "As he thinks, so he is; as he continues to think, so he remains."
    j "A strong man cannot help a weaker unless that weaker is willing to be helped, and even then the weak man must become strong of himself;"
    j "he must, by his own efforts, develop the strength which he admires in another."
    j "None but himself can alter his condition."
    j "It has been usual for men to think and to say, 'Many men are slaves because one is an oppressor; let us hate the oppressor.'"
    j "Now, however, there is amongst an increasing few a tendency to reverse this judgment, and to say, 'One man is an oppressor because many are slaves; let us despise the slaves.'"
    j "The truth is that oppressor and slave are co-operators in ignorance, and, while seeming to afflict each other, are in reality afflicting themselves."
    j "A perfect Knowledge perceives the action of law in the weakness of the oppressed and the misapplied power of the oppressor;"
    j "a perfect Love, seeing the suffering, which both states entail, condemns neither;"
    j "a perfect Compassion embraces both oppressor and oppressed."
    j "He who has conquered weakness, and has put away all selfish thoughts, belongs neither to oppressor nor oppressed."
    j "He is free."
    "I'm not sure that I can feel love or compassion for people who kill and maim and oppress."
    j "A man can only rise, conquer, and achieve by lifting up his thoughts. He can only remain weak, and abject, and miserable by refusing to lift up his thoughts."
    "You're saying that I have to find a way to love people who commit genocide or drop napalm on little kids?"
    j "Man does it for the people suffering the genocide, the children who are set afire. It is necessary."
    j "Before a man can achieve anything, even in worldly things, he must lift his thoughts above slavish animal indulgence."
    j "He may not, in order to succeed, give up all animality and selfishness, by any means; but a portion of it must, at least, be sacrificed."
    j "A man whose first thought is bestial indulgence could neither think clearly nor plan methodically; he could not find and develop his latent resources, and would fail in any undertaking."
    j "Not having commenced to manfully control his thoughts, he is not in a position to control affairs and to adopt serious responsibilities."
    j "He is not fit to act independently and stand alone."
    j "But he is limited only by the thoughts, which he chooses."
    j "There can be no progress, no achievement without sacrifice,"
    j "and a man's worldly success will be in the measure that he sacrifices his confused animal thoughts, and fixes his mind on the development of his plans, and the strengthening of his resolution and self-reliance."
    j "And the higher he lifts his thoughts, the more manly, upright, and righteous he becomes, the greater will be his success, the more blessed and enduring will be his achievements."
    "But the most successful people in the world aren't like that. Elon Musk isn't like that. Jeff Bezos isn't like that. Hell, even Bill Gates was known to very close friends with a certain Jeffrey--"
    j "Yes, this must be addressed. I do not know of whom you speak, exactly, but in my time I believe we had our equivalents, and I understand the point you are making."
    j "The universe does not favour the greedy, the dishonest, the vicious, although on the mere surface it may sometimes appear to do so;"
    j "it helps the honest, the magnanimous, the virtuous."
    j "All the great Teachers of the ages have declared this in varying forms, and to prove and know it a man has but to persist in making himself more and more virtuous by lifting up his thoughts."
    "I'm just not sure I believe that."
    j "Do the men you have mentioned seem content with their achievements"
    "Oh, no, definitely not."
    j "Then the universe does not favor them."
    "Oh! Okay. I see."
    j "Now think of an achievement of your own."
    "Okay. Hm..."
    "..."
    "Okay. I've got a few, actually."
    j "Very good."
    "And there's one more!"
    j "[chuckles]"
    "Made you laugh!"
    j "It is not very difficult to make me laugh. But it can be one of your achievements."
    j "Intellectual achievements are the result of thought consecrated to the search for knowledge, or for the beautiful and true in life and nature."
    j "Such achievements may be sometimes connected with vanity and ambition, but they are not the outcome of those characteristics;"
    j "they are the natural outgrowth of long and arduous effort, and of pure and unselfish thoughts."
    j "Spiritual achievements are the consummation of holy aspirations."
    j "He who lives constantly in the conception of noble and lofty thoughts, who dwells upon all that is pure and unselfish, will,"
    j "as surely as the sun reaches its zenith and the moon its full,"
    j "become wise and noble in character, and rise into a position of influence and blessedness."
    j "Achievement, of whatever kind, is the crown of effort, the diadem of thought."
    j "By the aid of self-control, resolution, purity, righteousness, and well-directed thought a man ascends;"
    j "by the aid of animality, indolence, impurity, corruption, and confusion of thought a man descends."
    j "A man may rise to high success in the world, and even to lofty altitudes in the spiritual realm,"
    j "and again descend into weakness and wretchedness by allowing arrogant, selfish, and corrupt thoughts to take possession of him."
    j "Victories attained by right thought can only be maintained by watchfulness. Many give way when success is assured, and rapidly fall back into failure."
    j "All achievements, whether in the business, intellectual, or spiritual world, are the result of definitely directed thought,"
    j "are governed by the same law and are of the same method; the only difference lies in the object of attainment."
    j "He who would accomplish little must sacrifice little;"
    j "he who would achieve much must sacrifice much;"
    j "he who would attain highly must sacrifice greatly."
    j "Do you have ideals?"
    "Yeah. Values, ideals, I do. I'd say I do. Maybe I'm a little bit of a dreamer, though. I'm not always realistic."
    j "This is a good thing. The dreamers are the saviours of the world."
    j "As the visible world is sustained by the invisible, so men, through all their trials and sins and sordid vocations, are nourished by the beautiful visions of their solitary dreamers."
    j "Humanity cannot forget its dreamers;"
    j "it cannot let their ideals fade and die;"
    j "it lives in them; it knows them as the realities which it shall one day see and know."
    j "Composer, sculptor, painter, poet, prophet, sage, these are the makers of the after-world, the architects of heaven. The world is beautiful because they have lived; without them, labouring humanity would perish."
    j "He who cherishes a beautiful vision, a lofty ideal in his heart, will one day realize it."
    j "Columbus cherished a vision of another world, and he discovered it;"
    label choices999:
        u "Well, not exactly--"
        u "He sure did!"
    j "Copernicus fostered the vision of a multiplicity of worlds and a wider universe, and he revealed it;"
    j "Buddha beheld the vision of a spiritual world of stainless beauty and perfect peace, and he entered into it."
    j "Cherish your visions."
    j "Cherish your ideals."
    j "Cherish the music that stirs in your heart, the beauty that forms in your mind, the loveliness that drapes your purest thoughts,"
    j "for out of them will grow all delightful conditions, all, heavenly environment; of these, if you but remain true to them, your world will at last be built."
    j "To desire is to obtain; to aspire is to achieve."
    j "Shall man's basest desires receive the fullest measure of gratification, and his purest aspirations starve for lack of sustenance?"
    j "Such is not the Law: such a condition of things can never obtain: 'ask and receive.'"
    j "Dream lofty dreams!"
    j "As you dream, so shall you become."
    j "Your Vision is the promise of what you shall one day be; your Ideal is the prophecy of what you shall at last unveil."
    j "The greatest achievement was at first and for a time a dream."
    j "The oak sleeps in the acorn;"
    j "the bird waits in the egg;"
    j "and in the highest vision of the soul a waking angel stirs."
    j "Dreams are the seedlings of realities."
    j "Your circumstances may be uncongenial, but they shall not long remain so if you but perceive an Ideal and strive to reach it. You cannot travel within and stand still without."
    j "Here is a youth hard pressed by poverty and labour; confined long hours in an unhealthy workshop; unschooled, and lacking all the arts of refinement."
    j "But he dreams of better things; he thinks of intelligence, of refinement, of grace and beauty."
    j "He conceives of, mentally builds up, an ideal condition of life;"
    j "the vision of a wider liberty and a larger scope takes possession of him;"
    j "unrest urges him to action,"
    j "and he utilizes all his spare time and means, small though they are, to the development of his latent powers and resources."
    j "Very soon so altered has his mind become that the workshop can no longer hold him."
    j "It has become so out of harmony with his mentality that it falls out of his life as a garment is cast aside,"
    j "and, with the growth of opportunities, which fit the scope of his expanding powers, he passes out of it forever."
    j "Years later we see this youth as a full-grown man."
    j "We find him a master of certain forces of the mind, which he wields with worldwide influence and almost unequalled power."
    j "In his hands he holds the cords of gigantic responsibilities;"
    j "he speaks, and lo, lives are changed; men and women hang upon his words and remould their characters, and, sunlike, he becomes the fixed and luminous centre round which innumerable destinies revolve."
    j "He has realized the Vision of his youth. He has become one with his Ideal."
    j "And you, too, will realize the Vision (not the idle wish) of your heart, be it base or beautiful, or a mixture of both,"
    j "for you will always gravitate toward that which you, secretly, most love."
    j "Into your hands will be placed the exact results of your own thoughts; you will receive that which you earn; no more, no less."
    j "Whatever your present environment may be, you will fall, remain, or rise with your thoughts, your Vision, your Ideal."
    j "You will become as small as your controlling desire; as great as your dominant aspiration."
    j "in the beautiful words of Stanton Kirkham Davis:"

    show Davis happy

    "Stanton Kirkham Davis" "You may be keeping accounts,"
    "Stanton Kirkham Davis" "and presently you shall walk out of the door that for so long has seemed to you the barrier of your ideals,"
    "Stanton Kirkham Davis" "and shall find yourself before an audience—the pen still behind your ear, the ink stains on your fingers and then and there shall pour out the torrent of your inspiration."
    "Stanton Kirkham Davis" "You may be driving sheep, and you shall wander to the city-bucolic and open-mouthed;"
    "Stanton Kirkham Davis" "shall wander under the intrepid guidance of the spirit into the studio of the master, and after a time he shall say, 'I have nothing more to teach you.'"
    "Stanton Kirkham Davis" "And now you have become the master, who did so recently dream of great things while driving sheep."
    "Stanton Kirkham Davis" "You shall lay down the saw and the plane to take upon yourself the regeneration of the world."

label flags:
    if knowsaboutjameslife:
        u "Is... was he a friend of yours?"
        j "We briefly met whilst he was traveling around the British Isles. I admired his work very much."
        u "Were you jealous of him?"
        j "The man who thinks is my colleague. He is not my competitor. A competition is a game of chance."
    else:
        u "That was beautiful."
        j "Indeed. He was a talent."
        u "He died?"
        j "Oh, yes. Quite some time ago."
        u "That's unlucky. I'm sorry to hear it."

    j "It is the thoughtless, the ignorant, and the indolent, seeing only the apparent effects of things and not the things themselves, talk of luck, of fortune, and chance."
    j "Seeing a man grow rich, they say, 'How lucky he is!'"
    j "Observing another become intellectual, they exclaim, 'How highly favoured he is!'"
    j "And noting the saintly character and wide influence of another, they remark, 'How chance aids him at every turn!'"
    j "They do not see the trials and failures and struggles which these men have voluntarily encountered in order to gain their experience;"
    j "have no knowledge of the sacrifices they have made, of the undaunted efforts they have put forth, of the faith they have exercised,"
    j "that they might overcome the apparently insurmountable, and realize the Vision of their heart."
    j "They do not know the darkness and the heartaches;"
    j "they only see the light and joy, and call it 'luck'."
    j "They do not see the long and arduous journey, but only behold the pleasant goal, and call it 'good fortune,'"
    j "do not understand the process, but only perceive the result, and call it chance."
    j "In all human affairs there are efforts, and there are results, and the strength of the effort is the measure of the result."
    j "Chance is not."
    j "Gifts, powers, material, intellectual, and spiritual possessions are the fruits of effort; they are thoughts completed, objects accomplished, visions realized."
    j "The Vision that you glorify in your mind, the Ideal that you enthrone in your heart—this you will build your life by, this you will become."
    j "Those men you mentioned--Neelon Musk and Jeff Bayesian, was it?--are they serene?"
    "Oh, definitely not."
    j "Indeed. I knew this would be the answer. You see, calmness of mind is one of the beautiful jewels of wisdom."
    j "It is the result of long and patient effort in self-control. Its presence is an indication of ripened experience, and of a more than ordinary knowledge of the laws and operations of thought."
    j "A man becomes calm in the measure that he understands himself as a thought evolved being, for such knowledge necessitates the understanding of others as the result of thought,"
    j "and as he develops a right understanding, and sees more and more clearly the internal relations of things by the action of cause and effect,"
    j "he ceases to fuss and fume and worry and grieve, and remains poised, steadfast, serene."
    j "The calm man, having learned how to govern himself, knows how to adapt himself to others; and they, in turn, reverence his spiritual strength, and feel that they can learn of him and rely upon him."
    j "The more tranquil a man becomes, the greater is his success, his influence, his power for good."
    j "Even the ordinary trader will find his business prosperity increase as he develops a greater self-control and equanimity, for people will always prefer to deal with a man whose demeanour is strongly equable."
    j "The strong, calm man is always loved and revered."
    j "He is like a shade-giving tree in a thirsty land, or a sheltering rock in a storm."
    j "Who does not love a tranquil heart, a sweet-tempered, balanced life?"
    j "It does not matter whether it rains or shines, or what changes come to those possessing these blessings, for they are always sweet, serene, and calm."
    j "That exquisite poise of character, which we call serenity, is the last lesson of culture, the fruitage of the soul."
    j "It is precious as wisdom, more to be desired than gold—yea, than even fine gold."
    j "How insignificant mere money seeking looks in comparison with a serene life—a life that dwells in the ocean of Truth, beneath the waves, beyond the reach of tempests, in the Eternal Calm!"
    j "How many people we know who sour their lives, who ruin all that is sweet and beautiful by explosive tempers, who destroy their poise of character, and make bad blood!"
    j "It is a question whether the great majority of people do not ruin their lives and mar their happiness by lack of self-control."
    j "How very few people we meet in life who are well balanced, who have that exquisite poise which is characteristic of the finished character!"
    j "Yes, humanity surges with uncontrolled passion, is tumultuous with ungoverned grief, is blown about by anxiety and doubt"
    j "only the wise man, only he whose thoughts are controlled and purified, makes the winds and the storms of the soul obey him."
    j "Tempest-tossed souls, wherever ye may be, under whatsoever conditions ye may live, know this:"
    j "in the ocean of life the isles of Blessedness are smiling, and the sunny shore of your ideal awaits your coming. Keep your hand firmly upon the helm of thought."
    j "In the bark of your soul reclines the commanding Master; He does but sleep: wake Him."
    j "Self-control is strength;"
    j "Right Thought is mastery;"
    j "Calmness is power."
    j "Say unto your heart, 'Peace, be still!'"
    j "Say it!" with vpunch
    "Peace, be still."
    j "Peace, be still."
    "Peace, be still."
    j "Peace."
    "Be still."



    # This ends the game.

    return
