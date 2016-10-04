# pyEvony
A client for Evony Age II based on Python

The client only has the ability to login to an account and register an account on any Evony Age II server at the moment. After logging in or registering it adds the castle ids of all the cities in that accoun to a json file named Alts.json.

For already registered players, to initialize the client, use
  Client(server_name,email_address,password)
For players who already registered in another server and wants to login to a new server for the first time, you also have the option to set which state you want your account to be in, use
  Client(server_name,email_address,password,zone=zone_number)
For players not registered in evony, use
  Client(server_name,email_address,password,register=True)
  here zone_number is the number of the state where you want your account to be in.
