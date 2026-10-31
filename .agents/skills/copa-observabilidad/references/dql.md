# DQL: plantillas para la sesión 1

Estas consultas **no se han ejecutado en un tenant**. Sustituye los valores ilustrativos y comprueba campos, permisos, tipos y valores reales. Usa la misma ventana/ámbito al comparar resultados. No pegues `AppRequests`, `where` o `operation_Id` de KQL en DQL.

## Logs recientes de error

El ejemplo completa el filtro de error de la p. física 18 y añade clúster para no mezclar namespaces homónimos. Los campos Kubernetes y el valor `ERROR` dependen de la ingesta; si faltan, investiga el enriquecimiento y selecciona un ámbito disponible.

```dql
fetch logs, from: -30m
| filter k8s.cluster.name == "CLUSTER_DEL_RETO"
| filter k8s.namespace.name == "NAMESPACE_DEL_RETO"
| filter loglevel == "ERROR"
| sort timestamp desc
| limit 50
| fields timestamp, loglevel, content, k8s.pod.name
```

Ordenar antes de limitar permite obtener los más recientes. Un límite de salida no garantiza bajo volumen escaneado: acota tiempo y bucket cuando esté confirmado. Si la ejecución devuelve advertencias de truncamiento o límite de escaneo, el resultado es parcial.

## Incidente histórico: errores por pod de un nodo

La ventana y los nombres siguientes son ejemplos. Para un incidente antiguo usa un intervalo absoluto, no una hora relativa al momento de ejecutar. Confirma la pertenencia del pod al nodo durante el incidente, no solo su ubicación actual.

```dql
fetch logs, timeframe: "2026-10-29T14:00:00Z/2026-10-29T14:30:00Z"
| filter k8s.cluster.name == "CLUSTER_DEL_RETO"
| filter k8s.namespace.name == "NAMESPACE_DEL_RETO"
| filter k8s.node.name == "NODO_DEL_RETO"
| filter loglevel == "ERROR"
| summarize registros_error = count(), by:{k8s.pod.name}
| sort registros_error desc
```

Se cuentan registros almacenados que pasan los filtros, no usuarios afectados ni peticiones fallidas. No colocar `limit` antes de `summarize` si se pretende contar todo el conjunto filtrado. El muestreo y la cobertura pueden limitar lo observado.

## Correlación y métricas

Para una operación, parte de un identificador de traza observado y confirma el campo del esquema antes de filtrar spans y logs. Un log sin correlación no se puede asociar a una traza por intuición. Conserva también entidad y ventana; no sumes duraciones de spans anidados o paralelos como si fueran secuenciales.

Para series métricas, descubre la clave, dimensiones y unidad del tenant y usa `timeseries`. `metrics` permite explorar métricas; `makeTimeseries` agrega registros no métricos en el tiempo. No inventes una clave ni promedies percentiles preagregados. Para una tasa, explicita numerador y denominador de la misma población; sin datos o con denominador cero no declares 100 % de éxito.

Si una consulta devuelve cero filas, revisa permisos, retención, ingesta, ámbito, tiempo, campos y severidad antes de concluir que no hubo incidentes. Diferencia una consulta vacía de un error de autorización.

Referencias: [fuentes y ventanas](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/data-source-commands), [agregaciones](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands), [métricas](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands/metric-commands).
