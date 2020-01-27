container_id=$(docker ps | grep web | cut -f1 -d" ")
 
docker stop $container_id 
