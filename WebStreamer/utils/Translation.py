# This file is a part of TG-FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
<i>ð Há´Ê,</i>{}\n
<i>I'm Telegram Files Streaming Bot As Well Direct Links Generator</i>\n
<i>CÊÉªá´á´ á´É´ Há´Êá´ á´á´ É¢á´á´ á´á´Êá´ ÉªÉ´Òá´Êá´á´á´Éªá´É´</i>\n
<i><u>ðªðð¥ð¡ðð¡ð ð¸</u></i>\n
<b>ð PÊá´É´ á´á´É´á´á´É´á´ê± Êá´á´á´ê± á´á´ á´á´Êá´á´É´á´É´á´ Êá´É´ Êá´á´.</b>\n\n"""

        HELP_TEXT = """
<i>- Sá´É´á´ á´á´ á´É´Ê ê°ÉªÊá´ (á´Ê) á´á´á´Éªá´ ê°Êá´á´ á´á´Êá´É¢Êá´á´.</i>
<i>- I á´¡ÉªÊÊ á´Êá´á´ Éªá´á´ á´xá´á´ÊÉ´á´Ê á´ÉªÊá´á´á´ á´á´á´¡É´Êá´á´á´ ÊÉªÉ´á´ !.</i>
<i>- á´á´á´¡É´Êá´á´á´ LÉªÉ´á´ WÉªá´Ê Fá´sá´á´sá´ Sá´á´á´á´</i>
<u>ð¸ ðªðð¥ð¡ðð¡ð ð¸</u>\n
<b>ð PÊá´É´ á´á´É´á´á´É´á´ê± Êá´á´á´ê± á´á´ á´á´Êá´á´É´á´É´á´ Êá´É´ Êá´á´.</b>\n
<i>Cá´É´á´á´á´á´ á´á´á´ á´Êá´á´á´Ê (á´Ê) Êá´á´á´Êá´ Êá´É¢ê±</i> <b>: <a href='https://t.me/NVSHDMOVIE'>[ @ðððððððððð ]</a></b>"""

        ABOUT_TEXT = """
<b>â MÊ É´á´á´á´ : NVS Link Generator Bot</b>\n
<b>ð¸Vá´Êê±Éªá´É´ : 3.0.3.1</b>\n
<b>ð¹ðð¨ð¯ð¢ð ðð¡ðð§ð§ðð¥ : @NVSHDMOVIE </b>
"""

        stream_msg_text ="""
<i><u>ð¬ð¼ðð¿ ðð¶ð»ð¸ ðð²ð»ð²ð¿ð®ðð²ð± !</u></i>\n
<b>ð FÉªÊá´ É´á´á´á´ :</b> <i>{}</i>\n
<b>ð¦ FÉªÊá´ ê±Éªá´¢á´ :</b> <i>{}</i>\n
<b>ð¥ Dá´á´¡É´Êá´á´á´ :</b> <i>{}</i>\n
<b>ð¥WATCH :</b> <i>{}</i>\n
Â ðð·ð¸ð ð»ð¸ð½ðº ð¸ð ð¿ð´ðð¼ð°ð½ð´ð½ð ð°ð½ð³ ðð¸ð»ð» ð½ð¾ð ð´ðð¿ð¸ðð´\n
@NVSHDMOVIE"""

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Há´Êá´', callback_data='help'),
        InlineKeyboardButton('AÊá´á´á´', callback_data='about'),
        InlineKeyboardButton('CÊá´sá´', callback_data='close')
        ],
        [InlineKeyboardButton("ð¢ ï¼­ï½ï½ï½ï½ ï¼£ï½ï½ï½ï½ï½ï½", url=f'https://t.me/NVSHDMOVIE')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Há´á´á´', callback_data='home'),
        InlineKeyboardButton('AÊá´á´á´', callback_data='about'),
        InlineKeyboardButton('CÊá´sá´', callback_data='close'),
        ],
        [InlineKeyboardButton("ð¢ ï¼­ï½ï½ï½ï½ ï¼£ï½ï½ï½ï½ï½ï½", url=f'https://t.me/NVSHDMOVIE')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Há´á´á´', callback_data='home'),
        InlineKeyboardButton('Há´Êá´', callback_data='help'),
        InlineKeyboardButton('CÊá´sá´', callback_data='close'),
        ],
        [InlineKeyboardButton("ð¢ ï¼­ï½ï½ï½ï½ ï¼£ï½ï½ï½ï½ï½ï½", url=f'https://t.me/NVSHDMOVIE')]
        ]
    )
