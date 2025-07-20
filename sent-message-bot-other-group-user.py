from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import asyncio

# Replace with your real credentials
api_id = 2125xxxx  # <<== Your api_id
api_hash = '3a1d75f6f880a6c64xxxxxx'  # <<== Your api_hash
phone = '+88018324xxxx'  # <<== Your phone number with country code
group_username = 'groupUsername'  # <<== Group username without @


client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start(phone=phone)

    group = await client.get_entity(group_username)

    offset = 0
    limit = 100
    all_participants = []

    while True:
        participants = await client(GetParticipantsRequest(
            channel=group,
            filter=ChannelParticipantsSearch(''),
            offset=offset,
            limit=limit,
            hash=0
        ))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)

    print(f"Total users: {len(all_participants)}")

    for user in all_participants:
        if user.bot or user.deleted:
            continue
        try:
            # Send private message to user (by user ID)
            await client.send_message(
                entity=user.id,
                message="Hello 👋 I wanted to personally welcome you!" #write your message here
            )
            print(f"Message sent to {user.id} @{user.username if user.username else ''}")
            await asyncio.sleep(1)  # to avoid flood limits
        except Exception as e:
            print(f"Failed to send message to {user.id}: {e}")

with client:
    client.loop.run_until_complete(main())
