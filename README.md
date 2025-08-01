### HecticPic 👉 https://hecticpic.vercel.app

Google Photos but I outsourced the servers to Discord because I’m cheap

![HecticPic Demo](https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif)

Google Photos said "15GB free, suck it"  so I hehe built this abomination:

    "Unlimited" storage (by exploiting Discord’s file uploads)

    8MB/image limit (Discord’s max file size)

    Zero server costs

Perfect for:

    Everyone

How It (Barely) Works
The Hack

    You upload a pic → Flask backend yeets it into a Discord channel via a bot

    Discord hosts it forever , URL gets saved in Firestore

    Frontend displays your Discord-hosted images 

Tech Stack

    Frontend	HTML/JS/CSS + Firebase	Looks legit, auth handled
    Backend	Python/Flask	
    Database	Firestore	Tracks Discord image CDN URLs


Setup
1. Create a Discord Bot

    Go to Discord Dev Portal

    Make a bot, invite it to your server with:

        messages.read

        attachments.write

    Note: Create a dedicated #image-dump channel (trust me)

2. Deploy the Crime

Backend (Railway):
Manual setup easy - env + github

Frontend (Vercel):
https://vercel.com/

💀 FAQ 
❓ Will Discord ban me?

Probably not, but:

    Don’t upload 10,000 pics/hour.

❓ Why not use AWS/S3?

Because:

    Free tiers expire → Discord is "free forever" (until it isn’t).

    Chaos is entertaining.

❓ Is this secure?

    Images are only visible to your bot/server.

    Firebase handles auth.

    No guarantees (this is a meme project).

⚠️ Legal-ish Disclaimer

    "This project is for educational purposes only. Discord’s TOS doesn’t explicitly forbid this (yet), but don’t @ me if they patch it. Use at your own risk."



Star the repo if you’d risk Discord’s wrath for unlimited storage.

License: WTFPL (Do What The Fuck You Want Public License)
Contribute: plis thenks
Shoutouts: Discord’s API team (pls don’t ban me).

