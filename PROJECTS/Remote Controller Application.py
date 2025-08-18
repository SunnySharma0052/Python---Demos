import time
import random

class Remote_Controller():
    def __init__(self, TV_Status = "OFF", TV_Volume = "=", Channel_List = "BBC1", Channel_Name = "BBC1"):
    
       print("Creating a remote controller..")

       self.TV_Status = TV_Status
       self.TV_Volume = TV_Volume
       self.Channel_List = Channel_List
       self.Channel_Name = Channel_Name

    def TV_ON(self):
        
        if self.TV_Status == "ON":
            print("TV is already on...")

        else:
            self.TV_Status = "ON"
            print("TV is turning on...")
            

    def TV_OFF(self):
          
        if self.TV_Status == "OFF":
            print("TV is already off...")

        else:
            self.TV_Status == "OFF"
            print("TV is turning off...")
            

    def Volume_Adjustment(self):

        while True:

            Answer = input("Volume Down '-' \nVolume Up: '-' \nExit: 'exit'")


            if Answer == "-":

                if self.TV_Volume != 0:
                    self.TV_Volume -= 1
                    print("Volume: ", self.TV_Volume)
                
            elif Answer == "+":

                if self.TV_Volume != 50:
                    self.TV_Volume +=1
                    print("Volume: ", self.TV_Volume)

            else:
                print("The sound level has updated.")
                break

    def Add_Channel(self,Channel_Name):

        print("Adding channel...")
        time.sleep(1)

        self.Channel_List.append(Channel_Name)
        print("Channel added...")

    def Random_Channel(self):

        Random = random.randint(0,len(self.Channel_List)-1)

        self.Channel_Name = self.Channel_List[Random]

        print("You are watching now",self.Channel_Name)

    def __len__(self):
        return len(self.Channel_List)
    
    def _str_(self):
        return "TV Status: () \nChannel List () \nWatching Channel: ()".format(self.TV_Status,self.TV_Volume,self.Channel_List,self.Channel_Name)
    
Remote_Controller_1 = Remote_Controller()

print("""
      
1. Turn on TV
2. Turn off TV
3. Volume Adjusment
4. Add Channel
5. Number of Channels
6. Open Random Channel
7. TV Info
      
For exit press 0
      
""")

while True:

    Operation = input("Choose the operation you want: ")

    if Operation == "Q" or Operation == "q":
        print("Program is closing..")

    elif Operation == "1":
        Remote_Controller_1.TV_ON()

    elif Operation == "2":
        Remote_Controller_1.TV_OFF()

    elif Operation == "3":
        Remote_Controller_1.Volume_Adjustment()

    elif Operation == "4":

        Channel_Names = input("input channel names seperated by comas..")
        Channel_List = Channel_Names.split(",")
        for adding in Channel_List:
            Remote_Controller_1.Add_Channel(adding)

    elif Operation == "5":
        print("Number of Channel: ", len(Remote_Controller_1))

    elif Operation == "6":
        Remote_Controller_1.Random_Channel()

    elif Operation == "7":
        print(Remote_Controller_1)

    else:
        print("Invalid operation!")