#!/bin/bash
yum update -y
sudo yum install httpd -y
sed -i 's/Listen 80[[:space:]]*$/Listen 8080/' /etc/httpd/conf/httpd.conf

cat <<'END_HTML' > /var/www/html/index.html
<!DOCTYPE html>
<html>
        <body>
            <h1>Hello World!</h1>
            <p>DB address: ${db_address}</p>
            <p>DB port: ${db_port}</p>
        </body>
</html>
END_HTML

sudo systemctl enable httpd
sudo systemctl restart httpd