# pyEvony

**evony.py**

A client for Evony Age II based on Python 2.7

The client only has the ability to login to an account and register an account on any Evony Age II server at the moment. After logging in or registering it adds the castle ids of all the cities in that accoun to a json file named Alts.json.

For already registered players, to initialize the client, use

    Client(server_name,email_address,password)
  
For players who already registered in another server and wants to login to a new server for the first time, you also have the option to set which state you want your account to be in, use

    Client(server_name,email_address,password,zone=zone_number)

For players not registered in evony, use

    Client(server_name,email_address,password,register=True)
    
    
**create.py**

It can be used to create accounts on a server and build the city to level 5 to colonize it and issuing commission quests. It used a script buildacc.txt which I have added as well. It supports the currrent version of Roboevony, v1.41. The first few lines of buildacc.txt will need to be edited before use.

Usage:-
    
    python create.py number_of_accounts server_name

To use create.py, the file roboevony.exe needs to be in the same folder as the rest of these files.

Currently, the file create.py will only run in Windows because there is a function in it which obtains the location of the SOL files for current location and its specific to windows only.
