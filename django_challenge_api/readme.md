##INSTALACION##

1) Tener Docker y docker compose instalados
2) Extraer los aliases del archivo aliases.txt, modificamos`APP_PATH` para que tenga la path a donde tengamos el proyecto y pegarlos en ~/.bashrc, para esto navegamos a home, `cd` y `nano .bashrc`, scroll hasta el final y lo pegan.
3) Abrimos otra consola o recargamos los aliases en la misma consola y corremos los siguientes comandos:
 (como no llegue  a hacer un dump y la logica que lo restaura cuando hacemos el setup, vamos a tener que crear el usuario a mano)
	- setup_app
	- sudo docker compose run  django_challenge_api sh -c "cd django_challenge_api && python3 manage.py createsuperuser"
	- start_app
(en caso de no levantar, start_app otra vez!)
Ahora si la API esta en 0.0.0.0:8000 o localhost:8000

La parte del middleware y el cliente no las llegue a hacer por falta de conocimiento y por no haber entendido del todo como se queria armar el sistema.
De todas formas seria la primera vez que armaba algo con esa estructura.
Tuve problemas tambien con setear celery en docker para tener la cola de crons que era otro requerimiento, pero es algo que en el dia a dia de mi trabajo se implementa.
En cuanto a las clases de permisos para el viewset deje la default (nada) porque al faltar los demas servicios ni me moleste, pero tenia en mente usar un sistema de public/private keys para identificacion de los servicios
