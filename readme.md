
![]()

# WTF?

This is your tiny and friendly software made with GTK+ and Python to ask you some stuff to check if you have learn your lesson.

You're welcome.

You decide the interval of time for each quiz to spawn.

Question are picked randomly.

YOU write your quiz.

# DEPENDENCIES

Well, not much.

- Python 3
- PyGObject
- setuptools

#USAGE

    $ bram [interval]

_**interval** is the number of minutes between each quiz._

# INSTALLATION

You can get the code on [github](https://github.com/denissalem/bram).

    ./setup.py install --user

_It might be necessary to install PyGObject from your distribution package system._

# BUILD YOUR KNOWLEDGES DATABASE

Your knowledges are stored as JSON files in ~/.bram/knowledges

A typical quiz look's like the following:

'''{
    "question": "Which number is a Mercenne prime?",
    "answers" : {
        "7": true,
        "9": false,
        "4": false,
        "5": false
    }
}'''

Some tips to keep in mind:

- Your quiz must have a question field
- The answers field may have as many items as you want.
- There is only one good answer.
