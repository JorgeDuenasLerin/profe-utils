# Update ip

El router DIGI que tenemos es muy malo, se queda colgado y es incapaz de actualizar el DNS dinámico cuando se reinicia.

Aquí un cliente para freedns.afraid.org

## From https://www.ipify.org/

Request library:

```
pip3 install requests
```

Example:
```
from requests import get

ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))
```

