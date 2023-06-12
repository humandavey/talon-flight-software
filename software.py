import curses, time
from curses.textpad import rectangle
from curses import wrapper

def eject_chute():
    pass
    # send 5v to ignite pyro charges

def get_data():
    pass
    # save & analyze incoming data

def main(window):

    armed = False
    confirm_eject = False
    eject_time = 1326194273874629
    eject = False

    window.nodelay(True)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_ON_BLACK = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    RED_ON_BLACK = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    YELLOW_ON_BLACK = curses.color_pair(3)
    
    option = "0"

    while True:

        get_data()

        # Get key presses
        try:
            key = window.getkey()
        except:
            key = None

        if key != None and (key == "1" or key == "2" or key == "3" or key == "4" or key == "0"):
            option = key

        if time.time() - eject_time > 3:
            eject = False
        
        # Option selection
        if key != None and key == " " and option != "0":
            # 1> ARM VEHICLE
            if option == "1" and not eject:
                armed = True
            
            # 2> DISARM VEHICLE
            if option == "2":
                armed = False
            
            # 3> TEST EJECTION CHARGE
            if option == "3" and confirm_eject and not eject:
                confirm_eject = False
                eject_time = time.time()
                eject = True
                eject_chute()
            elif confirm_eject and option != "3":
                confirm_eject = False
            elif option == "3" and not armed and key == " " and not eject:
                confirm_eject = True

            # 4> SHUTDOWN
            if option == "4":
                print("Talon Software closed.")
                break

        # Put text on terminal screen
        window.clear()

        window.addstr(0, 0, """┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          ___________       __                    _________       _____  __                                         ┃
┃          \__    ___/____  |  |   ____   ____    /   _____/ _____/ _____/  |___  _  ______ _____________            ┃
┃            |    |  \__  \ |  |  /  _ \ /    \   \_____  \ /  _ \   __\\\\   __\ \/ \/ \__  \\\\_  __ _/ __ \           ┃ 
┃            |    |   / __ \|  |_(  <_> |   |  \  /        (  <_> |  |   |  |  \     / / __ \|  | \\\\  ___/           ┃
┃            |____|  (______|____/\____/|___|__/ /_________/\____/|__|   |__|   \/\_/ (______|__|   \_____>          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
        
        window.addstr(10, 22, "72°F")
        window.addstr(10, 58, "180ft")
        window.addstr(10, 95, "1atm")

        rectangle(window, 17, 9, 19, 21)

        window.addstr(18, 10, "  Options")

        window.addstr(20, 10, "1> Arm Vehicle")
        window.addstr(21, 10, "2> Disarm Vehicle")
        window.addstr(22, 10, "3> Test Ejection")
        window.addstr(23, 10, "4> Shutdown")

        window.addstr(16, 72, "Vehicle Status")
        rectangle(window, 17, 50, 23, 106)

        # Update status message
        if armed:
            window.addstr(18, 59, "   _____                            ___")
            window.addstr(19, 59, "  /  _  \_______  _____   ____   __| _/")
            window.addstr(20, 59, " /  /_\  \_  __ \/     \_/ __ \ / __ | ")
            window.addstr(21, 59, "/    |    |  | \|  Y Y  \  ___// /_/ | ")
            window.addstr(22, 59, "\____|____|__|  |__|_|__/\___  \_____|")
        elif confirm_eject:
            window.addstr(18, 52, "___________    __              __   __")
            window.addstr(19, 52, "\_   _____/   |__| ____  _____/  |_|__| ____   ____")
            window.addstr(20, 52, " |    __)_    |  _/ __ _/ ___\   __|  |/  _ \ /    \\")
            window.addstr(21, 52, " |        \   |  \  ___\  \___|  | |  (  <_> |   |  \\")
            window.addstr(22, 52, "/_________/\__|  |\_____\_____|__| |__|\____/|___|__/")
            window.addstr(23, 52, "────────────\_____|")
        elif eject:
            window.addstr(18, 62, "___________    __              __ ")
            window.addstr(19, 62, "\_   _____/   |__| ____  _____/  |_")
            window.addstr(20, 62, " |    __)_    |  _/ __ _/ ___\   __|")
            window.addstr(21, 62, " |        \   |  \  ___\  \___|  |")
            window.addstr(22, 62, "/_________/\__|  |\_____\_____|__|")
            window.addstr(23, 62, "────────────\_____|")
        else:
            window.addstr(18, 51, "_______   __                                        ___")
            window.addstr(19, 51, "\____  \ |__| __________ _______  _____   ____   __| _/")
            window.addstr(20, 51, " |  |\  \|  |/  ___\__  \\_  __ \/     \_/ __ \ / __ | ")
            window.addstr(21, 51, " |  |/   |  |\___ \ / __ \|  | \|  Y Y  \  ___// /_/ | ")
            window.addstr(22, 51, "/_______/|__/______(______|__|  |__|_|__/\___  \_____|")

        # Make selection green
        if option != "0":
            window.addstr(19 + int(option), 10, str(option) + ">", GREEN_ON_BLACK)
        
        # Update ejection test message
        if confirm_eject:
            window.addstr(22, 10, "3> Press [SPACE] to confirm test", RED_ON_BLACK)
        elif eject:
            window.addstr(22, 10, "3> Ejection in progress", YELLOW_ON_BLACK)

        window.refresh()


if __name__ == "__main__":
    print("Starting Talon Software...\n")
    wrapper(main)
