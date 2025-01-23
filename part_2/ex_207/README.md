**Exercise 2.07**

 Run a Postgres database and save the Ping-pong application counter into the database.

The Postgres database and Ping-pong application should not be in the same pod. A single Postgres database is enough and it may disappear with the cluster but it should survive even if all pods are taken down.