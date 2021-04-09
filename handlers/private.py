from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**✨ Welcome,I'm {bn} 🎵

[Groups Music](https://t.me/sangramghangale). is a project designed for play, as simple as possible, music in your groups through the new voice chats introduced by Telegram.

❓How to use it?
Press the » 🎛 Commands button to view the full list of the commands of the bot!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀", url="https://telegra.ph/TELEGRAM-GROUP-MUSIC-BOT-04-09")
                  ],[
                    InlineKeyboardButton(
                        "𝗚𝗿𝗼𝘂𝗽", url="https://t.me/maharashtrafriendcircle"
                    ),
                    InlineKeyboardButton(
                        "𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/chocolatyqueenvcplayer"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "𝗔𝗱𝗱 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽", url="https://t.me/ChocolateQueenBot?startgroup=true"
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
                        "𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/chocolatyqueenvcplayer")
                ]
            ]
        )
   )


