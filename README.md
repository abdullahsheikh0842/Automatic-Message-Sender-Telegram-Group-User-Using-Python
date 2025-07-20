🚀 Python Telegram Marketing Automatic
Message Sender Script
Complete installation & deployment guide from zero

Full Setup Instructions
1️⃣ Install Python
Download and install Python 3.8 or higher: https://www.python.org/downloads/

Make sure to check “Add Python to PATH” during installation.

Verify installation by opening your terminal / command prompt and running:

python --version
2️⃣ Get Telegram API Credentials
Go to https://my.telegram.org/apps
Log in with your Telegram phone number.
Click “API development tools” and create a new application.
Fill in the required fields (App title, Short name, Platform can be “Other”).
After creation, you’ll get your api_id and api_hash.
Keep these credentials safe — you’ll need them for the script.
3️⃣ Prepare Your Telegram Account
Make sure the Telegram account you’ll use for this script has access to the target group or channel.
If needed, become admin in the target group/channel to fetch member list.
Your phone number must be accessible to receive Telegram login codes during script authentication.
4️⃣ Download Project Files
Download the bot script project files to your local PC.

5️⃣ Create requirements.txt
Create a file named requirements.txt in the project folder with this content:

telethon>=1.32.0
This will install the Telethon library needed to interact with Telegram API.

6️⃣ Install Dependencies
Open a terminal inside your project folder and run:

pip install -r requirements.txt
This installs the required Python packages.

7️⃣ Configure Your Script
Open draft_bot.py and update these variables with your info:

api_id: Your Telegram API ID from Step 2
api_hash: Your Telegram API hash from Step 2
phone: Your phone number including country code (e.g., +8801832483524)
group_username: The username of the target Telegram group or megagroup (without @)
8️⃣ Run the Script
Run the bot for the first time:

python draft_bot.py
You will be prompted to enter the Telegram login code sent to your Telegram app.

After login, the script will fetch the group members and create draft welcome messages.

9️⃣ Session File
After first login, a session.session file will be created in your project folder. This saves your login session.

Keep this file safe; it allows the script to run without logging in every time.

🔟 Running on cPanel (or any Hosting)
Most shared cPanel hosts don’t allow interactive Python scripts.
If your cPanel hosting supports Python apps and SSH access, you can upload your project files and session file.
Install dependencies via SSH:
pip install -r requirements.txt
Run the script with:
python draft_bot.py
If no SSH, run locally and upload the session file as needed (but script must run locally or on VPS for reliability).
Consider a VPS (like DigitalOcean, Linode, or free Oracle Cloud) for better control.
📋 Summary of Requirements
Python 3.8 or newer
pip (Python package installer)
Telethon Python library (pip install telethon)
Telegram API credentials (api_id & api_hash)
Telegram account with access to target group (admin recommended)
SSH access on server for deployment (recommended)
📝 Additional Tips
Never share your api_hash or session files publicly.
Follow Telegram’s Terms of Service to avoid account bans.
Test the script on a small test group before using on large groups.
You can customize the draft message inside the script to your preference.