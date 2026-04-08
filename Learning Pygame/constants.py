"""
Author: Gaby White
PyGame Surface Assignment 6
""" 

from vector import vec
from button import Button
from drawable import Drawable

RESOLUTION = vec(800, 400)
#WORLD_SIZE = vec(800,400)
SCALE = 1
UPSCALED = [int(x * SCALE) for x in RESOLUTION]
DOWNSCALED = [int(x * .5) for x in RESOLUTION]

CLICK = 0

START = Button(vec(313, 304), "start.png", 0, -1, True)

NEXT = Button(vec(655, 4), "next.png", 0, -1, True)

BAR = Button(vec(15, 10), "bar.png", 0, -1)

MENU = Button(vec(0, 0), "baseMenu.png", 0, -1)

SCROLLBAR = Button(vec(0,0), "scrollBar.png", 0, -1)

ARROW1 = Button(vec(0, 0), "arrow1.png", 0, 100, False, True)

ARROW2 = Button(vec(0, 0), "arrow2.png", 0, -100, False, True)

PLAY = Button(vec(600, 4), "play.png", 0, -1, True)

BUTTONS = [Button(vec(5, 104), "club.png", 3, 1), 
           Button(vec(200, 104), "coffee.png", 1, 2),
           Button(vec(395, 104), "date.png", 2, 3),
           Button(vec(590, 104), "dinner.png", 2, 4),
           Button(vec(5, 204), "friends.png", 3, 5),
           Button(vec(200, 204), "nap.png", 2, 6),
           Button(vec(395, 204), "officehours.png", 2, 7),
           Button(vec(590, 204), "party.png", 4, 8),
           Button(vec(5, 304), "scroll.png", 1, 9),
           Button(vec(200, 304), "study.png", 3, 10),
           Button(vec(395, 304), "volunteer.png", 3, 11),
           Button(vec(590, 304), "workout.png", 4, 12)]

ENERGYUNITS = [Button(vec(65, 12), "energy.png", 0, -1),
           Button(vec(115, 12), "energy.png", 0, -1),
           Button(vec(165, 12), "energy.png", 0, -1), 
           Button(vec(215, 12), "energy.png", 0, -1),
           Button(vec(265, 12), "energy.png", 0, -1),
           Button(vec(315, 12), "energy.png", 0, -1),
           Button(vec(365, 12), "energy.png", 0, -1),
           Button(vec(415, 12), "energy.png", 0, -1),
           Button(vec(465, 12), "energy.png", 0, -1),
           Button(vec(515, 12), "energy.png", 0, -1)]

O1 = ["After looking around the club fair, you decided to join the dance club. You have learned all the fresh moves to show your friends! "
      ]
O2 = ["The number in your bank may be going down quickly, but your energy is through the roof! All the caffeine in those coffees are making it hard to sit still in class, but at least you do all of your homework quickly. "
      ]
O3 = ["While in one of your classes, you get a Snapchat notification from an someone asking to grab dinner. You decide to go, if not for the comany, for the free meal. "
      ]
O4 = ["With all the madness of your first month in college, you sure do need to stay fueled! And it doesn't hurt that the dining hall always has ice cream. "
      ]
O5 = ["You decide to branch out during lunch one day and sit with a random table. They welcome you in and even invite you to a party that night."
]
O6 = ["College is tiring... sometimes all you need is a little mid-day rest to keep your productivity high. "
]
O7 = ["To keep grades up, and make sure your GPA if up, you head over to office hours every week. But the professors not only are helping you when struggling, it also is boosting your participation grade. "
]
O8 = ["School is fun, sure. But the real point of college is to party. Hard. You truly know the meaning of 'play hard', but the 'work hard' part is still up for debate. "
]
O9 = ["Sometimes, all you need is mind numbing doomscrolling to lift your mood. Looking back at all the memories you made during your first month, you are excited to keep the whirlwind going. "
]
O10 = ["Time to hit the books with midterms coming up. You need the 4.0 to stay a 4.0, and the library has become one of your best friends to accomplish that. "
]
O11 = ["A break from studying gives you the perfect time to go out and help the local community. Doesn't hurt that your biology professor happens to be there every Saturday too. "
]
O12 = ["It is bulking season. For your mind, for your soul, and most importantly, for your body. To be the best in class, you need to be your best physically. "
]
O13 = []
O14 = []
O15 = []
O16 = []
O17 = []
O18 = []
O19 = []
O20 = []
O21 = []
O22 = []
O23 = []
O24 = []