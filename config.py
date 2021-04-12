from os import getenv

from dotenv import load_dotenv

default_bot_token = "1657468666:AAEDDax6PsuDnXHzLprpf95MvF5tzDD0rtg"
default_owner_id = 1476130628
default_owner_hash = "59940cc8cba6160443c26cf682ba6885"
default_owner_hashid = 3864646
default_owner_string = "BAAyWLxI5dl9OLh4t1CrgsDUztatlFlvPuh6IiunNbPJuDDjKRgwkOoBelbXrb3i3IU6ULwNNUcB89aS3Op711HRx4RaDrx9-m_vnB75uH1Xa48pYUc0Hek-hjbRR9zcl-c9ONY-6t5j-vs0XWPqAXFNyW1YkEPv7Xe9vw5L4-WcI5V62wql78g3eTQqsKALN5dLXFKncttFulUoEyb5FyezOrhiBWnsbaBj0ECmm2hFgpEUwvAHC8YYtnfB6OXZ-tnnaK21piy6XEAnrrl9Z0c_2xfOfdochYVqqvf40mpySvhqMFqKCb6jz0fGCNii9WiVTWNmVXSwStMl1EWxnwoLX7J4gAA"

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", default_owner_string)
BOT_TOKEN = getenv("BOT_TOKEN", default_bot_token)
BOT_NAME = getenv("BOT_NAME")

API_ID = int(getenv("API_ID", default_owner_hashid))
API_HASH = getenv("API_HASH", default_owner_hash)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", default_owner_id).split()))
