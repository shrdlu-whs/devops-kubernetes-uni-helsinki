**Exercise 1.10**

 Split the "Log output" application into two different containers within a single pod:
One generates a new timestamp every 5 seconds and saves it into a file.
The other reads that file and outputs it with a hash for the user to see.
Either application can generate the hash. The reader or the writer.