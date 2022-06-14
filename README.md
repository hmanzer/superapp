
# superapp


## Environment Variables for and flask-mysql in parent folder.

DB_PORT=<br>
DB_NAME=<br>
DB_HOST=<br>
MYSQL_ROOT_PASSWORD=<br>
MYSQL_DATABASE=<br>
MYSQL_USER=<br>
MYSQL_PASSWORD=<br>

### secret_mysql.yml <br>
```
---
apiVersion: v1
kind: Secret
metadata:
  name: mysql-secrets
type: Opaque
stringData:
  db_root_password: 
  database: 
  username: 
  password: 
  ```

 
## Docker-compose for development enviroment
run docker-compose up<br>
**This will bring up a multi-container environment for testing purposes.**<br>


## Screenshot

![This is an image](https://github.com/hmanzer/superapp/blob/main/customers_api/swagger_page.jpg)<br>
