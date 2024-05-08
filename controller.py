import pyfirmata

comport = 'COM5'
board = pyfirmata.Arduino(comport)

relay_pins = {
    0: board.get_pin('d:13:o'),
    1: board.get_pin('d:12:o'),
    2: board.get_pin('d:11:o'),
    3: board.get_pin('d:10:o'),
    4: board.get_pin('d:9:o'),
    5: board.get_pin('d:8:o')  # Add more pins if needed
}

def relay(total):
    for pin in relay_pins.values():
        pin.write(1)  # Turn off all relays initially
    if total in relay_pins:
        relay_pins[total].write(0)  # Turn on the corresponding relay based on total finger count
