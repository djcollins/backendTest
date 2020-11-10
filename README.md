# Backend Engineering test - Daniel Collins

## What did I think about the task?

With new applications and frameworks the biggest hurdle is usually the setup. And naturally, that's what happened this time.
I eventually found a tutorial that mentioned the main checkpoints in creating and running an application on Docker. I just had to 
fill in the blanks where steps and instructions were left out.

The next trickiest part was "3) A function that decodes a given string previously encoded", because I couldn't figure out how to let the user input bytes via console. So I changed the function that encodes given strings to also save the string version of the encoded string in a dictionary. This allows the user to enter a "string" of bytes, which will then be mapped to the actual bytes, which is passed into the decoding function, to produce the original string. This seemed like a faster solution than a configuration that allows the user to input bytes. 


Allowing the user to input bytes without errors being thrown left right and center requried me to make a dictionary where the string value of the bytes mapped to the byte value of bytes? Does this make sense?
