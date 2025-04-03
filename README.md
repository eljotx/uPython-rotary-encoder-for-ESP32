# uPython-rotary-encoder-for-ESP32
Simple software to operate a rotary encoder using interrupts.

## A bit of theory
Rotary encoders are usually simple mechanical-electrical devices constructed as two sliders with a set of contacts creating two channels usually called A and B. Due to the initial polarization at the A and B outputs, two rectangular signals are generated during the rotation of the encoder axis, shifted in phase by 90 degrees, in such a way that during the right movement, the falling (or rising) edge in channel A leads the falling (or rising) edge in channel B by 90 degrees, and during the left rotation it is the other way around and the falling (or rising) edge in channel B leads the falling (or rising) edge in channel A by 90 degrees.
This phenomenon can be used to detect events related to the encoder rotation and to determine its direction.
Usually, simple encoders have the ability to distinguish (resolution) from 20 to 50 events per revolution.
Counting the number of encoder pulses and their direction is complicated by transients that arise when the sliders in both channels contact the contact pads.
Additionally, some rotary encoders have a monostable switch installed that operates when a force is applied along the encoder axis. The proposed solution, despite its simplicity, proved to be very effective with little complication of the program code.

## How it works
The solution is based on the interrupt system in both channels operating on the ESP32 pins defined for the falling edge of the signal.
During the rotation clockwise and the falling edge in channel A, the interrupt subroutine checks whether the state of channel A is logical "0" and then checks whether the state in channel B corresponds to logical "1". In such a case, the subroutine counts the event as a positive pulse. Shortly afterwards, a falling edge will appear in channel B and the subroutine handling this event will check whether the value in channel B is actually "0" and will proceed to check the state of channel A where the signal will also have the value "0", which means that such a combination will not cause any further reaction.

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/enc21.jpg)

During counterclockwise rotation and a falling edge in channel B, the interrupt subroutine checks if the state of channel B is a logical "0" and then checks if the state in channel A corresponds to a logical "1". In this case, the subroutine counts the event as a negative pulse. Shortly afterwards, a falling edge will appear in channel A and the subroutine for this event will check if the value in channel A is actually "0" and will proceed to check the state of channel B where the signal will also have the value "0", which means that such a combination will not cause any further reaction.

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/enc31.jpg)

The encoder axis switch event handling also uses an interrupt on the associated input and only relies on ensuring that the switch has been pressed.

## Connection diagram
The encoder can be connected to any inputs acting as "INPUT" and handling interrupts. The RC circuits (10k + 4.7nF) shown in the diagram on the inputs for channels A and B are designed to filter the shortest interferences arising on the encoder contacts during its rotation. If the input for handling the axis switch does not have the PULL_UP function, this input should also be polarized using a 10-100k resistor to the 3.3V pin.

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/enc11.jpg)

## Practical notes
1. Since the program uses only the falling edges of signals in channels A and B, the effective resolution is twice as small as that which can be achieved for event detection for falling and rising edges of signals. However, it seems that this inconvenience is a small cost for the effect that is obtained with this method.
2. The program was tested for several encoders from two manufacturers.
3. The **tic** variable allows you to change the direction of the encoder's operation. Of the two types of encoders tested, both had different mechanics and in each of them the events in channels A and B occurred in reverse.
4. If the function of the axis switch should consist of a single operation while waiting for further program reaction, then you can disable the interrupt by unblocking the **#switch.irq(handler=None)** line. The program example contains the **#switch.irq(handler=switch_ch)** lines for interrupt procedures in channels A and B, binding the unblocking of the axis switch after the encoder has been activated, but these commands can be used in any other way.

## YouTube links
In english:  https://youtu.be/tAkmGXPD3jM 
In polish:   https://youtu.be/GxGLLQ3V2bo 
