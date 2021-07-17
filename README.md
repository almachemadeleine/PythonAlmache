[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5337634&assignment_repo_type=AssignmentRepo)
# Prueba Inicial - Red Social (Python)

## Pregunta Técnica:

Una plataforma de Red Social, permite las siguientes operaciones a sus usuarios: post, follows, re-post

La plataforma provee a los desarrolladores de aplicaciones, el siguiente API:

GET /[username]/followers

{ “user”: “username”,  “Followers”: [“user1”, “user2”,….. “user n”] }


GET /[username]/following

{ “user”: “username”,  “Following”: [“user1”, “user2”,….. “user n”] }


Implemente la función "calculateDistanceBetweenUsers", que calcule la distancia entre 2 usuarios.

##### Ejemplo practico:

Dado:

- { “user”: “userA”,  “Following”: [“userB”, “userD”,“userE”, "userG"] }
- { “user”: “userB”,  “Following”: [“userC”, “userJ”,“userI”, "userE"] }
- { “user”: “userC”,  “Following”: [“userM”, “userA”,“userJ”, "userI", "userZ"] }
- ...
- { “user”: “userZ”,  “Following”: [“userP”, “userN”, “userC”, "userJ", "userK"] }
     

Si requiero la distancia entre "userA" y "userM"

Al buscar se encuentra que: User A, sigue a User B. Y User B, sigue a User C. Y User C, sigue User M

Entonces, la primera distancia encontrada entre User A y User M, es: 3
 
#### Entradas sugeridas y Salidas esperadas:

En la plantilla (repositorio), al utilizar "python3 main.py [parámetros]" espera recibir parámetros de entrada con el siguiente formato:

- "[login usuario 1]" "[login usuario 2]"
- Ejemplo: "userA" "userM"
- El primer parámetro "[login usuario 1]" está siendo alojado en la variable 'initialUser'
- El segundo parámetro "[login usuario 2]" está siendo alojado en la variable 'finalUser'

Y se espera que el resultado de 'calculateDistanceBetweenUsers(initialUser,finalUser)' sea la distancia entre los nodos y sea asignada a la variable 'distance', cuya presentación se realiza de la siguiente manera:

- Distancia entre '[initialUser]' y '[finalUser]', es: [distance]
- Ejemplo: Distancia entre 'userA' y 'userM', es: 3

La función 'initializeSocialNetwork' es solo una muestra de como simular la red social, el uso o no de la misma queda a su criterio.

Además, el mensaje final impreso con 'print' debe mantenerse.


**CONSIDERAR:** Sabemos de la existencia de respuestas en internet para esta pregunta, pero deseamos conocer su capacidad analítica para la resolución de este problema. Esperamos que el candidato tenga buenas habilidades en desarrollo de algoritmos para que pueda trabajar con equipo técnico apropiadamente.
