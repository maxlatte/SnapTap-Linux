import evdev
from evdev import ecodes
import sys

# Ensure this is your correct event node
DEVICE_PATH = '/dev/input/event6' 

try:
    kbd = evdev.InputDevice(DEVICE_PATH)
    # We create the virtual keyboard with ALL capabilities of the real one
    ui = evdev.UInput.from_device(kbd, name='snap-tap-virtual')
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

print(f"Snap Tap active on: {kbd.name}")

held_a = False
held_d = False

with kbd.grab_context():
    for event in kbd.read_loop():
        # Only intercept Keyboard Keys
        if event.type == ecodes.EV_KEY:
            
            # 1. Track physical state
            if event.code == ecodes.KEY_A:
                held_a = (event.value != 0)
            if event.code == ecodes.KEY_D:
                held_d = (event.value != 0)

            # 2. Snap Tap Logic for A and D
            if event.code == ecodes.KEY_A:
                if event.value == 1: # Press
                    ui.write(ecodes.EV_KEY, ecodes.KEY_D, 0)
                    ui.write(ecodes.EV_KEY, ecodes.KEY_A, 1)
                elif event.value == 0: # Release
                    ui.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
                    if held_d: ui.write(ecodes.EV_KEY, ecodes.KEY_D, 1)
                ui.syn()

            elif event.code == ecodes.KEY_D:
                if event.value == 1: # Press
                    ui.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
                    ui.write(ecodes.EV_KEY, ecodes.KEY_D, 1)
                elif event.value == 0: # Release
                    ui.write(ecodes.EV_KEY, ecodes.KEY_D, 0)
                    if held_a: ui.write(ecodes.EV_KEY, ecodes.KEY_A, 1)
                ui.syn()

            # 3. CRITICAL: Pass through every other key (Enter, W, S, etc.)
            else:
                ui.write_event(event)
                ui.syn()
        
        # 4. Pass through non-key events (Sync, LEDs, etc.)
        else:
            ui.write_event(event)
            ui.syn()
