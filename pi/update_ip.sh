NAME=pi2
IP=`hostname -I  | tr -d ' '`
#http://pi-sauloal.c9.io/54628/log/pi2/172.18.38.93/
URL=http://pi-sauloal.c9.io/54628/log
curl "${URL}/${NAME}/${IP}/" &> /home/pi/update_ip.log
