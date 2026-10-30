# Mapa del PDF y aplicación a los retos

Fuente: `Capsulas Informativas - Microsoft.pdf`, 18 páginas. La página 1 presenta la secuencia; las páginas siguientes desarrollan las cápsulas. Paginación física del PDF, empezando por 1.

| Cápsula | Páginas | Conocimiento aportado | Uso al recibir un reto |
| --- | --- | --- | --- |
| 1. Microsoft Azure | 2 | Plataforma cloud y recursos bajo demanda. | Identificar qué recursos existen y cuáles requiere realmente el enunciado. |
| 2. Resource Group | 2–3 | Agrupación lógica de recursos relacionados. | Localizar el ámbito correcto y evitar confundir grupo, suscripción y aplicación. |
| 3. App Service | 3 | Alojamiento administrado de aplicaciones y APIs. | Distinguir código, configuración, runtime, slot y plan de alojamiento. |
| 4. API | 3–4 | Contrato para intercambiar información entre sistemas. | Revisar URL, método, datos, respuesta y autenticación de la operación afectada. |
| 5. Frontend y backend | 4–5 | Responsabilidades distintas conectadas por una API. | Dibujar el recorrido real de la solicitud y localizar dónde falla. |
| 6. DevOps | 5–6 | Cultura de colaboración, automatización y mejora continua. | Relacionar cambios y despliegues con síntomas; preparar una validación repetible. |
| 7. Infraestructura como código | 6–7 | Definición versionable de infraestructura. | Revisar diferencias entre configuración declarada y entorno observado. |
| 8. Terraform | 7 | Administración declarativa de infraestructura. | Examinar proveedor, versiones, backend, estado y plan del proyecto. |
| 9. Observabilidad | 7–8 | Logs, métricas y trazas para entender el sistema. | Elegir la señal que contraste una hipótesis; los logs no sustituyen todas las señales. |
| 10. Logs | 8–9 | Eventos que ayudan a reconstruir una operación. | Obtener tiempo, severidad y correlación sin exponer datos sensibles. |
| 11. KQL | 9–11 | Filtros, ordenación y agregación de telemetría. | Usar tablas del contexto real y acotar tiempo y recurso antes de analizar. |
| 12. Application Insights | 11–12 | Telemetría de solicitudes, excepciones y dependencias. | Comprobar instrumentación y correlacionar eventos de una operación. |
| 13. Excepciones y HTTP 500 | 12–15 | Señales de fallos internos durante una solicitud. | Buscar evidencia concreta; el código 500 no demuestra qué componente falló. |
| 14. CORS | 15–16 | Acceso entre orígenes desde un navegador. | Separar restricciones del navegador, autenticación y errores reales del backend. |
| 15. Health Check | 16–17 | Comprobación del estado operativo. | Revisar ruta, respuesta, dependencias críticas y configuración de App Service. |
| 16. Configuración | 17 | Parámetros externos al código para cada entorno. | Verificar nombres, slot, presencia y resolución de secretos. |
| 17. Diagnóstico | 17–18 | Observar, investigar, analizar, corregir y validar. | Justificar la corrección con evidencia y repetir la prueba original. |

## Cómo estudiar con esta base

La secuencia del documento es adecuada para aprender vocabulario desde cloud hasta diagnóstico. Para preparar un reto concreto, prioriza el recorrido de la petición y las señales observables; después profundiza en los recursos o herramientas implicados. No hace falta estudiar las 17 cápsulas en cada consulta.

Los ejemplos técnicos incrustados como imágenes también se revisaron. En particular, la página 10 muestra `requests | take 10` y `exceptions | take 10`; la página 11 muestra filtrado por severidad, ordenación por `timestamp` y conteo. Consulta las [correcciones](fiabilidad.md) y las [consultas adaptadas](consultas-kql.md) antes de reutilizarlos.

## Límites para la hackathon

El PDF anuncia conocimientos relacionados con los retos, pero no especifica problemas, entregables, puntuaciones, tecnologías obligatorias, credenciales, regiones, presupuesto ni permisos. Esos datos deben proceder del enunciado y de los organizadores. Una posible relación entre una cápsula y un fallo es una hipótesis de trabajo, no una predicción del reto.
