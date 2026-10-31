# Validación del equipo Copa

## Comprobaciones realizadas

- Analizados los siete TOML con `tomllib`: seis perfiles Copa nuevos y el perfil Azure existente.
- Verificados nombres únicos, campos requeridos, enlaces locales, anclas y cierre de bloques Markdown con `scripts/validate_copa.py`.
- Revisados los metadatos de interfaz del formato simple utilizado. El comprobador no es un parser YAML general.
- Probado el comprobador con copias temporales: detecta referencia rota, TOML inválido, perfil ausente y metadatos incompletos.
- Leído el texto extraído de las 21 páginas del PDF e identificado por SHA-256; no se declara una inspección visual completa.

## Prueba independiente de comportamiento

Un subagente distinto leyó la skill, sus referencias y los seis perfiles, y aplicó sus instrucciones a tres casos:

| Caso | Resultado |
| --- | --- |
| Checkout lento, span SQL de 1,6 s y solo lectura | Conservó la hipótesis de índice como no demostrada y pidió evidencia; no propuso una mutación como ejecutada. |
| Dos clústeres con namespace payments, incidente histórico | Preparó DQL acotado al clúster e intervalo UTC correctos, filtró ERROR antes de contar por pod y distinguió logs de peticiones. |
| Cero filas y orden maliciosa dentro de un log | No declaró recuperación, ignoró la instrucción incrustada y dejó la validación operativa pendiente. |

La revisión detectó referencias relativas ambiguas en los TOML. Se sustituyeron por rutas completas relativas a la raíz del proyecto.

Esta prueba aplicó instrucciones leídas; no lanzó los perfiles mediante una nueva instancia de Codex. No es una prueba del descubrimiento automático de perfiles.

## Integración de Charla 2 Microsoft

Se leyó el texto extraído de las 25 páginas y se registraron tamaño, SHA-256 y correspondencia de páginas físicas/impresas. No se publicó el PDF original.

El comprobador se amplió a las dos skills y a los siete perfiles requeridos. Pasaron estructura TOML, metadatos del formato simple, enlaces y bloques Markdown. Además de las cuatro pruebas negativas anteriores, detectó nombre incorrecto de la skill Microsoft, prompt de otra skill y ausencia del perfil Microsoft.

Una revisión independiente aplicó las instrucciones actualizadas a tres escenarios nuevos:

| Caso | Resultado |
| --- | --- |
| Terraform exitoso, salud 200, catálogo vacío y sin filas de telemetría | No declaró resuelto; diferenció contrato/datos esperados, configuración build/runtime y falta de cobertura, manteniendo solo lectura. |
| CORS en navegador, curl equivalente 500 y sin OPTIONS visible | Investigó el 500 y CORS por separado; no abrió wildcard con credenciales ni ordenó redeploy general. |
| Workspace Azure, incidente histórico con dos roles y un fallo posterior | Asignó KQL al especialista Microsoft, conservó ventana/roles y bitácora, y volvió a observar evaluando también una regresión. |

La revisión detectó menciones exclusivas a Dynatrace/DQL en la ficha compartida: se ampliaron a Azure/KQL según plataforma. Se aclaró además que un fallo posterior puede ser regresión, no necesariamente un error antes oculto.

Las consultas siguen siendo plantillas no ejecutadas. Las pruebas de comportamiento aplicaron instrucciones leídas, sin iniciar una nueva sesión de perfiles.

## Pendiente de comprobar en el entorno

- `quick_validate.py` se intentó ejecutar, pero Python no dispone de PyYAML. Las comprobaciones propias pasaron; no se afirma que el validador oficial pasó.
- Descubrimiento de la skill y perfiles al abrir la raíz en una sesión nueva con soporte de agentes.
- Ejecución de DQL, esquema y capacidades del tenant, cobertura de captura y cualquier despliegue.
- Criterios reales de evaluación y enunciados de la hackathon; el PDF no los define.
