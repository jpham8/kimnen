label chapter1:

    scene apartment with dissolve

    m "Everyone got everything packed? You guys better use the bathroom too, or I’m going to kick you out of the car."
    patrick "Yup. Did all of that."
    danM "Yeah, let’s go."
    m "Alright. Let me call my parents to tell them I’m on the way back."
    "I do this every long car ride because my parents seem to worry a bit much."

    play sound "sfx/dial_tone.mp3"
    pause 2.3
    mom "Hi Johnny."
    m "Hi Mommy. I’m leaving now."
    mom "Good. What time will you be back?"
    m "Um, I think around eight. I need to drop off two friends first."
    mom "Ok. Drive back safe!"
    m "Yup, bye Mommy."
    mom "Bye!"
    play sound "sfx/hangup.mp3"
    pause 0.5

    m "Alright. Let’s load the car and head out."
    play sound "sfx/car_door1.mp3"
    scene car uofi with wipeleft
    "Just like the other times I’ve driven back to the Chicago suburbs, I play through video game soundtracks while talking about random things with my friends."
    scene car midway1 with dissolve
    pause 1.5
    scene car midway2 with dissolve
    "Corn fields slowly transform into buildings and highway lanes as we get closer to the city."
    scene patrick_house with dissolve
    m "See you on campus in two weeks!"
    patrick "Yeah. Thanks for the ride."

    scene car midway3 with dissolve
    pause 1.5
    scene dan_house with wiperight
    danM "Thanks for the ride."
    m "No problem. Venmo me whenever."
    danM "Sure. I can just do it when you drive me back to campus."
    m "Aight. See ya."

    scene car_suburb_night with wiperight
    stop music fadeout 1.0
    pause 1.0
    scene front door night with dissolve
    play music ["music/Home.mp3", "music/normal.mp3"] fadeout 1.5 fadein 1.5
    "I get into the driveway and ring the doorbell. My dad answers the door."
    dad "Hi Johnny. Is that all of your bags?"
    m "I think I have one more. Let me get it from the car."
    scene dining room night with irisout
    "I get my last backpack and head into the house. I see my mom to the left in the kitchen."
    mom "Hi Johnny! I’ve missed you!"
    "We both hug and kiss each other on the cheek."
    m "Hi Mommy. I’m pretty tired, so I’m going to bring my bags up to my room and rest for a bit."
    mom "Ok, dinner will be ready soon!"
    m "Alright, thanks."
    scene main_stairs_up with dissolve
    play sound "sfx/stair_up.mp3"
    pause 1.4
    scene my room house night with dissolve
    "I head up to my room and leave my stuff on the floor. I unpack my laptop first thing."
    mom "Johnny! Dinner’s ready!"
    m "Ok!"
    scene main_stairs_down with wipeleft
    play sound "sfx/stair_down.mp3"
    pause 1.4

    scene dining room table with dissolve
    "I head down and help set up the table. The three of us sit around the end of it. My brother and sister moved out awhile ago, so it’s rarely full."
    m "What did you make Mommy?"
    mom "Bánh hỏi with pork."
    m "Yay!"
    show banh_hoi at center_above with dissolve
    "One of my favorite Vietnamese dishes. I didn’t eat any Vietnamese food while at school due to laziness and difficulty."
    hide banh_hoi with dissolve
    dad "Johnny, can you get me a cup of tea too?"
    m "Sure."
    "The meal passes by with idle chatter and the TV playing in the background. I happily finish my plate and cup of milk. The conversation shifts to my summer internship."
    m "Oh yeah. Here’s pictures of my trip to the John Deere headquarters."
    show johndeere1 at center_above with dissolve
    mom "Wow! The building looks so pretty. "
    m "Yeah. It was pretty interesting how much nature they had inside the offices."
    hide johndeere1
    show johndeere2 at center_above with dissolve
    mom "Wow!"
    hide johndeere2 with dissolve
    m "Alright. Should I put my dishes in the sink?"
    mom "Yeah. Don't forget to rinse them too."
    m "Ok."
    scene kitchen with dissolve
    play sound "sfx/faucet.mp3"
    pause 1.8
    m "Thanks for dinner Mommy!"
    mom "No problem. Johnny do you want tea?"
    m "Sure!"
    "Tea from home is always the best. My mom usually makes jasmine tea after dinner."
    mom "Ok. I'll tell you to come down when it's ready."
    "I kiss her quickly on the cheek and head upstairs. My dad goes to his usual recliner."
    scene main_stairs_up with dissolve
    play sound "sfx/stair_up.mp3"
    pause 1.4

    scene my room house night with dissolve
    "I launch my usual websites and the group chat I have with my friends."
    "Video games are a major time sink for my friend group. Dota is the current game we've been playing together."
    "After a few moments, we start up a voice call."
    play sound "sfx/discord_user_join.mp3"
    pause 0.3
    kevin "Hi!"
    will "Hi!"
    m "Yo guys."
    scene dota_start with dissolve
    "We launch Dota 2 and queue up for a game. Just when it's about to start..."
    scene my room house night with vpunch
    mom "Johnny! Tea is ready!"
    m "Ok! Coming! One sec guys."
    scene second_floor with wipeleft
    play sound "sfx/stair_down.mp3"
    pause 0.25
    scene main_stairs_down with dissolve
    m "Thanks mommy!"
    mom "Careful, it's hot."
    m "Ok!"
    play sound "sfx/stair_up.mp3"
    scene my room house night with wiperight
    pause 0.1
    scene dota_start with dissolve
    m "Alright I’m back. Everyone ready?"
    will "Yup."

    scene black with dissolve
    play sound "sfx/dota.mp3"
    "A fierce battle rages on as both of our teams fight in a virtual arena. Eventually..."
    scene dota_end with dissolve
    m "Good game of Dota guys!"
    patrick "It was easyyy."
    kevin "Easyyyy."
    m "I'm gonna go to sleep now. Night guys."
    will "Good night."
    patrick "Night."
    play sound "sfx/discord_user_leave.mp3"
    scene my room house night with dissolve
    pause 1
    play sound "sfx/lightswitch.mp3"
    scene black with dissolve
    pause 2
    #Maybe new song here

    scene my room house with dissolve
    "August 9, Tuesday"
    dad "Hey Johnny. Can you help me get groceries from Costco?"
    m "Sure. Let me change."
    scene costco with dissolve
    dad "Has your mom mentioned anything about her stomach pains to you?"
    m "No? I don't think so."
    dad "I've been trying to tell her to go to the doctor, but she won't listen. Can you convince her to go with you?"
    m "I guess. Is it that big of an issue?"
    dad "She's been complaining about it for a week now. She works too much and doesn't sleep enough too."
    dad "She spends too much time and effort for her company. I make enough money to let her work less, but she won't listen."
    m "I guess. I’ll ask her about it when we get back."
    dad "Thanks Johnny."
    dad "Oh yeah. I need your help with putting up curtains and cutting the grass."
    m "Ok."
    mt "Ugh this is such a pain. I wanted to work on my bus app too…"

    scene my room house day with blinds
    m "Guess I should talk to mommy about the doctor's."
    scene main_stairs_down with dissolve
    play sound "sfx/stair_down.mp3"
    pause 1.4
    scene basement_stairs with dissolve
    play sound "sfx/basement_down.mp3"
    pause 1.4
    scene basement with wipeleft
    "This is where my mom does her job of making decorative bows from ribbons."
    m "Hi Mommy."
    "I lean in to kiss her on the cheek."
    mom "Hi Johnny. What's up?"
    m "Daddy told me you have some stomach pains?"
    mom "Yeah. It's not too bad though. It just hurts when I eat too much."
    m "Do you know why it hurts?"
    mom "No. It just hurts for a bit here after eating."
    "She points to her mid lower abdomen."
    m "Yeah. I don't think that's normal. Why didn't you go to the doctor's yet?"
    mom "I planned on going sometime in September. I’m too busy right now."
    m "Are you sure? You can go with me when I get my physical for school."
    mom "Um… What day?"
    m "I think I'll try to schedule it next week."
    mom "Ok. Make sure I'm with the woman doctor."
    m "Ok."
    scene basement_stairs with wiperight
    play sound "sfx/basement_up.mp3"
    pause 1.4

    scene my room house day with dissolve
    "I schedule the doctor's appointment and put it in my calendar."
    show august calendar at truecenter with dissolve
    mt "Oh yeah. Mommy and I are going to visit Lisa in Chicago this weekend."
    "My sister lives in the Windy City with her fiance, Dan."
    mt "Should be a good time."
    hide august calendar with dissolve
    mt "That reminds me..."
    "I like to complain to my sister about random family matters."
    play sound "sfx/text.mp3"
    m "Got I hate being home"
    play sound "sfx/text_short.mp3"
    m "God*"
    play sound "sfx/message.mp3"
    pause 0.5
    lisa "Ha why"
    play sound "sfx/text_long.mp3"
    m "Have to help do housework constantly. Mommy has stomach pain, and I had to convince her to go to the doctor with me."
    play sound "sfx/message.mp3"
    pause 0.5
    lisa "Yeah I told her she needed to go"
    mt "Well that's enough complaining. Time to help Daddy I guess."
    "The day passes uneventfully as I help do chores."
    scene black with dissolve
    play sound "sfx/lightswitch.mp3"
    pause 2

    scene my room house with dissolve
    "August 12, Friday"
    m "Are you ready yet Mommy?"
    mom "Yeah. Five more minutes."
    m "You always take forever. The train is coming in like 30 minutes!"
    dad "Johnny! Is your mom ready yet?!"
    m "Almost!"
    scene front_door_day with dissolve
    play sound "sfx/car_door1.mp3"
    pause 1.7
    scene train_station with dissolve
    "We somehow make it to the train station on time. My dad drops us off and we wave goodbye."
    scene chicago with dissolve
    "After an hour long train ride, we arrive at Ogilvie Station."
    m "Finally. Let's go Mommy."
    mom "Ok. Make sure you hold my hand."
    m "Fine."
    "My mom smiles happily as we head to the street. Lisa and Dan pick us up, and we head to the restaurant."
    scene roister entrance with dissolve
    lisa "We ordered a lot so dig in!"
    m "Thanks!"
    "Dinner proceeds blissfully as multiple great dishes come one after the other."
    show roister1 at center_above with dissolve
    ""
    hide roister1
    show roister2 at center_above with dissolve
    ""
    hide roister2
    show roister3 at center_above with dissolve
    ""
    hide roister3 with dissolve
    "We head back to my sister’s apartment afterwards."
    scene lisa condo with dissolve
    lisa "Do you guys want to see a movie? There isn’t too much else to do right now."
    m "Sure. Mommy?"
    mom "I’m ok. I’m a little tired so I’ll just lie down here. Have fun though."
    m "Ok. You guys ready then?"
    dan "Yeah."
    scene lisa hallway with wiperight
    lisa "Do you think mommy will be okay?"
    m "Think so. She usually has stomach issues after eating. I scheduled a doctor’s appointment with her for Tuesday."
    lisa "That’s good. Hopefully it’s nothing too serious."
    scene black wtih dissolve
    pause 0.3
    play sound "sfx/lightswitch.mp3"
    pause 2

    scene my room house day with dissolve
    "August 16, Tuesday"
    m "Mommy! Are you ready yet!"
    mom "Yeah! Just a little bit longer!"
    scene front_door_day with dissolve
    play sound "sfx/car_door1.mp3"
    pause 1.7
    scene doctors with fade
    "My physical proceeds normally. Pretty much nothing has changed from last year."
    "After I get back to the waiting room, my mom is called in to see the same doctor."
    scene black with dissolve
    scene doctors with fade
    "My mom finally returns to the waiting room."
    m "What did the doctor say?"
    mom "She wasn’t sure what was wrong exactly, but she said she'll try to schedule a CT scan for me. Also, I need medicine to help me go to toilet."
    m "Oh. Ok."
    mom "Can we stop by the grocery story and pharmacy?"
    m "Sure."

    scene black with dissolve
    "A few days pass as we wait for the phone call to approve the CT scan. My dad worries over every ring of the home phone."
    "I brush it all off and spend time coding and playing with friends."
    "Before I know it, it’s time to head back to school."

    scene my room house day with dissolve
    "August 21, Sunday"
    dad "Johnny! Did you pack everything yet?"
    m "Almost! I’ll bring everything down after I shower!"
    "After getting ready, I head downstairs to eat a quick lunch."
    scene main_stairs_down with wipeleft
    play sound "sfx/stair_down.mp3"
    pause 1.4
    scene dining room day with dissolve
    mom "Johnny, can you grill the food I marinated for you? I’m too tired right now."
    "My mom always makes food for me to bring back to school. Helps a lot when I have to return to an empty fridge."
    m "Sure. Are you ok?"
    mom "Yeah. I’ll be downstairs making bows. Tell me if you need help."
    scene backyard with wipeleft
    "I eat lunch while grilling the chicken and ribs."
    mt "I wonder how much longer this is going to take..."
    scene basement_stairs with dissolve
    play sound "sfx/basement_down.mp3"
    pause 1.4
    scene basement with wipeleft
    m "Hi Mommy. The chicken has been cooking for 45 minutes. How much longer should I grill it?"
    mom "What temperature is it at?"
    m "400."
    mom "It should be ok in 20 more minutes."
    m "Alright."
    scene backyard with wiperight
    "I finish grilling the food and head inside to bag it."
    scene dining room day with dissolve
    mt "Alright time to put everything in the car."
    scene front_door_day with dissolve
    play sound "sfx/car_door1.mp3"
    "I pack the food and the rest of my stuff in my car."
    dad "Is that everything?"
    m "Let me do a last check of my room."
    dad "Sure. Say bye to your mom too."
    scene my room house with dissolve
    mt "Hm. Don't think I forgot anything. I'll be back soon anyways."
    scene doorway with dissolve
    "Just as I come downstairs, my mom comes up from the basement to say goodbye."
    mom "Bye Johnny. I’ll miss you!"
    "We hug and kiss each other on the cheeks."
    m "Yup. I’ll be back in two weeks so don’t worry too much. "
    mom "Do you have all the food packed?"
    m "Yeah. I think I have everything. Bye Mommy!"
    scene front_door_day with dissolve
    "I head out of the house to my car and message my friends that I’m heading out to pick them up."
    dad "The car should be ready. Bye Johnny."
    m "Bye Daddy. See you in two weeks!"
    "As I’m about to start driving, my mom waves goodbye from the doorway."
    "I wave goodbye to my parents then head off to my friends' houses."
    #
    #scene black with dissolve
    stop music fadeout 1.0
    #pm "Unbeknownst to me at the time, that would be the last I’d see my mom in a healthy state."

    #pause 1.0
    #Around 10-12 minutes or reading so far

    jump chapter2
