MYSQL_HOST=$(kubectl get svc| grep mysql-systemlog-svc | awk '{print $3}')
MYSQL_PORT=3306
MYSQL_USER_ID=root
MYSQL_USER_PASSWORD=password1234

echo " -env MYSQL_HOST=$MYSQL_HOST -env MYSQL_PORT=$MYSQL_PORT --env MYSQL_USER_ID=$MYSQL_USER_ID --env MYSQL_USER_PASSWORD=$MYSQL_USER_PASSWORD"


docker run -it --env MYSQL_HOST=$MYSQL_HOST --env MYSQL_PORT=$MYSQL_PORT --env MYSQL_USER_ID=$MYSQL_USER_ID --env MYSQL_USER_PASSWORD=$MYSQL_USER_PASSWORD  testplayercom/web-app-systemlog:v3
