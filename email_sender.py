import smtplib
import time
import random
import pytz
import os
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from getpass import getpass
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

CYAN = Fore.CYAN + Style.BRIGHT
MAGENTA = Fore.MAGENTA + Style.BRIGHT
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
YELLOW = Fore.YELLOW + Style.BRIGHT
RESET = Style.RESET_ALL
CHECK = "✔️"
CROSS = "❌"

print(f"""
{GREEN}

  o__ __o__/_                                  o     o          o__ __o                                     o                          
 <|    v                                     _<|>_  <|>        /v     v\                                   <|>                         
 < >                                                / \       />       <\                                  < \                         
  |            \o__ __o__ __o      o__ __o/    o    \o/      _\o____          o__  __o   \o__ __o     o__ __o/    o__  __o   \o__ __o  
  o__/_         |     |     |>    /v     |    <|>    |            \_\__o__   /v      |>   |     |>   /v     |    /v      |>   |     |> 
  |            / \   / \   / \   />     / \   / \   / \                 \   />      //   / \   / \  />     / \  />      //   / \   < > 
 <o>           \o/   \o/   \o/   \      \o/   \o/   \o/       \         /   \o    o/     \o/   \o/  \      \o/  \o    o/     \o/       
  |             |     |     |     o      |     |     |         o       o     v\  /v __o   |     |    o      |    v\  /v __o   |        
 / \  _\o__/_  / \   / \   / \    <\__  / \   / \   / \        <\__ __/>      <\/> __/>  / \   / \   <\__  / \    <\/> __/>  / \       
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      
                                                                                            Human Simulator Email Sender - For Red Teamers V.1
                                                                                            By C0mm4nd1
{RESET}                                                  
""")

print(f"{YELLOW}📨 NOTE:{RESET} This script simulates human-like email sending behavior to bypass filters.")
print(f"{CYAN}🔐 DISCLAIMER:{RESET} This tool does not store credentials. All inputs are used only for this session.\n")
print(f"{MAGENTA}⚠️ It is recommended to warm up the domain to avoid SPAM filtering.")
print(f"{MAGENTA}⚠️ Invisible characters are randomly added to subject and body to bypass detection.\n")

sender = input("📬 \033[1mSender email\033[0m: ")
password = getpass("🔐 \033[1mPassword\033[0m: ")
smtp_server = input("🌐 \033[1mSMTP Server\033[0m (e.g. smtp.hostinger.com): ")
smtp_port = int(input("📮 \033[1mSMTP Port\033[0m (e.g. 587): "))
subject = input("📝 \033[1mEmail Subject\033[0m: ")
body = input("💬 \033[1mEmail Body\033[0m: ")

print(f"{MAGENTA}🗂️ Available recipient files in current directory:")
recipient_files = [f.name for f in Path('.').glob('*.txt')]
for idx, file in enumerate(recipient_files):
    print(f"   [{idx+1}] {file}")

while True:
    recipients_path_input = input("🔢 \033[1mEnter number or path of recipient file\033[0m: ").strip()
    if recipients_path_input.isdigit():
        index = int(recipients_path_input) - 1
        if 0 <= index < len(recipient_files):
            recipients_path = recipient_files[index]
            break
    elif os.path.isfile(recipients_path_input):
        recipients_path = recipients_path_input
        break
    print(f"{RED}Invalid selection. Please try again.{RESET}")

include_image = input("🖼️ Do you want to embed an image? (y/n) [y]: ").strip().lower() or 'y'
image_path = None
if include_image == 'y':
    print(f"{MAGENTA}🖼️ Available image files in current directory:")
    image_files = [f.name for f in Path('.').glob('*.png')]
    for idx, img in enumerate(image_files):
        print(f"   [{idx+1}] {img}")
    while True:
        image_choice = input("🔢 \033[1mEnter number or path of image file\033[0m: ").strip()
        if image_choice.isdigit():
            index = int(image_choice) - 1
            if 0 <= index < len(image_files):
                image_path = image_files[index]
                break
        elif os.path.isfile(image_choice):
            image_path = image_choice
            break
        print(f"{RED}Invalid selection. Please try again.{RESET}")
    print()  # newline after image selection

print(f"{MAGENTA}💡 The following delay simulates human-like behavior and avoids spam filters.")
print(f"{MAGENTA}💡 Recommended between 3 and 15 seconds.\n")
delay_min = int(input("⏱️ \033[1mMinimum delay\033[0m (seconds): "))
delay_max = int(input("⏱️ \033[1mMaximum delay\033[0m (seconds): "))
print()  # newline after max delay
print(f"{YELLOW}🚀 Sending...{RESET}")

with open(recipients_path, 'r') as f:
    recipients = [line.strip() for line in f if line.strip()]

timezone = pytz.timezone("America/Bogota")
def timestamp():
    return datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")

invisible_chars = ['\u200b', '\u200c', '\u200d']
subject_variants = ["", ".", random.choice(invisible_chars)]

success_count = 0
fail_count = 0
log_filename = f"logs_campaign_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
with open(log_filename, 'w') as log:
    for recipient in recipients:
        try:
            msg = MIMEMultipart('related')
            msg['From'] = sender
            msg['To'] = recipient
            variant = random.choice(subject_variants)
            msg['Subject'] = subject + variant

            invisible = random.choice(invisible_chars)
            html = f"""
            <html>
                <body>
                    <p>{body}{invisible}</p>
                    {f'<img src="cid:img123">' if image_path else ''}
                </body>
            </html>
            """
            alt = MIMEMultipart('alternative')
            alt.attach(MIMEText(html, 'html'))
            msg.attach(alt)

            if image_path:
                with open(image_path, 'rb') as img:
                    image = MIMEImage(img.read())
                    image.add_header('Content-ID', '<img123>')
                    image.add_header('Content-Disposition', 'inline', filename=os.path.basename(image_path))
                    msg.attach(image)

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender, password)
                server.send_message(msg)

            print(f"[{GREEN}{CHECK} {timestamp()}{RESET}] Sent to {recipient}")
            log.write(f"{timestamp()} - SENT - {recipient}\n")
            success_count += 1

        except Exception as e:
            print(f"[{RED}{CROSS} {timestamp()}{RESET}] Failed to {recipient}: {e}")
            log.write(f"{timestamp()} - FAIL - {recipient} - {e}\n")
            fail_count += 1

        time.sleep(random.randint(delay_min, delay_max))

print(f"\n{GREEN}✔️ Sent: {success_count} | {RED}❌ Failed: {fail_count}{RESET}")
print(f"🪵 Log saved as {log_filename}")
