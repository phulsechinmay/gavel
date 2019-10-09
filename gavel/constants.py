ANNOTATOR_ID = 'annotator_id'
TELEMETRY_URL = 'https://telemetry.anish.io/api/v1/submit'

# Setting
# keys
SETTING_CLOSED = 'closed' # boolean
SETTING_STOP_QUEUE = 'queued' # boolean
# values
SETTING_TRUE = 'true'
SETTING_FALSE = 'false'

# Defaults
# these can be overridden via the config file
DEFAULT_WELCOME_MESSAGE = '''
Welcome to Gavel.

This is the judging system we’re using for **TAMU Datathon 2019**. 

**Please read this important message carefully before continuing.**

Gavel is a fully automated expo judging system that both tells you where to go
and collects your votes.

The system is based on the model of pairwise comparison. You'll start off by
looking at a single submission, and then for every submission after that,
you'll decide whether it's better or worse than the one you looked at
**immediately beforehand**.

If at any point, you can't find a particular submission, you can click the
'Skip' button and you will be assigned a new project. **Please don't skip
unless absolutely necessary.**

Gavel makes it really simple for you to submit votes, but please think hard
before you vote. **Once you make a decision, you can't take it back**.
'''.strip()

DEFAULT_EMAIL_SUBJECT = 'TAMU Datathon Judging Info!'

DEFAULT_EMAIL_BODY = '''
Hi {name}!

Thank you for being a judge for TAMU Datathon 2019!

You'd be judging teams in the Learner track. The judging system works on pairwise judging, you'll get more information about it when you go to the link below.

Below is the magic link for you to access the judging system. Please DO NOT share this with others, it's your personal link.

To access the judging system, visit this link: {link}.

Please make sure to read the welcome message and instructions before you continue.

Happy judging!

- TAMU Datathon Team
'''.strip()

DEFAULT_CLOSED_MESSAGE = '''
The judging system is closed for now. 

If you’ve already finished judging all your teams, you’re done!
'''.strip()

DEFAULT_CLOSING_MESSAGE = '''
Gavel judging is in the process of shutting down. Please wait.
'''.strip()

DEFAULT_DISABLED_MESSAGE = '''
Your account is currently disabled. Reload the page to try again.
'''.strip()

DEFAULT_LOGGED_OUT_MESSAGE = '''
You are currently logged out. Open your magic link to get started.
'''.strip()

DEFAULT_WAIT_MESSAGE = '''
Seems like the system is having issues assigning you new teams. Please reload the page in a minute.

If you’ve looked at all the teams already, then you’re done judging!
'''.strip()
