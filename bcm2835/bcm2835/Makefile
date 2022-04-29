Relay_demo:Relay_demo.o
	gcc -Wall -o Relay_demo Relay_demo.o -lbcm2835
Relay_demo.o:Relay_demo.c
	gcc -Wall -c Relay_demo.c -lbcm2835

two: Relay_demo_2.o
	gcc -Wall -o Relay_demo_2 Relay_demo_2.o -lbcm2835
Relay_demo_2.o:Relay_demo_2.c
	gcc -Wall -c Relay_demo_2.c -lbcm2835

clean:
	rm Relay_demo.o Relay_demo Relay_demo_2.o Relay_demo_2
