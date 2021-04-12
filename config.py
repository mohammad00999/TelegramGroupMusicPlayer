from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = "BACMzxTIYDepsMGA5J5Eqe_W6GbVSFH9R78B4sqP0no8PgFhUGTKbQnoKhMdPSc8VA4FgIL6ji2gPcGkHRUtEpW4aph6mDPk5OO2W-UvSo4qc-54z3GB2-8kqGKeoMXMLRC-MQVSHpOdG-aAL1rZ0lTE5KlmcjsllWRw72vwrXtizUP8Ylj-WTTS-SpQ1nWrtdwolyqUZ9BjRzYILFYzK2vgv8D1qQPQITeKE5tPMClObDd1vtuUg5v6ih-G47e0WLZ2oBQetWryQY37pl-1e6MeeX0OkUZyyjKQh320WtWbomEVLcd-nWB1ptTIjq1WkHUGa4fE1XtNooc1juv9NxvMWdduGgA"
BOT_TOKEN = "1732667279:AAGRH0hxRh_q10jaO7HKbFsv_a283nl4CEU" 
BOT_NAME = "SylixmusicPlayerbot"

API_ID = "3841155"
API_HASH = "afe725b6a08bc532b2ff5b7b51740fcc"

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = int("1476130628")
