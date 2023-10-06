from sty import fg, Style, RgbFg, rs, ef
from datetime import datetime as dt
from colorama import Style as st
from colorama import Fore
from datetime import date
import requests as rq
import socket as so
import datetime
import json
import os

class tools:
  class discord:
    class webhook:
      def send(webhook_url, message):
        msg_str = str(message)
        payload = {
          "content": msg_str
        }
        json_data = json.dumps(payload)
        hdrs = {"Content-Type": "application/json"}
        response = rq.post(webhook_url, data=json_data, headers=hdrs)
        if response.status_code == 204:
          print("Webhook message successfully sent.")
        else:
          print(f"Error sending webhook message. (status code: {response.status_code}")
  # -------------------------------------------------------------
  def reverse(text: str):
    reversed_text = text[::-1]
    return reversed_text
  # --------------------------------------------------
  class replit:
    class secrets:
      def get(secret_name: str):
        secret = os.environ[f'{secret_name}']
        return secret
  # ------------------------------------------------------
  class time:
    def current_time():
      now = dt.now()
      current_time = now.strftime("%H:%M:%S")
      return current_time
    # ---------------------------------------------
    def current_hour():
      now = dt.now()
      current_time = now.strftime("%H")
      return current_time
    # -----------------------------------------------
    def current_minute():
      now = dt.now()
      current_time = now.strftime("%M")
      return current_time
    # ----------------------------------------
    def current_second():
      now = dt.now()
      current_time = now.strftime("%S")
      return current_time
    # ----------------------------------------------
    def wait(time: int):
      start_time = datetime.datetime.now()

      target_time = start_time + datetime.timedelta(seconds=time)

      while datetime.datetime.now() < target_time:
        pass

      return
  # ----------------------------------------------
  class date:
    def current_date():
      today = date.today()
      res = today.strftime("%m/%d/%y")
      return res
    # ----------------------------------------
    def current_month():
      today = date.today()
      res = today.strftime("%B")
      return res
    # -------------------------------------
    def current_day():
      today = date.today()
      res = today.strftime("%A")
      return res
    # --------------------------------------
    def current_year():
      today = date.today()
      res = today.strftime("%Y")
      return res
  # ------------------------------------------
  class pc:
    def get_hostname():
      hostname = so.gethostname()
      return hostname
    # -------------------------------------------
    def get_ip():
      hostname =so.gethostname()
      ip = so.gethostbyname(hostname)
      return ip
    # -------------------------------------------
    class commands:
      def cmd(command: str):
        os.system(command=command)
  # -------------------------------------------
  class math:
    add = lambda num1, num2: int(num1) + int(num2)
    # ----------------------------------------------
    subtract = lambda num1, num2: int(num1) - int(num2)
    # ----------------------------------------------
    multiply = lambda num1, num2: int(num1) * int(num2)
    # ----------------------------------------------
    divide = lambda num1, num2: int(num1) / int(num2)

class text:
  class color:
    def red(text):
      red_text = Fore.RED + str(text) + st.RESET_ALL
      return red_text
    # -----------------------------------------------------
    def orange(text):
      fg.orange = Style(RgbFg(255, 150, 50))
      orange_text = fg.orange + str(text) + fg.rs
      return orange_text
    # --------------------------------------------------
    def yellow(text):
      yellow_text = Fore.YELLOW + str(text) + st.RESET_ALL
      return yellow_text
    # -------------------------------------------------------
    def green(text):
      green_text = Fore.GREEN + str(text) + st.RESET_ALL
      return green_text
    # -----------------------------------------------------
    def blue(text):
      blue_text = Fore.BLUE + str(text) + st.RESET_ALL
      return blue_text
    # -----------------------------------------------------
    def purple(text):
      fg.purple = Style(RgbFg(227, 16, 255))
      purple_text = fg.purple + str(text) + fg.rs
      return purple_text
    # -----------------------------------------------
    def pink(text):
      fg.pink = Style(RgbFg(255, 126, 231))
      pink_text = fg.pink + str(text) + fg.rs
      return pink_text
    # -------------------------------------------------------
    def black(text):
      black_text = Fore.BLACK + str(text) + st.RESET_ALL
      return black_text
    # --------------------------------------------------------
    def white(text):
      white_text = Fore.WHITE + str(text) + st.RESET_ALL
      return white_text
    # --------------------------------------------------------
    def custom_rgb(R: int, G: int, B: int, text):
      fg.custom = Style(RgbFg(R, G, B))
      custom_text = fg.custom + str(text) + fg.rs
      return custom_text
  # -----------------------------------------------------
  class format:
    def italic(text):
      italic_text = ef.italic + str(text) + rs.italic
      return italic_text