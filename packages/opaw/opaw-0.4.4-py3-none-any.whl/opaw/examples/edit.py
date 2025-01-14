from opaw.util import log
from opaw.model.edit import EditBot
from opaw import util
from opaw.examples import setup

"""
====================
= Deprecated model =
====================
"""

# api key
setup()

# logger
logger = log.get("edit", "logs/edit.log")

# edit
bot = EditBot()
prompt = "Hey, this was my filst car!!"  # filst -> first
instruction = "Fix the spelling mistakes"
response = bot.create(prompt, instruction=instruction)
text = response["choices"][0]["text"]
logger.info(f"text: {text}")

# save history if needed
bot.save_history("history/edit-hist.json")
