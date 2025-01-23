**Exercise 5.06**

Install Knative Serving component to your k3d cluster.

For Knative to work locally in k3d you need to create it a cluster without Traefik:

$ k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2 --k3s-arg "--disable=traefik@server:0"

Next, try out the examples in Deploying a Knative Service, Autoscaling and Traffic splitting.