from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**โจ Welcome,I'm {bn} ๐ต

[Groups Music](https://t.me/sangramghangale). is a project designed for play, as simple as possible, music in your groups through the new voice chats introduced by Telegram.

โHow to use it?
Press the ยป ๐ Commands button to view the full list of the commands of the bot!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐", url="https://telegra.ph/TELEGRAM-GROUP-MUSIC-BOT-04-09")
                  ],[
                    InlineKeyboardButton(
                        "๐๐ฟ๐ผ๐๐ฝ", url="https://t.me/maharashtrafriendcircle"
                    ),
                    InlineKeyboardButton(
                        "๐๐ต๐ฎ๐ป๐ป๐ฒ๐น", url="https://t.me/chocolatyqueenvcplayer"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "๐๐ฑ๐ฑ ๐ง๐ผ ๐ฌ๐ผ๐๐ฟ ๐๐ฟ๐ผ๐๐ฝ", url="https://t.me/ChocolateQueenBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐๐ต๐ฎ๐ป๐ป๐ฒ๐น", url="https://t.me/chocolatyqueenvcplayer")
                ]
            ]
        )
   )


