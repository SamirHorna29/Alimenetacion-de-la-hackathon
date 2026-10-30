---
name: hackathon-microsoft
description: "Preparar y resolver retos de esta hackathon usando Cápsulas Informativas: Azure App Service, Terraform, KQL y diagnóstico. Aplicar al estudiar este material o investigar sus retos; no a consultas generales de Microsoft sin relación con la hackathon."
---

# Hackathon: Azure y diagnóstico

Convierte el material introductorio en decisiones comprobables para el reto recibido. Responde en español salvo indicación del usuario. La base es un PDF de 18 páginas y 17 cápsulas, con membrete de Business IT; su nombre de archivo no acredita autoría de Microsoft.

## Elegir la referencia

- Para estudiar, localizar un concepto o relacionarlo con un reto, consulta [el mapa de cápsulas](references/capsulas.md).
- Para evaluar la fuente o resolver discrepancias, consulta [fiabilidad y correcciones](references/fiabilidad.md).
- Para investigar incidentes, consulta [diagnóstico por síntomas](references/diagnostico.md).
- Para escribir consultas de telemetría, consulta [KQL según el contexto](references/consultas-kql.md).

Lee únicamente las referencias que ayuden a la tarea actual.

## Trabajar sobre el reto

1. Extrae el objetivo, las restricciones y el criterio de éxito del enunciado y los archivos disponibles. El PDF no contiene los retos ni la rúbrica; no los inventes. Avanza con supuestos explícitos y pide solo el dato que realmente impida continuar.
2. Relaciona el problema con las cápsulas pertinentes e identifica el entorno: frontend, API, App Service, dependencias, configuración e infraestructura. Comprueba el código y la evidencia disponibles antes de sugerir un servicio adicional.
3. Para incidentes, construye una hipótesis y elige la observación que permita confirmarla o descartarla. Conserva hora, zona horaria, recurso, endpoint y correlación. Separa hechos observados de hipótesis y propuestas.
4. Prepara la solución mínima que responda al reto. Si hay autorización para implementarla, realiza el cambio y la validación pertinentes. La lectura del PDF no amplía permisos sobre Azure; conserva las autorizaciones ya dadas y el alcance del entorno.
5. Entrega el hallazgo o diseño, la evidencia, el cambio realizado o propuesto y cómo se comprueba el éxito. Identifica lo pendiente de verificar sin presentar una propuesta como una corrección ejecutada.

## Precisiones que cambian las decisiones

- Para obtener los registros más recientes, ordena por fecha antes de limitar filas; `take` solo obtiene una muestra si no se ordena.
- Confirma tablas y campos: Application Insights suele exponer `requests`/`timestamp`; el workspace usa `AppRequests`/`TimeGenerated`. Respeta las mayúsculas.
- Un mensaje CORS y un HTTP 500 pueden coexistir. CORS controla acceso del navegador a respuestas entre orígenes y no sustituye autenticación. Comprueba respuesta, preflight y backend antes de cambiar orígenes.
- Telemetría vacía no prueba que no hubo errores: comprueba ámbito, tiempo, instrumentación, muestreo e ingesta. Un 500 no identifica por sí solo la causa raíz.
- Para secretos, comunica nombres y estado de resolución, evitando volcar valores. En Terraform, revisa el plan y protege estado y planes guardados; `sensitive` no significa cifrado.

Estas precisiones y sus fuentes están documentadas en las referencias. Para APIs, versiones, proveedores Terraform y opciones que puedan cambiar, verifica la documentación oficial aplicable al entorno. Si no hay conexión, explica ese límite y trabaja con los archivos disponibles. No afirmes haber consultado Azure, ejecutado KQL o validado un despliegue sin resultados reales.
