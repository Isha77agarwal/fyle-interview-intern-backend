### Building and Running Docker file

- Take a pull of docker image from docker hub.
```
docker pull ishaagarwal77/fyle-interview-intern-backend:latest
```

- Build and Run the container 

```
docker container run -d -p 7755:7755 ishaagarwal77/fyle-interview-intern-back
end
```

- The server has started on http://localhost:7755/

- Check the container running 

```
docker container ls
```

- Stop the container

```
docker container stop <container id>
```