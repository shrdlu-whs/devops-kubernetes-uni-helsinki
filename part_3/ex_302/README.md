**Exercise 3.02**

 Deploy the "Log output" and "Ping-pong" applications into GKE and expose it with Ingress.
"Ping-pong" will have to respond from /pingpong path. This may require you to rewrite parts of the code.

Note that Ingress expects a service to give a successful response in the path / even if the service is mapped to some other path!