# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Glazier user interaction."""

import logging
import re
import time


def GetUsername():
  """Prompt the user for their username.

  Returns:
    The username string entered by the user.
  """
  username = False
  while not username:
    username = Prompt('Please enter your username: ',
                      validator='^[a-zA-Z0-9]+$')
  return username


def Keystroke(message, validator='.*', timeout=30):
  """Prompts the user for a keystroke and waits the specified amount of time.

  Args:
    message: the prompt message displayed to the user
    validator: a regular expression to validate any responses
    timeout: the length of time in seconds to wait for a response

  Returns:
    String of the character input from the user that matched input_regex.
  """
  import msvcrt  # pylint: disable=g-import-not-at-top
  print message
  i = 0
  kbhit = False
  while i < timeout and not kbhit:
    kbhit = msvcrt.kbhit()
    i += 1
    time.sleep(1)
  if kbhit:
    response = msvcrt.getch()
    result = re.match(validator, response)
    if result:
      logging.debug('Matched user input, %s, as a valid input.', response)
      return response
  logging.debug('No input from user prior to timeout.')
  return None


def Prompt(message, validator='.*'):
  """Prompt the user for input.

  Args:
    message: the prompt message displayed to the user
    validator: a regular expression to validate any responses

  Returns:
    a response string if successful, else None
  """
  response = raw_input(message)
  if not re.match(validator, response):
    logging.error('Invalid response entered.')
    return None
  return response
