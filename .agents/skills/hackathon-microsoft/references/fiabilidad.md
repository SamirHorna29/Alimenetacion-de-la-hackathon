# Revisión de fiabilidad de las cápsulas

Revisión realizada el **30 de octubre de 2026**. Dictamen: **útil como introducción; requiere precisiones para usarlo como guía operativa**. Esta valoración es cualitativa, no una certificación ni una puntuación de exactitud.

## Identificación y procedencia

- Archivo revisado: `Capsulas Informativas - Microsoft.pdf`, 4 037 157 bytes, 18 páginas y 17 cápsulas.
- SHA-256: `04d1108c2779225ef4a0b2d12e4c978d83323eee75c37fb86e5cf219e00d576d`.
- El membrete visible dice **Business IT**.
- Los metadatos declaran autora **Carelys Echeverry**, creación el 16/07/2026 y modificación el 23/07/2026, ambas con zona `-05:00`.
- Microsoft Word para Microsoft 365 figura como programa productor. Esto identifica la herramienta utilizada, no acredita publicación ni revisión por Microsoft.
- En la revisión no se encontraron bibliografía ni enlaces de referencia en el texto o las anotaciones. No se ha autenticado la autoría institucional ni una firma criptográfica.

Se revisó el texto de las 18 páginas y se inspeccionaron los ejemplos y diagramas incrustados como imágenes. El documento tiene valor pedagógico; su procedencia debe describirse con los límites anteriores.

## Conceptos aprovechables

Las explicaciones de recursos, APIs, separación frontend/backend, IaC y diagnóstico ofrecen un vocabulario inicial coherente. Las siguientes fuentes primarias respaldan las bases relevantes:

| Base conceptual | Valoración | Contraste |
| --- | --- | --- |
| Resource Group como agrupación lógica de recursos | Correcta a nivel introductorio. | [Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) |
| App Service para alojar webs y APIs sin administrar la infraestructura subyacente | Correcta; esto no elimina las responsabilidades sobre código y configuración. | [App Service](https://learn.microsoft.com/en-us/azure/app-service/overview) |
| DevOps e IaC | Útiles; conviene entender DevOps como cultura y prácticas, sin reducirlo a una metodología rígida. | [DevOps](https://learn.microsoft.com/en-us/devops/what-is-devops), [IaC](https://learn.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code) |
| Terraform declarativo | Correcta como presentación de la herramienta. | [Qué es Terraform](https://developer.hashicorp.com/terraform/intro) |
| Observabilidad y Application Insights | Correctas como introducción a la telemetría de aplicaciones. | [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview) |

## Correcciones y ampliaciones necesarias

| Tema y ubicación | Evaluación | Aplicación práctica | Fuente primaria |
| --- | --- | --- | --- |
| “Últimas solicitudes” con `requests` y `take 10`, p. 10, imagen | Error en la interpretación del ejemplo: `take` no garantiza cuáles devuelve. | Ordenar por fecha descendente antes de limitar filas. | [Operador take](https://learn.microsoft.com/en-us/kusto/query/take-operator) |
| Tablas KQL, pp. 10–11 | El texto enumera nombres capitalizados; las imágenes usan minúsculas. Además, el esquema depende del contexto. | Confirmar `requests`/`timestamp` en Application Insights o `AppRequests`/`TimeGenerated` en workspace. `Metrics` no es una tabla genérica garantizada. | [Modelo de telemetría](https://learn.microsoft.com/en-us/azure/azure-monitor/app/data-model-complete) |
| KQL de solo lectura, p. 11 | Correcto para consultas; no debe extenderse a todas las operaciones de administración de Kusto. | Distinguir consultas y comandos de administración. | [KQL](https://learn.microsoft.com/en-us/kusto/query/) |
| CORS, pp. 15–16 | Simplificación que puede inducir a error: no es autorización de usuarios ni impide todo envío de solicitudes. | Revisar origen, respuesta y preflight cuando corresponda. Una petición simple puede llegar al servidor y su respuesta quedar inaccesible al código del navegador. | [CORS en MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) |
| Configurar CORS en App Service | Ampliación ausente en el PDF. | Elegir la capa responsable; no superponer sin análisis CORS de App Service y del framework. No combinar origen `*` con credenciales. | [CORS en App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-rest-api) |
| HTTP 500 y excepciones, pp. 13–15 | El significado general es correcto; el estado no identifica una causa concreta. | Correlacionar el fallo con registros, configuración y dependencias; no concluir automáticamente “servidor apagado” o “es CORS”. | [HTTP 500](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/500) |
| Captura automática de excepciones y telemetría, pp. 12–14 | Depende de instrumentación, runtime y configuración. No está garantizada para cada evento. | Verificar instrumentación e ingesta antes de interpretar ausencia de registros. | [Modelo de telemetría](https://learn.microsoft.com/en-us/azure/azure-monitor/app/data-model-complete) |
| Conteos de telemetría, p. 11 | `count` cuenta filas devueltas, no siempre el tráfico total. | Explicitar ventana y muestreo al comunicar cantidades. | [Muestreo](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-sampling), [Métricas](https://learn.microsoft.com/en-us/azure/azure-monitor/app/metrics-overview) |
| Health Check, pp. 16–17 | Concepto correcto; falta la configuración particular del servicio. | La ruta debe existir; App Service espera 200–299 y no sigue redirecciones. Comprobar dependencias críticas. | [Health Check de App Service](https://learn.microsoft.com/en-us/azure/app-service/monitor-instances-health-check) |
| Variables y credenciales, p. 17 | Separar configuración y código es correcto; una variable no protege por sí sola un secreto. | Usar mecanismos de secretos compatibles con el entorno y evitar volcados de valores. Cambiar app settings puede reiniciar la aplicación. | [Configuración](https://learn.microsoft.com/en-us/azure/app-service/configure-common), [Referencias a Key Vault](https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references) |
| Terraform, p. 7 | Introducción incompleta para ejecutar cambios reales. | Revisar el plan y gestionar el estado; archivos de estado y planes pueden contener secretos incluso si se ocultan en la consola. | [Plan](https://developer.hashicorp.com/terraform/cli/commands/plan), [Datos sensibles](https://developer.hashicorp.com/terraform/language/manage-sensitive-data) |

Las fuentes enlazadas se consultaron durante esta revisión. Las precisiones de operación, seguridad y contexto son ampliaciones verificadas; no se atribuyen al PDF. Revalidar las opciones que dependan de versiones o de cambios en Azure antes de implementarlas.

## Diseño elegido para la skill y el agente

Una skill breve dirige al mapa, a las correcciones y a guías prácticas según la tarea. Conserva la relación con las páginas sin cargar un manual completo en cada consulta. Un agente especializado reutiliza esa misma base para relacionar un enunciado con evidencias y evitar conclusiones prematuras.

Esta estructura permite preparar retos de desarrollo, configuración, observabilidad e infraestructura sin asumir que todos exigen Terraform o que toda avería es CORS. El agente no necesita un modelo fijado, nuevas credenciales ni una aplicación de agentes independiente para leer y razonar sobre los materiales.

## Validación del paquete

Se realizó una prueba independiente aplicando la skill y el perfil a tres solicitudes:

| Caso | Resultado observado |
| --- | --- |
| Pedir las diez solicitudes recientes desde un workspace sin credenciales | Produce `AppRequests` y `TimeGenerated`, ordena antes de limitar y diferencia plantilla de resultados ejecutados. |
| CORS en navegador y 500 en la misma operación con curl, con permiso solo de inspección | Prioriza investigar el fallo, mantiene CORS como hipótesis separada y pide código/evidencia que faltan sin inventar una causa. |
| Pedir retos y tecnologías obligatorias sin enunciado | Distingue preparación de requisitos y evita presentar escenarios como confirmados. |

El TOML se analizó con `tomllib`; se comprobaron los campos del frontmatter y los metadatos de interfaz, los enlaces locales y el hash del PDF. No se encontraron defectos bloqueantes en estos casos. La prueba aplicó las instrucciones leídas; no ejecutó el perfil mediante un nuevo proceso de Codex.

El validador auxiliar `quick_validate.py` no pudo iniciar porque el Python disponible carece de PyYAML. Las comprobaciones estructurales propias pasaron; no equivalen a ejecutar ese validador. El descubrimiento automático del perfil y de la skill se debe comprobar al abrir el proyecto en una sesión nueva.

## Límites de la revisión

No se dispone todavía de los retos reales ni de su rúbrica. No se ejecutaron consultas contra Azure, despliegues ni correcciones de recursos durante la revisión. Los ejemplos preparados son plantillas contrastadas con documentación y necesitan adaptarse al esquema y entorno reales. La fiabilidad de cada diagnóstico futuro dependerá de los datos del reto y de su validación.
