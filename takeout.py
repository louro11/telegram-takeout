import os, datetime
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChat, MessageMediaPhoto, MessageMediaDocument
import html
import asyncio

# Steps to get necessary account data
# Go to: https://my.telegram.org/auth
# After receiving the code on the target phone
# Go to: API development tools (https://my.telegram.org/apps) 
# Get the API_ID and the API_HASH



async def download_media(message, folder_path):
    media_name = ''
    if message.media:
        media = message.media
        if isinstance(media, MessageMediaPhoto):
            photo = media.photo
            media_name = f'photo_{message.id}.jpg'
            await client.download_media(photo, file=os.path.join(folder_path, media_name))
        elif isinstance(media, MessageMediaDocument):
            document = media.document
            media_name = f'document_{message.id}'.format(document.mime_type.split('/')[-1])
            await client.download_media(document, file=os.path.join(folder_path, media_name))
    return media_name


async def save_all_messages_to_html(chat_limit=10, message_limit=20):
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Enter the code: '))

    async for dialog in client.iter_dialogs():

        chat_entity = dialog.entity
        chat_id = dialog.id
        chat_title = dialog.title
         
        # Use username if available, otherwise fallback to the title
        #chat_title = chat_entity.username# or str(chat_entity.title)


        # Retrieve messages from the chat
        messages = await client.get_messages(chat_id, limit=message_limit)

        # Save messages to an HTML file for each chat
        filename = f'{chat_title.replace(" ", "_").lower()}_conversation.html'

        with open(os.path.join(export_dir, filename), 'w', encoding='utf-8') as html_file:
            html_file.write(f'<html><head><title>{chat_title} Conversations</title></head><body><ul>')

            for message in messages:
                media_name = await download_media(message, export_dir)
                html_file.write(f'<li><b>{html.escape(chat_title) + " (" + html.escape(str(message.sender_id)) + ") [" + html.escape(str(message.date)) +"]"}</b>: {message.text}</li>')
                if media_name:
                    html_file.write(f'<br><i>{html.escape(media_name)}</i>')
                html_file.write('</li>')

            html_file.write('</ul></body></html>')

    await client.disconnect()



async def save_chat_messages_to_html(chat_id):
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Enter the code: '))


    chat_entity = chat_id
    chat_title = chat_id
     
    # Use username if available, otherwise fallback to the title
    #chat_title = chat_entity.username# or str(chat_entity.title)


    # Retrieve messages from the chat
    messages = await client.get_messages(chat_id)

    # Save messages to an HTML file for each chat
    filename = f'{chat_title.replace(" ", "_").lower()}_conversation.html'

    with open(os.path.join(export_dir, filename), 'w', encoding='utf-8') as html_file:
        html_file.write(f'<html><head><title>{chat_title} Conversations</title></head><body><ul>')

        for message in messages:
            media_name = await download_media(message, export_dir)
            html_file.write(f'<li><b>{html.escape(chat_title) + " (" + html.escape(str(message.sender_id)) + ") [" + html.escape(str(message.date)) +"]"}</b>: {message.text}</li>')
            if media_name:
                html_file.write(f'<br><i>{html.escape(media_name)}</i>')
            html_file.write('</li>')

        html_file.write('</ul></body></html>')

    await client.disconnect()

if __name__ == "__main__":

    #Ask the user if he wants to export ALL chats or just a particular one
    print("Telegram chat takeout, please type the number (the order) of the chat you would like to export. Type ALL to export all chats (it may take a while))")
    chat_id = input("Chat name: ")

    #Read config file
    with open("config.txt", "r", encoding="utf-8") as config:
        line = config.readline()
        values = line.split('"')
        api_id = values[1]

        line = config.readline()
        values = line.split('"')
        api_hash = values[1]

        line = config.readline()
        values = line.split('"')
        phone_number = values[1]

    client = TelegramClient('session_name', api_id, api_hash)
    export_dir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    os.makedirs(export_dir)
    if chat_id == 'ALL':
        asyncio.run(save_all_messages_to_html(chat_limit=10, message_limit=20))
    else:
        asyncio.run(save_chat_messages_to_html(chat_id))    
