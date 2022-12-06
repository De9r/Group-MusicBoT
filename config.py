from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "AQDCvokFkIOeZOSEOP1E2LjVzHiiAikVt4Kcv0ihgtRilRA1yAkWj6JkwVN_E219SRuH-BGFZt7MT83S6axTNLsFKI96vi9P2LQD5R6GIVqpcO-y_cC6DZ_FHiRq9hEpTgpS6cYeewm-MsuYN3AzQoh53LfOYpiEcN4txPaMco1I41Xr_UhW2tzgwNbnX3AuiN4V8VlqCRqjuwySfBn76YDKEKOaxvR0iJsoN9_d3CcMPvDlE2cAaoaJOtz2gJyZhuQVhdadeHr0L8si3g5qOANqsP4Jt1SqWtvEa8QbowcEKcgL7O9w1i0VFPryfTgRhxpMk1PlGyyWMZEdP53U2ZXYAAAAATEeBl8A")
BOT_TOKEN = getenv("BOT_TOKEN","1990152924:AAFw0Dv4EPA_bjaxztSUBSM1tUCACgTAMTE")
BOT_NAME = getenv("BOT_NAME","ملطلط")

API_ID = int(getenv("API_ID"),17338150)
API_HASH = getenv("API_HASH","a855f783b521cbecef19e0e5dca232de")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
