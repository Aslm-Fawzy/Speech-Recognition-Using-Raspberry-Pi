

# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
welcome_text = """
     hello sir
         For Knowing Date : say (today)
         For Turn on Led : say (open)
         For Turn off Led : say (close)
         For Closing Program : say (exit)
      """
# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
welcome_obj = gTTS(text=welcome_text, lang=language, slow=False)

# Saving the converted audio in a mp3 
welcome_obj.save("../Records/welcome.mp3")
# Doing the same for turnining on Led
open_text = """
       Please Check if the led is Turned on or not
      """
open_obj = gTTS(text=open_text, lang=language, slow=False)
open_obj.save("../Records/open.mp3")

# Doing the same for turnining off Led
close_text = """
       Please Check if the led is Turned off or not
      """

close_obj = gTTS(text=close_text, lang=language, slow=False)
close_obj.save("../Records/close.mp3")


# Doing the same while exit from program
exit_text = """
      Ok Good Bye
      """

exit_obj = gTTS(text=exit_text, lang=language, slow=False)
exit_obj.save("../Records/exit.mp3")

# Doing the same while checking date
from datetime import date
date_text = str(date.today())

date_obj = gTTS(text=date_text, lang=language, slow=False)
date_obj.save("../Records/date.mp3")

