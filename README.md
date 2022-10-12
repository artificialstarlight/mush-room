# mush-room
Chat server and client app.

# Usage

Run "pip install requirements.txt" in the folder. You must have pip and Python 3.x installed.

The mush-room-client.exe was meant for my instance of the server which was hosted using AWS. It was compiled from Python to .exe using PyInstaller, so some antiviruses may flag it as a false positive.

To run locally, run mush-server2.py. You can change the value of the variable using a text editor.

Then, run mush-room-client.py. Connect and enjoy!


# Features:
- Chat messaging using the terminal
- Command "!TRY ###" may be typed, where ### is any 3-digit number sequence. If the sequence is the same as the randomly generated one that occurs upon server startup, the client will be surprised with a bonus geomancy fortune-telling! (Just for fun). No consequence for incorrect sequences. Infinite guesses are allowed. 

# Features To Be Implemented:
- Colored text for each client username


