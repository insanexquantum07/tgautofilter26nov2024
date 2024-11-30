import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '29362464'))
API_HASH = environ.get('API_HASH', '31973315b0872a0478886de31a1e4848')
BOT_TOKEN = environ.get('BOT_TOKEN', "7583841548:AAG6EwjBohqUp_dy0P3RUtZLzWKQxKoYzyo")


# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))

# This Pics Is For Start Message Picture, You Can Add Multiple By Giving One Space Between Each.
PICS = (environ.get('PICS', 'https://envs.sh/Y5c.jpg https://envs.sh/Y5j.jpg https://envs.sh/Y5_.jpg')).split() #SAMPLE PIC

NOR_IMG = environ.get("NOR_IMG", "https://envs.sh/Y5Z.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://envs.sh/Y55.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/15c1ad448dfe472a5cbb8.jpg")


# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001747994613'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5533079371 5207138613').split()]

# This Is File Channel Where You Upload Your File Then Bot Automatically Save It In Database 
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002344473596 -1002043045800 -1001866646571').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', True)) # Set True Or False
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False)) # Set True Or False (This try again button is only for request to join fsub not for normal fsub)
auth_channel = environ.get('AUTH_CHANNEL', '-1001809820921') # give your force subscribe channel id here else leave it blank
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1001821031247')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001732232755')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002043045800')).split()]
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001858701768').split()]
LOG_GROUP = int(environ.get('LOG_GROUP', '-1001984194316'))
DUMP_GROUP = int(environ.get('DUMP_GROUP', '-1001984194316'))

# MongoDB information
MULTIPLE_DATABASE = bool(environ.get('MULTIPLE_DATABASE', True)) # Set True or False

DATABASE_URI = environ.get('DATABASE_URI', "")   # IF Multiple Database Is False Then Fill Only This Database Url.
DATABASE_NAME = environ.get('DATABASE_NAME', "promovies")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'ProFilter')

# If Multiple Database Is True Then Fill All Three Below Database Uri Else You Will Get Error.
O_DB_URI = environ.get('O_DB_URI', "mongodb+srv://protgm:nPro29112024mvisreplacetgaf@promovies.b6fia.mongodb.net/?retryWrites=true&w=majority&appName=promovies")   # This Db Is For Other Data Store
F_DB_URI = environ.get('F_DB_URI', "mongodb+srv://profiles1id:pass1profilter@profiles1.df7m7.mongodb.net/?retryWrites=true&w=majority&appName=profiles1")   # This Db Is For File Data Store
S_DB_URI = environ.get('S_DB_URI', "mongodb+srv://profiles02tgafrep:profilesdb02pass@profiles2.d64l7.mongodb.net/?retryWrites=true&w=majority&appName=profiles2")   # This Db is for File Data Store When First Db Is Going To Be Full.


# Premium And Referal Settings
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', True)) # Set Ture Or False

# If PREMIUM_AND_REFERAL_MODE is True Then Fill Below Variable, If Flase Then No Need To Fill.
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20')) # number of referal count
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/f21404a4882698d5488dd.jpg')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b>-  s - \n\n- 20s - 1 \n- 40s - 1 s\n- 100s - 3 s\n- 200s - 6 s\n\n<blockquote>  s </blockquote>\n\n    \n     \n  s\n - x\n -s  \n - s s\n  s & ss\n   s\n s     1  \n\n<blockquote>   - <code>paradox52693@okhdfcbank</code></blockquote>\n\n      /myplan\n\n s s ss  \n\n  s  ss s  s s       </b>')
OWNER_USERNAME = environ.get('OWNER_USERNAME', 'talk_mrs_bot') # owner username without @

# Clone Information : If Clone Mode Is True Then Bot Clone Other Bots.
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False
CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', "") # Necessary If clone mode is true
PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', '') # Public Channel Username Without @ or without https://t.me/ and Bot Is Admin With Full Right.

# Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+EapqivvgHbc5YmY1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/infinity_botzz')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/links_tutorialbypp/25')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '+EapqivvgHbc5YmY1') # Support Chat Link Without https:// or @


# True Or False
AI_SPELL_CHECK = bool(environ.get('AI_SPELL_CHECK', True))
PM_SEARCH = bool(environ.get('PM_SEARCH', False))
BUTTON_MODE = bool(environ.get('BUTTON_MODE', False))
MAX_BTN = bool(environ.get('MAX_BTN', True))
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
IMDB = bool(environ.get('IMDB', False))
AUTO_FFILTER = bool(environ.get('AUTO_FFILTER', True))
AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", False))
SPELL_CHECK_REPLY = bool(environ.get("SPELL_CHECK_REPLY", True))
MELCOW_NEW_USERS = bool(environ.get('MELCOW_NEW_USERS', True))
PROTECT_CONTENT = bool(environ.get('PROTECT_CONTENT', False))
PUBLIC_FILE_STORE = bool(environ.get('PUBLIC_FILE_STORE', True))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))


# Token Verification Info :
VERIFY = bool(environ.get('VERIFY', True))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', 'runurl.in')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '23713ba321c3ed8a7d3580276b0248a5a41f30bd')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', 'https://t.me/links_tutorialbypp/19')

# If You Fill Second Shortner Then Bot Attach Both First And Second Shortner And Use It For Verify.
VERIFY_SECOND_SHORTNER = bool(environ.get('VERIFY_SECOND_SHORTNER', True))
# if verify second shortner is True then fill below url and api
VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', '')
VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '')


# Shortlink Info
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'tnshort.net')
SHORTLINK_API = environ.get('SHORTLINK_API', '9bccb0b14ed6841652fa22d3481907788c1b8838')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/links_tutorialbypp/19') # How Open Shortner Link Video Link , Channel Link Where You Upload Your Video.


# Others
MAX_B_TN = environ.get("MAX_B_TN", "7")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', '⚠️ ғᴏʟʟᴏᴡ, sᴜʙsᴄʀɪʙᴇ ᴀɴᴅ sʜᴀʀᴇ!')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)


# Choose Option Settings 
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]
EPISODES = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25", "E26", "E27", "E28", "E29", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E38", "E39", "E40"]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]
YEARS = ["1900", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]



# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://spotless-shrew-infinitybotz1105-c4f0c399.koyeb.app/")


# Rename Info : If True Then Bot Rename File Else Not
RENAME_MODE = bool(environ.get('RENAME_MODE', False)) # Set True or False


# Auto Approve Info : If True Then Bot Approve New Upcoming Join Request Else Not
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', True)) # Set True or False


# Start Command Reactions
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"] #don't add any emoji because tg not support all emoji reactions


if MULTIPLE_DATABASE == False:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI    # This Db is for User Data Store
    OTHER_DB_URI = O_DB_URI       # This Db Is For Other Data Store
    FILE_DB_URI = F_DB_URI        # This Db Is For File Data Store
    SEC_FILE_DB_URI = S_DB_URI    # This Db is for File Data Store When First Db Is Going To Be Full.
