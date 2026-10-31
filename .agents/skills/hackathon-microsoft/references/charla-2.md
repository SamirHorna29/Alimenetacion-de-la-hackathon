# Charla 2: Operación Bajo Presión

## Fuente y alcance

Archivo: `Charla 2 - Operacion Bajo Presion - Microsoft.pdf`.
Tamaño: 759 626 bytes; 25 páginas físicas.
SHA-256: `7c4109765cbc3fb11a65f5722d8a71ef9e317786527622d6ab56d166d96a202b`.

La portada identifica Hackathon COPA 2026, track Microsoft, charla 2, y presenta a Business IT como Partner Microsoft / Azure Expert MSP. Son declaraciones del documento; el nombre del archivo no acredita autoría editorial de Microsoft. El texto se extrajo y leyó completo con pdftotext; no se realizó una inspección visual completa de imágenes.

Esta charla es distinta de la sesión 2 de Dynatrace anunciada en el primer documento y aún no aportada. Contiene escenarios y orientaciones para el reto, pero no una rúbrica completa ni evidencia del entorno actual. Los hosts, horas, excepciones y estados de resolución de ejemplo no son observaciones reales del equipo.

## Mapa por página física

| Páginas | Tema | Aplicación |
| --- | --- | --- |
| 1–3 | Presentación, escenario posterior a Terraform y agenda. | Distinguir despliegue terminado de aplicación funcional. |
| 4–7 | Mentalidad SRE, primeros minutos y capas de evidencia. | Reproducir, recoger datos y evitar trabajo duplicado. |
| 8–12 | Señales, correlación, Azure Monitor y Application Insights. | Elegir evidencia y reconstruir la operación. |
| 13 | Consultas KQL para solicitudes, excepciones, traces y dependencias. | Usar esquema real, ventana y ámbito de recurso. |
| 14–16 | Síntomas y lectura de un 500/stack trace. | Separar excepción, contexto y causa. |
| 17–19 | URL frontend, contrato de integración y CORS. | Comparar solicitud real y configuración efectiva. |
| 20 | Errores en cascada, salud y preparación funcional. | Validar en capas después de cada cambio. |
| 21–23 | Método de seis pasos y ejemplo de CORS. | Detectar → Observar → Analizar → Hipótesis → Corregir → Validar. |
| 24–25 | Bitácora y cierre. | Conservar resultados y preparar respuestas sustentadas. |

La numeración impresa difiere desde la página física 17 (impresa 18). Las páginas físicas 22, 23 y 24 llevan 23, 25 y 26. El archivo pasa de Caso 1 a Caso 3; no se reconstruye una lámina ausente del Caso 2. Las variables se tratan en el mapa y en la bitácora, sin atribuirles una página no incluida.

## Qué conservar y qué precisar

- **Método y recuperación, pp. 5–6 y 22.** Usar hipótesis comprobables, un cambio evaluable por vez, responsabilidad por tarea y validación funcional. Si la validación falla, volver a observar. Cuando el alcance autorice mitigación urgente, un rollback respaldado puede restaurar servicio antes de conocer la causa definitiva: registrar mitigación y causa pendiente como estados distintos.
- **Silencio de telemetría, p. 7.** No demuestra que la petición nunca llegó al backend. Contrastar URL/red con instrumentación, ámbito, permisos, filtros, muestreo, retención e ingesta. La espera de 1–3 minutos de la p. 12 no es garantía universal. Fuentes: [ingesta](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-ingestion-time), [muestreo](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-sampling).
- **Correlación, pp. 10 y 16.** Usar `operation_Id` o `OperationId` observado en la telemetría y comprobar propagación. No asumir que un encabezado `x-ms-request-id` es ese mismo identificador. Las tablas/columnas varían entre Application Insights y workspace; una correlación solo reconstruye lo capturado. Fuente: [modelo de telemetría](https://learn.microsoft.com/en-us/azure/azure-monitor/app/data-model-complete).
- **Consultas, p. 13.** El título sobre resolver el 80 % de casos es una afirmación pedagógica sin evaluación aportada. `count()` cuenta filas; `severityLevel >= 2` incluye advertencias. El percentil depende de población y unidad: en workspace `DurationMs` está en milisegundos. Ver [consultas adaptadas](consultas-kql.md).
- **URL compilada, p. 17.** Inspeccionar framework, bundle y mecanismo de configuración. Algunos frontends fijan valores durante build; otros los cargan en runtime. Reconstruir solo cuando el valor esté incorporado al artefacto; comprobar también caché/versión servida. No imponer rebuild a todas las apps.
- **Contrato y estados, p. 18.** Comparar ruta, verbo, payload, tipo y esquema con la versión desplegada. Un 4xx/5xx no identifica por sí solo qué componente debe cambiar: proxies y gateways pueden emitirlo. Un 200 vacío puede ser válido; requiere datos esperados o un contrato que demuestre el defecto.
- **CORS, p. 19.** No toda petición usa preflight; la falta de OPTIONS no descarta CORS. Comparar solicitudes equivalentes y validar en navegador. CORS no sustituye autenticación. En App Service, confirmar qué capa responde; la configuración de plataforma tiene prioridad sobre la de la aplicación. Fuente: [CORS en App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-rest-api).
- **Salud y despliegue, pp. 20 y 23.** `/health`, `/health/deep` y `/api/status` son rutas del ejemplo, no endpoints garantizados. Confirmar código/contrato y dependencias críticas. No basta un HTTP 200 para validar la funcionalidad del reto. App Service no define una ruta por defecto: [Health Check](https://learn.microsoft.com/en-us/azure/app-service/monitor-instances-health-check). No todo cambio requiere redeploy de código; aplicar el mecanismo real de configuración y su validación.

Usa el [procedimiento de operación](operacion-bajo-presion.md) para aplicar estas ideas sin convertir los ejemplos del documento en requisitos universales.
