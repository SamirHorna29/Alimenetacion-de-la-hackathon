# Operación bajo presión: aplicación al equipo

Base: [Charla 2, páginas físicas 5–7 y 22–24](charla-2.md). Este procedimiento complementa [diagnóstico](diagnostico.md); no reemplaza el alcance ni el criterio de éxito del enunciado.

## Ciclo de trabajo

1. **Detectar:** reproducir la operación, anotar hora/zona, entorno/slot, URL/método, versión y resultado esperado/observado. Determinar impacto con datos, sin inventar usuarios afectados.
2. **Observar:** recoger evidencia en navegador, HTTP, aplicación, plataforma y repositorio según el síntoma. Inspeccionar sin alterar la línea base. Registrar consulta/comando, ventana y resultado; sanitizar secretos.
3. **Analizar:** encontrar la primera discrepancia comprobada y correlacionar la misma operación. Diferenciar falta de datos de falta de tráfico.
4. **Hipótesis:** formular causa candidata, evidencia a favor/en contra y prueba que permita refutarla. Registrar propietario y estado en la bitácora.
5. **Corregir:** el implementador realiza el cambio autorizado, delimitado y reversible cuando sea posible; anota diff, versión y efecto esperado. No cambiar simultáneamente CORS, URL y configuración de un mismo incidente para probar suerte.
6. **Validar:** repetir la operación original en una ventana posterior, revisar salud real, dependencias y funcionalidad. Si aparece otro fallo, volver a observar y comprobar si es una dependencia antes oculta o una regresión del cambio. Conservar una corrección solo mientras su evidencia siga siendo válida; considerar la reversión dentro del alcance autorizado si el cambio empeora el sistema.

Las investigaciones independientes pueden ir en paralelo, con un propietario por línea. Los cambios que afectan al mismo recurso se coordinan y validan secuencialmente. Un rollback autorizado puede mitigar impacto sin resolver todavía la causa: no confundir recuperación con explicación definitiva.

## Primera evidencia por síntoma

| Síntoma | Evidencia que distingue hipótesis | No concluir todavía |
| --- | --- | --- |
| API 500 | Excepción completa sanitizada, primera línea propia, configuración/dependencia y operación asociada. | Que el servidor está apagado o falta una variable solo por el código HTTP. |
| Setting ausente | Nombre esperado en código/IaC, slot y presencia/resolución en configuración efectiva. | Que deba copiarse el valor secreto a logs o al repositorio. |
| Frontend vacío | URL real de Network, DNS, estado, payload y versión del frontend. | Que los datos falten por CORS o que todo frontend requiera rebuild. |
| Error de integración | Método, ruta, Content-Type, JSON y contrato de la versión desplegada. | Que todo 200 vacío sea un fallo o que un 4xx identifique al responsable. |
| Mensaje CORS | Origen exacto, respuesta, preflight si existe y comparación equivalente fuera del navegador. | Que OPTIONS siempre deba llegar a Application Insights o que curl pruebe la política del navegador. |
| Salud verde, operación fallida | Implementación de endpoints, dependencias críticas y prueba funcional real. | Que un health endpoint superficial certifique la release. |
| Fallo tras terraform apply exitoso | Plan/diff aplicado, configuración efectiva, versión y funcionamiento de la aplicación. | Que éxito de IaC sea prueba funcional. |

## Reparto entre agentes

El coordinador asigna `hackathon_microsoft` a App Service, Application Insights y KQL; `copa_dql` se ocupa de Dynatrace/DQL. `copa_servicios_trazas` contrasta la cadena causal; `copa_implementador` ejecuta el cambio autorizado y `copa_verificador` comprueba el resultado. No enviar la misma consulta a varios agentes.

Si ambos sistemas observan la misma aplicación, relaciona entidad, ventana, operación y reglas de propagación antes de asociar sus identificadores. No supongas que un ID de Dynatrace, un encabezado HTTP y OperationId sean intercambiables.

## Bitácora y entrega

Usa la [plantilla del equipo](../../copa-observabilidad/assets/bitacora-incidente.md), copiándola al lugar de trabajo apropiado para el reto; no modifiques la plantilla con datos reales. No versionar payloads sensibles.

Cada hipótesis conserva resultado, motivo de descarte y condición que justificaría reabrirla con nueva evidencia. No repetir una prueba descartada sin un cambio relevante. Para CTFd, prepara respuestas trazables al enunciado y evidencias; no inventes flags ni envíes respuestas como parte de una simple tarea de diagnóstico.

Entrega estado preciso: investigando, mitigado con causa pendiente, corregido pendiente de validación o resuelto con evidencia. Mantén pendientes separados de resultados comprobados.
