#include <bcm2835.h>
#include <stdio.h>

int main(int argc, char **argv) {
    
    uint8_t Relay[] = {5, 6, 13, 16, 19, 20, 21, 26};
    uint8_t i;

    if(!bcm2835_init())  {   //use BCM2835 Pin number table
        printf("bcm2835 init failed !\r\n");
        return 1;
    }
    printf("bcm2835 init success\r\n");
    //GPIO config
    for(i=0; i<8; i++)  {
        bcm2835_gpio_fsel(Relay[i], BCM2835_GPIO_FSEL_OUTP);
        bcm2835_gpio_write(Relay[i], HIGH);
    }
   
    while(1) {
      for(i=0; i<6; i++){
	if(i%2==0) {
	  bcm2835_gpio_write(Relay[1], LOW);
	}
	else {
	  bcm2835_gpio_write(Relay[1], HIGH);
	}
	if(i%3==0) {
	  bcm2835_gpio_write(Relay[2], LOW);
	}
	else {
	  bcm2835_gpio_write(Relay[2], HIGH);
	}
      	bcm2835_delay(300);
      }
    }
    return 0;
}
