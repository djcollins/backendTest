# Backend Engineering test - Daniel Collins

## What did I think about the task?
With new applications and frameworks the biggest hurdle is usually the setup. And naturally, that's what happened this time.
I eventually found a tutorial that mentioned the main checkpoints in creating and running an application on Docker. I just had to 
fill in the blanks where steps and instructions were left out, and to use other tutorials where this one produced errors (incorrect naming in command line instructions). 

It wasn't clear what to do with the docker image on the Windows Docker application, 
so I've excluded that from this repository, and just uploaded the code as requested. 

Overall this task was really interesting, learning about the new technologies used in the software field. 

## Pros and Cons of Nameko and Docker for Python Microservices
### The Pros
From the research I've done to complete this task, it seems like the main benifit of using this technology is the scalability of the services. 
Having an application consist of multiple microservices enables us to modify different features/services independently, without 
affecting other components that do not directly interact with it or depend on it. This also helps with cost efficiency for servers, 
since the microservice will only be replicated when required. 
Another benefit is that this service would run on any machine, since it resides in a container which does the rest of the work. 

### The Cons
Takes a while to set up. I found the documentation was lacking, it seems like quite a new technology. Nameko specifically, did not have too many tutorials or examples. 
I'm also using Windows, which is always a problem when it comes to development. 
Developers will have to ensure that updates are compatible with other microservices current versions. This could be a tricky task. 

## Decisions I made
I decided to import a huffman encoding package instead of creating one. After a few minutes of research into what it entailed I decided to follow the rule of 
"Dont recreate the wheel" and import dahuffman module from PyPi. 

One big decision here was to use the load_shakespear character encoding, since with Huffman compression, the more characters present, the longer the encoded symbols.
Since specials symbols should not appear often in communication between Microservice, this seemed appropriate. 

I thought I would keep the code structure as standard as possible. Using a dictionary to store my variables just made sense.
I also decided to make a dictionary that stored the byte encoded bytes of a string as a string, because for testing via console commands, it wasn't possible to input bytes as function paramaters via console. 

## How long did each part take
The coding took around 10 minutes, but planning the string-byte to byte dictionary took a 10 minutes on it's own, once I realised byte input into console wasn't a feasible approach. 
Learning about Dockers, Nameko, containers and Microservices took around 5 hours. 
Setting up environments and downloading everything needed took another hour or two. 
But writing this README was the most stressful part of the assignment, putting my thoughts onto a keyboard. 
Writing this document has taken me almost 3 hours. 


If I have left anything out or done anything blatantly incorrectly, Please let me know. If this could be considered an MVP of an assignment. 
