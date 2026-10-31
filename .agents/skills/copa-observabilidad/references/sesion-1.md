# Sesión 1: base documental y correcciones

## Procedencia y alcance

Archivo local analizado: `Sesion 1 - Observabilidad Inteligente con Dynatrace.pdf`.
Tamaño: 1 888 371 bytes. SHA-256:
`dcf919091b92f45f4947005ee6bab2e6aa478b849d8426636a6b35467d06ca6c`.

Se extrajo y leyó el texto de las 21 páginas con pdftotext. Esta revisión no es una inspección visual completa de diagramas o imágenes. El PDF original permanece fuera del repositorio; estas notas son una síntesis, no una reproducción del documento. La vinculación con la hackathon de Copa procede de la petición del usuario; el documento no establece su rúbrica, retos ni acceso al entorno.

Se usa paginación física, comenzando por la portada. El orden impreso no siempre coincide: la página física 10 lleva 10 y la 11 lleva 09; la 13 lleva 13 y la 14 lleva 12. Citar la página física evita confundir estas secciones.

## Mapa del contenido

| Páginas físicas | Contenido | Aplicación al equipo |
| --- | --- | --- |
| 1–2 | Presentación y cuatro bloques. | Preparar la sesión, sin inventar un reto. |
| 3–5 | Monitoreo, observabilidad, logs/métricas/trazas y Grail. | Elegir señales complementarias según la pregunta. |
| 6–9 | Servidores, VMs, contenedores y Kubernetes. | Distinguir recursos y cambios de estado. |
| 10–11 | Vista Kubernetes y topología Smartscape. | Confirmar entidades y dependencias del entorno. |
| 12–14 | Servicios, cuatro señales de salud y PurePath. | Investigar latencia, errores, tráfico y saturación con límites de captura. |
| 15 | Ejemplo de checkout lento y dependencia de base de datos. | Aprender una secuencia de investigación; no trasladar la causa de ejemplo a otro incidente. |
| 16–19 | Logs, comandos DQL y errores por nodo/pod. | Consultar con tiempo, ámbito y campos comprobados. |
| 20–21 | Cierre y anuncio de sesión 2. | Seguridad, experiencia de usuario y negocio quedan anunciados, no desarrollados. |

## Precisiones operativas

1. **Captura de trazas, pp. 14 y 20.** La presentación afirma cobertura permanente sin muestreo. Dynatrace documenta Adaptive Traffic Management y reducción adaptativa de carga: puede haber transacciones no capturadas. No inferir tráfico total de un conteo de spans ni ausencia de fallos de una traza ausente. Fuentes: [ATM](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-saas-dps), [modelo de trazas](https://docs.dynatrace.com/docs/semantic-dictionary/model/trace).

2. **Descubrimiento automático, p. 12.** La instalación por sí sola no garantiza observar toda tecnología. Verifica runtime, versión, modo, reglas de inyección y propagación. Cuando conviven OneAgent y OpenTelemetry, comprueba duplicación y continuidad antes de habilitar otra captura. Fuentes: [soporte](https://docs.dynatrace.com/docs/ingest-from/technology-support), [modos](https://docs.dynatrace.com/docs/platform/oneagent/monitoring-modes/monitoring-modes), [OneAgent y OTel](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration).

3. **Causa raíz, pp. 15–16 y 19.** Una dependencia de 1,6 s localiza tiempo consumido; para afirmar que falta un índice hacen falta pruebas adicionales de consulta/plan y alternativas como bloqueos. Los logs pueden ser incompletos o registrar el síntoma. Una coincidencia temporal y un resultado de IA no sustituyen un mecanismo comprobado. Fuentes: [causa raíz](https://docs.dynatrace.com/docs/dynatrace-intelligence/root-cause-analysis/concepts), [límites de IA generativa](https://docs.dynatrace.com/docs/dynatrace-intelligence/agentic-and-generative-ai/dynatrace-generative-ai-overview).

4. **DQL, pp. 17–19.** Hay que elegir objeto y campos: `fetch logs` y `fetch spans` no convierten todas las señales en el mismo esquema. Las métricas temporales usan `timeseries`; `metrics` explora claves y dimensiones. Los selectores Classic y KQL de Azure no son DQL. Fuentes: [fuentes DQL](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/data-source-commands), [métricas DQL](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/metric-commands), [migración de selectores](https://docs.dynatrace.com/docs/platform/upgrade/preserve-metrics-and-service-visibility/metrics/metric-selector-conversion).

5. **Conteo por pod, p. 18.** El ejemplo agrupa registros de un namespace sin filtrar severidad aunque llama al resultado errores. Añade un criterio comprobado de error antes de contar. Un número de logs de error tampoco equivale a solicitudes fallidas: una solicitud puede generar varios registros.

6. **Kubernetes, pp. 8–10.** Las funciones descritas son capacidades, no evidencia de que un clúster tenga autoscaling, disponibilidad o recuperación configurados correctamente. No prometer despliegues sin cortes ni escalar por una imagen ilustrativa; inspeccionar configuración y eventos del caso.

Las precisiones son ampliaciones de esta revisión. Verifica documentación oficial vigente cuando la implementación dependa de versión, experiencia Classic/Grail o capacidades del tenant.
