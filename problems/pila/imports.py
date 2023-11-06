"""
Avoid importing the same modules in all files of this directory,
import this file in the other .py files which needs this modules
"""

#absolute importe aparently not working
#from   implement_ds.stack import Stack

#relative import:
#import re
#from ...implement_ds.stack import Stack
# "data-structures-project" #da omission.common.game_enums import GameMode

from implement_ds.stack import Stack
s1=Stack(6)
s1.push(1)
s1.push(23)
s1.push(3)
s1.push(61)
s1.push(2)
s1.push(10)#top

print(s1.top())
"""

├── omission
    ├── README.md
    └── .gitignore
│   ├── app.py
│   ├── common
│   │   ├── classproperty.py
│   │   ├── constants.py
│   │   ├── game_enums.py
│   │   └── __init__.py
│   ├── data
│   │   ├── data_loader.py
│   │   ├── game_round_settings.py
│   │   ├── __init__.py
│   │   ├── scoreboard.py
│   │   └── settings.py
│   ├── game
│   │   ├── content_loader.py
│   │   ├── game_item.py
│   │   ├── game_round.py
│   │   ├── __init__.py
│   │   └── timer.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── resources
│   └── tests
│       ├── __init__.py
│       ├── test_game_item.py
│       ├── test_game_round_settings.py
│       ├── test_scoreboard.py
│       ├── test_settings.py
│       ├── test_test.py
│       └── test_timer.py
"""