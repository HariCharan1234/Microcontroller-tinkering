Just a desscription of the added programs :

microcontrollerRemote_IDE : A program that lets the user remotely add, read and run programs without any cable connection using WiFi. I understand that naming it as an "IDE" isn't
accurate and shows my inexperience so, I apologize if that, for whatever reason, makes someone upset.

mainloop.py : the reciever end program to recieve code from any connecting device that interprets commands sent by the client using microcontrollerRemote_IDE which is meant to be
on the microcontroller.

Note that while this does eliminate the requirement for frequently interrupting the task given to the microcontroller and essentially enabling the code to be changed at any moment
which could be valuable in projects where it is deisrable to not interrupt the task being performed by the microcontroller, it doesn't entirely eliminate the requirement for a
wired connection to make certain changes.

I look forward to any other applications where this code could help a fellow creator out, perhaps in applications where it's more feasible to connect to a seperate device and use
it's computing power instead of relying on the microcontroller's limited capabilities where a similar approach could be used.
