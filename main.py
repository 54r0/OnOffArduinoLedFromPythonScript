import serial

microcontroller = serial.Serial("/dev/cu.usbmodem14101", 9600);

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    read_from_terminal()

    print("fine")

