# Ultimate Pollbot ([@ultimate_pollbot](https://t.me/ultimate_pollbot))

[![MIT Licence](https://img.shields.io/badge/license-MIT-success.svg)](https://github.com/Nukesor/pollbot/blob/master/LICENSE.md)
[![Paypal](https://github.com/Nukesor/images/blob/master/paypal-donate-blue.svg)](https://www.paypal.me/arnebeer/)
[![Patreon](https://github.com/Nukesor/images/blob/master/patreon-donate-blue.svg)](https://www.patreon.com/nukesor)


# Customization Settings:
Ultimate Pollbot features a wide range of customization and anonymization features.

**Poll types**
This bot has 4 different vote modi. Each mode is useful for various scenarious. Choose wisely.

- Single vote: User get one vote for the poll
- Block vote: Users can vote without restriction, but only one vote per option.
- Limited vote: Each user gets X votes for distribution, but max one vote per option.
- Cumulative vote: Every user gets X votes they can distribute as they like.

**Anonymity settings:**
Polls can be configured to be anonymous. The votes of the respective users are not visible.
Polls can be made anonymous subsequently, but as soon as a poll is anonymous it stays that way!

Further it's possible to hide the results of the poll until it gets closed.
As soon as such a poll is closed, the results will be visible, but such an poll cannot be reopened~

**Custom sorting options:**
The bot allows to configure the sorting of the option list AND and the user list for each option.

Users can be sorted by vote date or username. Options can be sorted by highest percentage, name or by the order they've been added.

**Planned features:**
- Addition and removal of options
- Set a due date for a poll
- Get due date notifications for polls, if the bot is in the same group
- Date picker for date options


# Poll Management:
- Polls can be closed
- Polls can be reopened unless the poll is configured to hide the results until it has been closed.
- Polls can be completely deleted, which means that all non-forwarded occurences of the poll will be removed.


## Commands:

    /start      Start the bot
    /create     Create a new poll
    /list       List all active polls and manage them
    /donations  Get me a coffee


## Installation and Starting:

1. You will need to install `poetry` to install all dependencies.
2. Clone the repository:

        % git clone git@github.com:nukesor/ultimate_pollbot pollbot && cd pollbot

3. Now copy the `pollbot/config.example.py` to `pollbot/config.py` and adjust all necessary values.
4. Finally execute following commands to install all dependencies and to start the bot:

        % poetry install
        % poetry run initdb.py
        % poetry run main.py

5. If you plan to keep up to date, you need to set the current alemibic revision manually.
Get the latest revision with `poetry run alembic history` and change the current head to the newest revision with `poetry run alembic stamp <revision>`.
6. Now you can just execute `poetry run alembic upgrade head`, whenever you are updating from a previous version.



## Botfather Commands

    start - Start the bot
    create - Create a new poll
    list - List all active polls and manage them
    donations - Get me a coffee
