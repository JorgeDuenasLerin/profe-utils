# Update ip

El router DIGI que tenemos es muy malo, se queda colgado y es incapaz de actualizar el DNS dinámico cuando se reinicia.

Aquí un cliente para freedns.afraid.org

Install:
```
sudo apt-get install python3-dnspython
```

## Cron

```
* * * * * $(cd /home/jorge/profe-utils/freedns-updater/;python3 update-afraid.py > last_execution.txt)
```
