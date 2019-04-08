import wiringpi
import time


class Illuminator(object):
    
    def __init__(self):
        wiringpi.wiringPiSetupGpio()

        # setup SPI
        self.channel = 0  # SPI_CE0  or GPIO 08 or Pin25
        self.speed = 500000 
        wiringpi.wiringPiSPISetup(self.channel, self.speed)
        # setup PWM 
        self.PWM_GPIO = 18 # the hardware PWM is GPIO_18 or pin 12
        wiringpi.pinMode(self.PWM_GPIO, 2) # the hardware PWM is on GPIO 18 
        self.brightness = 0
        self.set_brightness(self.brightness)

    def set_brightness(self, val):
        """ Set the global LED brightness (both for the matrix illuminator and the fluorescence)
        Args: val: integer 0-100% brightness
        
        """
        print(val)
        assert val<100, "Brightness value must be a value between 0-100"
        assert val>=0, "Brightness value must be a value between 0-100"
        MAX_DUTY_CYCLE = 1024
        duty_cycle = (100-val)*MAX_DUTY_CYCLE/100
        wiringpi.pwmWrite(self.PWM_GPIO, duty_cycle)

    def brightness_sweep(self):
        """ mainly for show
        """
        for i in range(0,100,1):
            self.set_brightness(i)
            time.sleep(0.005)

    def iterate_matrix(self, start=0, end=4):
        """ iterate LEDs on the matrix
        This is a debugging tool and will be removed
        """
        # turn off matrix while the pattern is set
        self.set_brightness(0)

        for num in range(start, end):
            send_byte = chr(2**num)
            wiringpi.wiringPiSPIDataRW(self.channel, send_byte)
            self.brightness_sweep()
            num += 1
        return
    def flash_pattern(self):
        pass
    def flash_phase_contrast(self):
        pass
    def flash_fluorescence(self):
        pass

if __name__=="__main__":
    illum = Illuminator()
    illum.iterate_matrix(end=8)
