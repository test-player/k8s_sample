container_id=$(docker ps | grep web | cut -f1 -d" ")
 
docker exec -it $container_id  curl localhost:5000
