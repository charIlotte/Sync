import pymem
import pymem.process
import keyboard
import time

dwForceJump = 0x52B8BFC
dwLocalPlayer = 0xDE7964
m_fFlags = 0x104


def main():
    pm = pymem.Pymem('csgo.exe')
    client = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll

    while True:
        if keyboard.is_pressed('end'):
            exit(0)

        if keyboard.is_pressed('space'):
            force_jump = client + dwForceJump
            player = pm.read_int(client + dwLocalPlayer)
            on_ground = pm.read_int(player + m_fFlags)
            if player and on_ground and on_ground == 275:
                pm.write_int(force_jump, 5)
                time.sleep(0.08)
                pm.write_int(force_jump, 4)


if __name__ == '__main__':
    main()
