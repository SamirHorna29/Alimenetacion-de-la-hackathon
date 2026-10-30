# Diagnóstico aplicado a los retos

Guía derivada de las cápsulas 5, 9–17. Los casos son posibilidades de diagnóstico; no describen retos confirmados de la hackathon.

## Recorrido y evidencia

Ubica el trayecto observado: navegador o cliente → frontend → API/backend → dependencias. Añade App Service, configuración e IaC donde intervengan. Para una solicitud fallida, registra recurso y slot, endpoint y método, hora con zona horaria, estado esperado/observado e identificador de correlación cuando exista.

Normaliza la ventana a UTC para compararla con telemetría, conservando la hora original. Revisa cambios recientes solo cuando haya una relación temporal plausible.

## Elegir la siguiente comprobación

| Síntoma | Primera comprobación útil | Cómo interpretar la evidencia |
| --- | --- | --- |
| Pantalla sin datos o error de consola | URL que usa el frontend y solicitud en Network. | Separar fallo del cliente, estado HTTP, conectividad y restricción del navegador. |
| “CORS” en el navegador | Origen exacto, método, cabeceras, respuesta y `OPTIONS` si hubo preflight. | La consola puede ocultar un error del backend. Comparar la operación equivalente fuera del navegador; clientes como curl no aplican la política CORS. |
| HTTP 500 | Solicitud y excepción/dependencia del mismo intervalo y operación. | El 500 acredita un fallo al atender la petición, pero requiere evidencia para atribuir causa. |
| 401 o 403 | Identidad, permisos y capa que emitió el estado. | No tratar un fallo de autenticación/autorización como problema de CORS. |
| Health Check no saludable | Ruta real, estado HTTP, redirecciones y dependencias críticas. | Aplicación iniciada no equivale a aplicación preparada para servir. |
| Variables ausentes o fallo tras despliegue | Nombres esperados, entorno/slot y estado de resolución. | Diferenciar ausencia, valor inválido y secreto inaccesible sin imprimirlo. |
| Telemetría vacía | Recurso/workspace, ventana, tabla, instrumentación e ingesta. | La falta de filas no confirma la ausencia de incidentes. |
| Error o diferencia en Terraform | Error exacto, versión/proveedor, configuración y plan. | Distinguir sintaxis, permisos, cuotas, estado, deriva y cambios de configuración. |

## CORS junto con un 500

Si el navegador muestra CORS y la operación equivalente devuelve 500 fuera del navegador, investiga primero el recorrido de atención en el servidor e identifica qué capa emitió ese estado; una capa intermedia también puede responder. Mantén como hipótesis separada una configuración CORS incorrecta. Comprueba método, cuerpo y autenticación al comparar solicitudes: un GET sin credenciales no equivale a un POST autenticado.

Determina qué capa genera los encabezados CORS. En App Service, revisa el efecto de su configuración frente a la del framework. Evita abrir todos los orígenes como corrección de prueba. Con credenciales, usa los orígenes concretos requeridos. La distinción entre solicitudes simples y preflight está descrita en [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) y el comportamiento de la plataforma en [App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-rest-api).

## Configuración, salud e infraestructura

En App Service, comparar nombres y slot evita corregir un entorno distinto. Obtener solo nombres cuando basten reduce exposiciones accidentales. Si se necesitan secretos, usa el mecanismo autorizado del proyecto. Documenta el estado de resolución sin copiar el valor. Las app settings se inyectan en el entorno y cambiarlas provoca reinicios: [configuración](https://learn.microsoft.com/en-us/azure/app-service/configure-common).

Para Health Check, confirma la ruta elegida, respuesta 2xx y comportamiento ante un fallo de dependencia crítica. La ruta de ejemplo `/health` no existe automáticamente. Considera autenticación y redirecciones según el diseño real; no elimines autenticación de toda la aplicación para resolver una comprobación de salud. Consulta [el comportamiento de App Service](https://learn.microsoft.com/en-us/azure/app-service/monitor-instances-health-check).

En Terraform, inspecciona los archivos del proyecto y el proveedor utilizado antes de recomendar comandos de versión específica. Distingue validación de configuración, planificación y aplicación. Si la tarea autorizada incluye un despliegue, revisa las creaciones, cambios, reemplazos y eliminaciones propuestos antes de aplicarlo dentro de ese alcance. Los planes guardados y el estado pueden contener secretos: [plan](https://developer.hashicorp.com/terraform/cli/commands/plan), [datos sensibles](https://developer.hashicorp.com/terraform/language/manage-sensitive-data).

## Evidencia de resolución

Repite la operación que falló, registra el resultado y compara el mismo recurso y ventana temporal. Comprueba además que la corrección no oculta el problema original: por ejemplo, un health endpoint que devuelve siempre 200 no demuestra que una dependencia se recuperó.

Presenta una nota proporcional al reto: síntoma, evidencia, hipótesis confirmada o pendiente, cambio, resultado de validación y siguiente comprobación. Cuando solo haya acceso al enunciado, entrega un plan de verificación con el resultado esperado de cada comprobación, sin inventar logs ni resultados.
