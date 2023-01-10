from pyrogram import Client, filters
import time
import config as cfg


client = Client("my_account", api_id=cfg.api_id, api_hash=cfg.api_hash)


@client.on_message(filters.command("start_spam", prefixes=['.']))
def start_spam(client, msg):
    iterations = msg.text[12:].split()[0]
    txt = msg.text[15:]
    for i in range(int(iterations)):
        time.sleep(0.25)
        client.send_message(msg.chat.id, txt)

if __name__ == "__main__":
    client.run()