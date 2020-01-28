curl -i \
    -H "Accept: application/json" \
    -H "X-HTTP-Method-Override: PUT" \
    -X POST -d "id":3,"message":"Ryan login failed" \
    http://192.168.20.10:31287/systemlog/add
