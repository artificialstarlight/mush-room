# mush-room
Chat server and client app.

# Usage
The mush-room-client.exe is meant for my instance of the server which is hosted using AWS. It was compiled from Python to .exe using PyInstaller, so some antiviruses may flag it as a false positive.

To run locally, run mush-server2.py. You can change the value of the variable using a text editor.

Then, run mush-room-client.py. Connect and enjoy!


# Features:
- Chat messaging using the terminal
- Command "!TRY ###" may be typed, where ### is any 3-digit number sequence. If the sequence is the same as the randomly generated one that occurs upon server startup, the client will be surprised with a bonus geomancy fortune-telling! (Just for fun). No consequence for incorrect sequences. Infinite guesses are allowed. 

# Known Bugs
When multiple clients connect to the server and start chatting, messages/text may become overlapped client-side in the terminal. This is a work in progress and will be fixed sometime soon.

# Features To Be Implemented:
- Colored text for each client username
- Bugs fixed


