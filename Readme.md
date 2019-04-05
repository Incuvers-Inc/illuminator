# Illuminator
LED Matrix illuminator for IRIS. Because, as any photographer will say, "good lighting is always needed to take a good picture."

## Hardware
- resistor network (one resistor per LED, 256 in total)
- 32x 74HC595 (for 256 outputs total)
- a dimming transistor for the fluorescence LED (5V PWM)
- a trigger transistor for the fluorescence LED (3.3V logic)
- a logic level shifter (four 3.3V -> 5V)
- capacitors to reduce kicks in current draw


### Power
The main power source will be used for the both illumination modules (matrix+ fluorescence LED). This can potentially blow the fuse is all of the components happen to be active at the same time. Luckily there is no requirement for them to simultaneously be active. The lighting flash is much shorter than the timescales for the environmental controls, so the latter can be disabled for the duration of the lighting flash. This must however be controlled by the software. Failure to account for this may result in a blown fuse.

### LED matrix
The fluorescence LED must first be disabled before the matrix LED is activated.

The LED matrix is driven by `74HC595` shift registers that can holds the state of up to 8 LEDs. The state of all the LED's must be first set before they are globally activated by grounding their shared `output_enable` pin.

#### Dimming
Global dimming is made possible with PWM on the `output_enable` input of the `74HC595`. All only one PWM signal is needed to dim the full matrix.

### Fluorescence LED
All the matrix LEDs must first be disabled before the fluorescence LED is lit.
The on/off state of the fluorescence LED is set from a single transistor.

#### Dimming
Dimming for the fluorescence LED is accomplished using the same PWM signal. In order for the matrix to stay off when the fluorescence LED is enabled, all the individual matrix LEDs must first be disabled.


### RPi interface
The RPi supplies inputs as the common PWM, fluorescence LED trigger, SPI for the matrix (three inputs) and of course a common ground.

Since the matrix is powered at 5V, the logic level (SPI and PWM) has to also be  shifted to 5V.

Since the fluorescence LED is trigger from a transistor, the logic level can stay at 3.3V.


## Software

### Illumination flash

The software must make sure that all the matrix LEDs are set to an `off` state after a pattern is finished flashing.
Iy may be good measure to be redundant and also do this before turning on the fluorescence LED.
The same goes for turning off the fluorescence LED before turning on the matrix.

### Power management

Since the LED's are powered from the main power source,
it is important to limit the total current draw from activated sub-components.
It is the software's responsibility to temporary disable components (heating/fans/valves) that could draw current for the duration of the illumination flash. Since this is rather short, it should cause any environmental noticeable disruptions.

NOTE: the activate camera sensor (and post processing) will also cause a short-lived power demand, consider reactivating the environmental subcomponents only after the image is processed.
