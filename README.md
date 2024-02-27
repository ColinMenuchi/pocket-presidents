# Pocket Presidents

This is a program I initially designed as a final project for UVM's CS1210 course.
Now, it is a game that I sometimes work on in my freetime.

Pocket Presidents is a hilarious take on the popular website Pokemon Showdown.
You get to build a team of Pokemon and battle with them, only all the Pokemon are
US Presidents! Each President has four moves, each holding some surprise in battle.
Moves could deal damage, heal your president, raise your president's stats, or lower
your oppoenent's stats. The goal is to create a team of three that can defeat the computer's
team! At the same time, the moves you will use in battle are only intuitive if you know your
US presidents, which adds an extra challenge. However, unlike Pokemon there are no types and
no swapping in battle. This way, battles can resemble presidential debates way more easily.
If you aren't careful, a battle could become long, drawn-out, or just seemingly go nowhere.
Do you have what it takes to become a Pocket President master? Only one way to
find out!

Pip-Installable Modules Needed for Running (Along With Their Versions):
pygame==2.5.2
PySide6==6.6.0
PySide6-Addons==6.6.0
PySide6-Essentials==6.6.0
setuptools==68.2.2
shiboken6==6.6.0
wheel==0.41.2

Instructions For Running & Testing:
Download all files and folders in this repository and make sure they are all in the same directory.
Once everything is downloaded, run the python file titled: pocket_presidents.py
Upon running the program you will be greeted by the home screen. Wait for the animation to finish playing
and then click the start button that appears in the middle of the screen. This will take you to the
president select screen. Use the scroll buttons on the left and right hand sides of the screen to
view your options. Click the select button next to three of the presidents to build your team. Once
you have selected three presidents, click the big "GO" button that appears in the middle of the screen.
This will take you to the battle screen. In the bottom right, click the red "FIGHT" button. This will open
the move menu for your current president. Pick one of the four moves and try to defeat your opponent.
Part of the challenge is trying to guess what each move does, as part of the game is to test your US
president knowledge. If you understand what a move references, you might get an idea as what it's supposed
to do. However, for the sake of testing, I have included a catalog of each move and it's effect below so
you know what to expect when testing a move. If you can faint all three of your opponent's presidents, you win.
If your opponent faints all three of your presidents, you lose. On the win/loss screen, a restart button
and a quit button appear. Click the restart button to play again. Click the quit button to close the game.

How I Tested My Program:
Each time I added in a new feature I would test it before moving on to the next thing. When making the home screen,
I made sure the animation worked as intended before moving to the start button.
Then I made sure the start button worked, etc. The battle was the hardest part to test as it took so much code.
First I made sure that damaging moves worked. Then I added in a speed calculation, which brought new problems that
had to be solved. I made sure each president had a speed stat, the one with the higher one moves first,
and each round both presidents only move once (assuming neither ofthem die). After that it was
healing moves and stat change moves. I continued to test each feature when it was implemented.
Now the game is complete, and although there is a lot of code, the battle mechanics are complex and completely work.
However, because this is a game, I have also had my friends play test it in order to find bugs, get ideas for
balance changes, and get general feedback.

Known Defects (But Not Really):
There are no defects to my knowledge, but a couple things to note. I in my playthroughs I found that
pygame can be a little finicky (sometimes). If you encounter any of the following problems you can get around
them by either closing and restarting the game or by using these fixes. If the buttons do not
do anything when you click them, click them rapidly 2-3 times. If a president dies in battle and is not moving off
the screen, be patient, it always happens eventually. Lastly, if you click the fight button and end up at the confirm
menu, this is because pygame registered you clicking one of the move buttons, so just click the back button.

Citations:
I wrote all the code and drew all of the president sprites and button images. However, many of the ideas
that made this game possible were contributed by friends. Collaborating with others to develop this game
was truly an unforgettable experience.

The following files are not mine, nor do I claim owndership of them:
(graphics/ampersand.png) - From: https://www.glitschkastudios.com/work/dungeons-dragons
(graphics/menu_background.jpeg) - From: https://www.bbc.com/news/election-us-2020-54003441
(graphics/oval_office.jpeg) - From: https://www.npr.org/sections/president-biden-takes-office/2021/01/21/959223157
(graphics/pokemon_title.png) - From: https://www.cheatcc.com/articles/the-history-of-the-pokemon-logo/
photos-president-bidens-redecorated-oval-office
(graphics/pokemon_battlefield2.webp) - From: https://pokemon-reborn.fandom.com/wiki/Fairy_Tale_Field
(audio/B&W-Battle_Gym_Leader.mp3) - From: https://downloads.khinsider.com/game-soundtracks/album/pokemon-black-and-white
(audio/B&W-Battle_Team_Plasma.mp3) - From: https://downloads.khinsider.com/game-soundtracks/album/pokemon-black-and-white
(audio/B&W-Battle_Wild.mp3) - From: https://downloads.khinsider.com/game-soundtracks/album/pokemon-black-and-white
(audio/B&W-Team_Plasma_Victory.mp3) - From: https://downloads.khinsider.com/game-soundtracks/album/pokemon-black-and-white
(audio/B&W-Wild_Pokemon_Victory.mp3) - From: https://downloads.khinsider.com/game-soundtracks/album/pokemon-black-and-white
(audio/battle_button_click.mp3) - From: https://pixabay.com/sound-effects/button-124476/
(audio/Battle-Chairman_Rose.flac) - From: https://downloads.khinsider.com/game-soundtracks/album/pokemon-sword-shield-ost
(audio/Battle-Marnie.flac) - From: https://downloads.khinsider.com/game-soundtracks/album/pokemon-sword-shield-ost
(audio/Marnie-Victory.flac) - From: https://downloads.khinsider.com/game-soundtracks/album/pokemon-sword-shield-ost
(audio/menu_song.mp3) - From: https://downloads.khinsider.com/game-soundtracks/album/pokemon-red-green-blue-yellow
(audio/spb_piano.mp3)- From: https://pixabay.com/music/modern-classical-the-star-spangled-banner-piano-version-145016/
(audio/spb.mp3) - From: https://pixabay.com/music/special-occasions-the-star-spangled-banner-113772/
(audio/start_button_click.mp3) - From: https://pixabay.com/sound-effects/click-124467/
(audio/stat_drop.mp3) - From: https://youtu.be/ptAJqPVwgec?si=oWHX3dOnbIhBJFCK
(audio/stat_raise.mp3) - From: https://youtu.be/ptAJqPVwgec?si=oWHX3dOnbIhBJFCK

Move Catalog:
-George Washington- (The Glass Cannon)
Cross Delaware - Raise Washington's Attack
Tar and Feather - Lower Opponent's Speed
Valley Forge - Heal User (2/3 of Max HP)
Bayonet Charge - Deals Damage to the Opponent

-Abraham Lincoln- (The Jack of All Trades (Offense))
Emancipate - Heal User (1/3 of Max HP)
Four Score - Deals Damage to the Opponent
Divided House - Deals Damage to the Opponent
For The Union - Raises Lincoln's Attack

-Bill CLinton- (The Jack of All Trades (Defense))
Sign NAFTA - Raises Clinton's Attack
Ms. Lewinsky? - Raises Clinton's Defense
Send in Hillary - Deals Damage to the Opponent
Egg McMuffin - Heal User (1/3 of Max HP)

-Obama- (The Spikey Wall)
Obamacare - Heals User (1/3 of Max HP)
Obamehameha - Deals Damage to the Opponent
Let Me Be Clear - Raises Obama's Attack
Michelle Lunch - Lowers Opponent's Defense

-Donald Trump- (The True Wall)
You're Fired - Deals Damage to the Opponent
Build a Wall - Raises Trump's Defense
Fake News - Lowers Opponent's Defense
Uuuuuuge - Heals the User (1/3 of Max HP)

-Joe Biden- (Hard Hitter, Slow Mover)
Biden Blast - Deals Damage to the Opponent
Chocolate Chip - Heals User (1/3 of Max HP)
Sniff - Lowers Opponent's Attack
Asufutimaeh- - Raise's Biden's Speed
