# mush-room
Chat server and client app.

# Usage
Client (.exe and mush-room-client.py) is configured for my server hosted with AWS. You may edit the port/IP address in the client side code to 8080/"localhost" (respectively) for the client to work with the server running locally.

To run locally, after changing value of variable "IP_address" in mush-room-client.py to "localhost" (quotes included), run mush-server2.py. You can change the value of the variable using a text editor.

Then, run mush-room-client.py. Connect and enjoy!


# Features:
- Chat messaging using the terminal
- Command "!TRY ###" may be typed, where ### is any 3-digit number sequence. If the sequence is the same as the randomly generated one that occurs upon server startup, the client will be surprised with a bonus geomancy fortune-telling! (Just for fun). No consequence for incorrect sequences. Infinite guesses are allowed. 

# Known Bugs
When multiple clients connect to the server and start chatting, messages/text may become overlapped client-side in the terminal. This is a work in progress and will be fixed sometime soon.

# Features To Be Implemented:
- Colored text for each client username
- Bugs fixed


