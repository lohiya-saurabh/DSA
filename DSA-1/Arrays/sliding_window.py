import time

# define window size
WINDOW_SIZE = 4

# define data to be sent
data = ['packet1', 'packet2', 'packet3', 'packet4', 'packet5',
        'packet6', 'packet7', 'packet8', 'packet9', 'packet10']

# initialize variables
base = 0
nextseqnum = 0
timer = time.time()

# loop until all packets have been sent and acknowledged
while base < len(data):
    # send packets within the window
    while nextseqnum < base + WINDOW_SIZE and nextseqnum < len(data):
        print('Sending packet:', data[nextseqnum])
        nextseqnum += 1

    # wait for acknowledgements
    while True:
        if time.time() - timer >= 1:
            print('Timeout')
            break

        # simulate receiving an acknowledgement
        if nextseqnum > base:
            print('Received ACK for packet:', data[base])
            base += 1
            timer = time.time()
            break
