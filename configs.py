# (c) @LazyDeveloperr
import os
from os import getenv, environ


# Online Stream and Download
PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
	ON_HEROKU = True
	APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN','lazy-gangster-baby-lazydeveloperr.koyeb.app') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "http://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
DISABLE_CHANNEL_BUTTON = bool(environ.get('DISABLE_CHANNEL_BUTTON', False))
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', '-1002097432152'))
BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001987654567")).split())) 
STREAM_LOGS = environ.get('STREAM_LOGS','-1002007510451')
SESSION = environ.get('SESSION','MissRozy')
CUSTOM_CAPTION = environ.get('CUSTOM_CAPTION')


class Config(object):
	API_ID = int(os.environ.get("API_ID", 27505575))
	API_HASH = os.environ.get("API_HASH", "03bbc5e15dbddfb03fb953435b5eb028")
	BOT_TOKEN = os.environ.get("BOT_TOKEN","7028356497:AAGcawXxGHWTE2a2-zR_AE52-QYqy3Tzrtk")
	BOT_USERNAME = os.environ.get("BOT_USERNAME" , "silentfilestorebot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", -1002007510451))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "2056329003"))
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Aru:VXLPtm8IhOMMklOR@atlascluster.btk4mu1.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002097432152")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002132361598")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	LAZY_CHANNEL = int(os.environ.get('LAZY_CHANNEL','-100'))
	LAZY_MODE = bool(os.environ.get("LAZY_MODE", False))
	LAZY_PIC = os.environ.get("LAZY_PIC","https://telegra.ph/file/d382d2fad1fdd2a4ccca4.png")
	LP_BTN_MAIN_CH_USRNM = os.environ.get("LP_BTN_MAIN_CH_USRNM")
	LP_CHANNEL_USRNM = os.environ.get("LP_CHANNEL_USRNM")
	LPCH_ADMIN_USRMN = os.environ.get("LPCH_ADMIN_USRMN")
	LP_CUSTOM_TEMPLATE= os.environ.get("LP_CUSTOM_TEMPLATE")
  # LP_CUSTOM_TEMPLATE= os.environ.get("LP_CUSTOM_TEMPLATE","{file_name} - example \n\n Please Upadate this template acording to you @LazyDeveloperr ")
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	AUTO_DELETE_TIME = int(os.environ.get('AUTO_DELETE_TIME', 60))

	ABOUT_BOT_TEXT = f"""
ᴛʜɪꜱ ɪꜱ ᴘᴇʀᴍᴀɴᴇɴᴛ ꜰɪʟᴇꜱ ꜱᴛᴏʀᴇ ʙᴏᴛ!
ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ɪ ᴡɪʟʟ ꜱᴀᴠᴇ ɪᴛ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ. ᴀʟꜱᴏ ᴡᴏʀᴋꜱ ꜰᴏʀ ᴄʜᴀɴɴᴇʟ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴀꜱ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴇᴅɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ, ɪ ᴡɪʟʟ ᴀᴅᴅ ꜱᴀᴠᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ꜰɪʟᴇ ɪɴ ᴄʜᴀɴɴᴇʟ & ᴀᴅᴅ ꜱʜᴀʀᴀʙʟᴇ ʙᴜᴛᴛᴏɴ ʟɪɴᴋ.

🤖 *ᴍʏ ɴᴀᴍᴇ:* [ꜰɪʟᴇꜱ ꜱᴛᴏʀᴇ ʙᴏᴛ](https://t.me/silentfilestorebot)

📝 *ʟᴀɴɢᴜᴀɢᴇ:* [PУΓHФИ3](https://www.python.org)

📚 *ʟɪʙʀᴀʀʏ:* [P͢y͢r͢o͢g͢r͢a͢m͢](https://docs.pyrogram.org)

📡 *ʜᴏꜱᴛᴇᴅ ᴏɴ:* [koyeb](https://app.koyeb.com)

🧑🏻‍💻 *DΞVΞLФPΞЯ:* [ARU](https://t.me/silent_amv)

👥 *Movie gr⊕up:* [ARU MOVIE](https://t.me/movieseriesanimehindi)

📢 *Anime Group:* [ARU ANIME](https://t.me/anime_movies_series_hindi_dub)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 <a href='https://t.me/silent_amv'>*ミ★- ARU-★彡* </a>

<a href=''https://t.me/silent_amv>ARU</a> ɪꜱ ꜱᴜᴘᴇʀ ɴᴏᴏʙ 😎. ᴊᴜꜱᴛ ʟᴇᴀʀɴɪɴɢ ꜰʀᴏᴍ ᴏꜰꜰɪᴄɪᴀʟ ᴅᴏᴄꜱ. Main credit goes to @LazyDeveloperr .
ᴀʟꜱᴏ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴡɪʟʟ ᴅᴇʟᴇᴛᴇ ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛꜱ ꜰʀᴏᴍ ᴅᴀᴛᴀʙᴀꜱᴇ. ꜱᴏ ʙᴇᴛᴛᴇʀ ᴅᴏɴ'ᴛ ꜱᴛᴏʀᴇ ᴛʜᴏꜱᴇ ᴋɪɴᴅ ᴏꜰ ᴛʜɪɴɢꜱ.
"""
	LAZY_HOME_TEXT = """
HΞУ, [{}](tg://user?id={})\n\nɪ'ᴍ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ *ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ*.

ミ★ 𝘚𝘦𝘯𝘥 𝘮𝘦 𝘢𝘯𝘺 𝘧𝘪𝘭𝘦 𝘐 𝘸𝘪𝘭𝘭 𝘨𝘪𝘷𝘦 𝘺𝘰𝘶 𝘢 𝘱𝘦𝘳𝘮𝘢𝘯𝘦𝘯𝘵 𝘚𝘩𝘢𝘳𝘢𝘣𝘭𝘦 𝘓𝘪𝘯𝘬. 𝘐 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘈𝘭𝘴𝘰! 𝘊𝘩𝘦𝘤𝘬 *A͢b͢o͢u͢t͢ B͢o͢t͢*  𝘉𝘶𝘵𝘵𝘰𝘯 .

«[⚡𝙇𝙖𝙯𝙮 𝙢𝙤𝙙𝙚 𝙨𝙩𝙖𝙩𝙪𝙨 : 𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋✅]»
 🥷 𝘕𝘰𝘸 𝘌𝘷𝘦𝘳𝘺𝘵𝘩𝘪𝘯𝘨 𝘪𝘴 𝘶𝘱𝘰𝘯 𝘮𝘦 🥷
"""
	HOME_TEXT = """
HΞУ, [{}](tg://user?id={})\n\nɪ'ᴍ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ *ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ*.

ミ★ 𝘚𝘦𝘯𝘥 𝘮𝘦 𝘢𝘯𝘺 𝘧𝘪𝘭𝘦 𝘐 𝘸𝘪𝘭𝘭 𝘨𝘪𝘷𝘦 𝘺𝘰𝘶 𝘢 𝘱𝘦𝘳𝘮𝘢𝘯𝘦𝘯𝘵 𝘚𝘩𝘢𝘳𝘢𝘣𝘭𝘦 𝘓𝘪𝘯𝘬. 𝘐 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘈𝘭𝘴𝘰! 𝘊𝘩𝘦𝘤𝘬 *A͢b͢o͢u͢t͢ B͢o͢t͢*  𝘉𝘶𝘵𝘵𝘰𝘯 .

 😏𝙣𝙤𝙬 𝙞𝙩𝙨 𝙖𝙡𝙡 𝙪𝙥𝙤𝙣 𝙪 𝙗𝙖𝙗𝙮👍
"""


