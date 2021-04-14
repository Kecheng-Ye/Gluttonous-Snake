from Game_component import *

def main():
    game = Glutonous_Snake(20, 20)
    game.start()


if __name__ == '__main__':
    main()
    # listener = Key_listener([None])
    # keyboard_signal = signal.signal(signal.SIGUSR1, signal_function)

    # listener.start()
    # while True:
    #     fool()
    #     time.sleep(0.1) 