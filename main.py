import serial

microcontroller = serial.Serial("/dev/cu.usbmodem14101", 9600);

from telethon import TelegramClient, events, sync

import requests


def read_from_terminal():
    # lettura del comando da input
    comando = "spegni"
    while comando != "esci":
        comando = input("Inserisci il comando accendi/spegni: ")
        print(comando)

        # invio del comando ad arduino
        microcontroller.write(comando.encode('ascii'))

    microcontroller.flush()
    microcontroller.close()

def read_from_telegram():

    TOKEN = "5544630619:AAE997m6LfflMbyAPFOnR6AbIctfDQNMA44"
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    # lettura comando da canale telegram
    #api_id =
    #api_hash =
    #client = TelegramClient('arduino', api_id, api_hash)

    #@client.on(events.NewMessage(chats='channel_name'))
    #async def my_event_handler(event):
    #    print(event.raw_text)

    #client.start()
    #client.run_until_disconnected()

    print(requests.get(url).json())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    read_from_terminal()


    print("fine")

