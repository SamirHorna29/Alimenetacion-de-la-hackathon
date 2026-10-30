# KQL para investigar los retos

Plantillas elaboradas para esta base. **No se han ejecutado contra un entorno Azure.** Ajusta ventana, recurso, rol y campos al esquema real. La ventana de 30 minutos es un ejemplo, no un requisito del PDF.

## Confirmar el contexto

| Dato | Application Insights | Workspace de Log Analytics |
| --- | --- | --- |
| Solicitudes | `requests` | `AppRequests` |
| Excepciones | `exceptions` | `AppExceptions` |
| Dependencias | `dependencies` | `AppDependencies` |
| Mensajes de aplicación | `traces` | `AppTraces` |
| Métricas personalizadas | `customMetrics` | `AppMetrics` |
| Fecha | `timestamp` | `TimeGenerated` |
| Correlación | `operation_Id` | `OperationId` |
| Estado de solicitud | `resultCode` | `ResultCode` |
| Rol de aplicación | `cloud_RoleName` | `AppRoleName` |

Comprueba las tablas visibles y los campos antes de copiar una consulta. El [modelo de telemetría](https://learn.microsoft.com/en-us/azure/azure-monitor/app/data-model-complete) explica los contextos. Las métricas estándar también pueden almacenarse en el sistema de métricas; no presumas una tabla universal llamada `Metrics`.

Si el workspace reúne varias aplicaciones, añade un filtro por el `_ResourceId` confirmado o por el rol correcto antes de comparar resultados. Evita mezclar incidentes de recursos distintos.

## Solicitudes más recientes

En Application Insights:

```kusto
requests
| where timestamp > ago(30m)
| order by timestamp desc
| take 10
| project timestamp, name, resultCode, operation_Id, cloud_RoleName
```

En el workspace:

```kusto
AppRequests
| where TimeGenerated > ago(30m)
| order by TimeGenerated desc
| take 10
| project TimeGenerated, Name, ResultCode, OperationId, AppRoleName
```

Corrección del ejemplo de la página 10: sin ordenación, `take 10` devuelve una muestra de hasta diez registros. Consulta [take](https://learn.microsoft.com/en-us/kusto/query/take-operator).

## Solicitudes con respuestas 5xx

Ejemplo de workspace; para buscar solo HTTP 500, sustituye el filtro numérico por `ResultCode == "500"`.

```kusto
AppRequests
| where TimeGenerated > ago(30m)
| where toint(ResultCode) between (500 .. 599)
| project TimeGenerated, Name, ResultCode, OperationId, AppRoleName
| order by TimeGenerated desc
| take 50
```

Los campos se contrastaron con [AppRequests](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/apprequests). Un resultado vacío requiere revisar ámbito y captura antes de descartar fallos.

## Excepciones recientes

```kusto
AppExceptions
| where TimeGenerated > ago(30m)
| project TimeGenerated, ExceptionType, Message, OperationId, AppRoleName
| order by TimeGenerated desc
| take 50
```

Revisa si los mensajes contienen información sensible antes de compartir resultados. Los campos se contrastaron con [AppExceptions](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/appexceptions).

## Correlacionar una operación

Sustituye el literal de ejemplo por un `OperationId` observado; acota también el recurso cuando corresponda.

```kusto
let observedOperationId = "REEMPLAZAR_POR_ID_OBSERVADO";
union withsource=SourceTable AppRequests, AppExceptions, AppDependencies, AppTraces
| where TimeGenerated > ago(30m)
| where OperationId == observedOperationId
| order by TimeGenerated asc
| take 100
```

En Application Insights, el equivalente usa las tablas minúsculas, `timestamp` y `operation_Id`. La correlación depende de que la instrumentación propague el identificador; su ausencia no prueba que los componentes sean independientes.

## Cantidad de filas observadas por estado

```kusto
AppRequests
| where TimeGenerated > ago(30m)
| summarize StoredRows=count() by ResultCode
| order by StoredRows desc
```

Comunica que se contaron filas almacenadas en la ventana consultada. El muestreo y los filtros pueden hacer que no representen todas las solicitudes. Para estimaciones o métricas de tráfico, confirma la configuración y semántica de `ItemCount` antes de agregarlo: [muestreo](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-sampling), [métricas](https://learn.microsoft.com/en-us/azure/azure-monitor/app/metrics-overview).

Las consultas KQL son de lectura; los comandos de administración de Kusto son una categoría distinta. Estas plantillas no conceden acceso a un workspace: [KQL](https://learn.microsoft.com/en-us/kusto/query/).
