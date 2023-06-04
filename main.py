vexcode_brain_precision = 0
vexcode_console_precision = 0
myVariable = 0
runAmount = 0
opticVal = 0

def when_started1():
    global myVariable, runAmount, opticVal, vexcode_brain_precision, vexcode_console_precision
    optical_10.set_light(LedStateType.ON)
    optical_10.set_light_power(90, PERCENT)
    opticVal = 0
    runAmount = 0
    motor_19.set_position(0, DEGREES)
    motor_20.set_position(0, DEGREES)
    wait(2, SECONDS)
    while runAmount < 17:
        for repeat_count in range(10):
            opticVal = opticVal + optical_10.hue()
            wait(5, MSEC)
        opticVal = opticVal / 10
        brain.screen.print(opticVal, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        if opticVal < 32 and opticVal > 27:
            motor_19.spin_to_position(0, DEGREES, wait=True)
            wait(1, SECONDS)
            motor_20.spin_for(FORWARD, 60.5, DEGREES, wait=True)
            wait(0.5, SECONDS)
            opticVal = 0
        if opticVal < 37 and opticVal > 31:
            motor_19.spin_to_position(120, DEGREES, wait=True)
            wait(1, SECONDS)
            motor_20.spin_for(FORWARD, 60.5, DEGREES, wait=True)
            wait(0.5, SECONDS)
            opticVal = 0
