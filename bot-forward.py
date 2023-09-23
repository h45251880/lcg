#hai na
import telethon
api_id = 27334525
api_hash = '3dc8706c5f0f8f4abdcd0ab148585cc5'
client = telethon.TelegramClient('anon', api_id, api_hash)


@client.on(telethon.events.NewMessage)
async def my_event_handler(event):
    if 'vi_' in event.raw_text or 'p_' in event.raw_text or 'd_' in event.raw_text or 'pk_' in event.raw_text:
      if event.chat_id != 5612666796:
        logr = open("c1.txt", "r", encoding="gb18030")
        if event.raw_text in logr.read():
            print('匹配')
            logr.close()
        else:
            logr.close()
            print('不匹配，發送')
            await client.send_message('FilesDriveRobot', event.raw_text)
            await client.send_message('haha8784', event.raw_text)
            logw = open("c1.txt", "a", encoding="gb18030")
            logw.write(event.raw_text)
            logw.write('\n')
            logw.close
            

client.start()
client.run_until_disconnected()
