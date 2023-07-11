# Accountant Bot

This is a Telegram bot written in Python using the `aiorgam` library. The bot has the following features:

- Greets the user and provides a menu with options.
- Allows you to record spending or income.
- Displays the history of expenses / income for the day / month / year / the entire period.
- Supports built-in keyboard for interaction.

## Getting Started

To use this bot, you need to have Python installed on your machine. Follow these steps to get started:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Obtain a bot token from the [BotFather](https://core.telegram.org/bots#botfather) and update the `config.py` file with your token.
4. Run the bot by executing the `bot.py` script.

## Usage

Once the bot is running, open your Telegram app and search for the bot using its username. Start a chat with the bot and you will see the following options:

- **/start**: Command to start bot.
- **/s и сумму расхода**: Enter the command `/s` and the amount of the expense for the bot to record.
- **/e и сумму дохода** : Enter the `/e` command and the amount of income for the bot to make an entry.
- **История за день** : The bot will display records for 1 day, if these records were.
- **История за месяц** : The bot will display records for a month, if these records were.
- **История за год** : The bot will display records for a year, if these records were.
- **История за весь период** : The bot will display records for the entire period, if these records were.

Choose the desired option and interact with the bot accordingly.