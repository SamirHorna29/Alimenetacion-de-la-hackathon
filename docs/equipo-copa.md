# Equipo multiagente para la hackathon de Copa

Seis perfiles de Codex comparten la skill `copa-observabilidad` y la síntesis del primer documento. Están diseñados para investigar y ejecutar tareas concretas, conservando evidencia entre agentes.

| Agente | Responsabilidad |
| --- | --- |
| `copa_coordinador` | Convierte el enunciado en tareas, elige especialistas e integra la entrega. |
| `copa_infraestructura` | Hosts, Kubernetes, topología y cobertura de instrumentación. |
| `copa_servicios_trazas` | Latencia, fallos, dependencias y causa propuesta. |
| `copa_dql` | Consultas, correlación y agregación de evidencia. |
| `copa_implementador` | Cambios autorizados y pruebas de código/configuración/paneles. |
| `copa_verificador` | Revisión independiente y comprobación del criterio de éxito. |

```mermaid
flowchart TD
    U[Enunciado y evidencia] --> C[Coordinación]
    C --> I[Infraestructura]
    C --> T[Servicios y trazas]
    C --> Q[Consultas DQL]
    I --> E[Evidencia integrada]
    T --> E
    Q --> E
    E --> M[Implementación si corresponde]
    E --> V[Verificación independiente]
    M --> V
    V --> R[Entrega con pruebas y límites]
```

No es necesario activar los seis agentes. El agente principal coordina; los especialistas no vuelven a delegar. Se respetan los cupos de la sesión y se trabaja por tandas cuando haga falta. El especialista existente `hackathon_microsoft` puede atender componentes Azure cuando estén presentes.

## Uso

Abre la raíz de este proyecto en Codex y utiliza:

```text
Usa $copa-observabilidad y coordina los agentes necesarios para este reto de Copa:
[enunciado]
Evidencias: [archivos o resultados]
Entorno y ventana: [datos conocidos]
Alcance autorizado: [lectura, cambios locales o entorno específico]
Criterio de éxito: [resultado esperado, si está definido]
```

Para preparar la sesión sin un reto:

```text
Usa $copa-observabilidad para explicarme la sesión 1, señalar sus simplificaciones
y preparar un ejercicio simulado de diagnóstico con logs, métricas y trazas.
```

También puedes pedir explícitamente: `Delega a copa_dql la revisión de esta consulta` o `Delega a copa_verificador la revisión de esta solución y sus pruebas`.

Los perfiles siguen el formato de [agentes personalizados de Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents); la skill usa el formato de [skills](https://learn.chatgpt.com/docs/build-skills). Heredan modelo y permisos de la sesión. No se requiere fijar otro modelo ni modificar la configuración global. El descubrimiento debe comprobarse al abrir el proyecto; si la sesión no admite delegación, los roles pueden aplicarse de manera secuencial.

## Base documental y límites

Lee [la síntesis y correcciones](../.agents/skills/copa-observabilidad/references/sesion-1.md), [las plantillas DQL](../.agents/skills/copa-observabilidad/references/dql.md) y [los criterios de validación](../.agents/skills/copa-observabilidad/references/validacion.md).

El documento tiene 21 páginas. La corrección principal es que PurePath puede aplicar muestreo; también se precisan la cobertura de OneAgent, los conteos DQL y la diferencia entre correlación y causa raíz. La sesión 2 está anunciada pero no forma parte de esta base.

Estos archivos no instalan OneAgent ni conectan un tenant. Sin acceso real, el equipo entrega análisis y plantillas; con herramientas y autorización pertinentes puede ejecutar comprobaciones. El PDF original no se publica.

## Comprobación local

Con Python 3.11 o posterior:

```powershell
python scripts/validate_copa.py
```

El comprobador verifica estructura TOML, referencias locales y metadatos del paquete. No ejecuta DQL, no prueba un despliegue y no garantiza el descubrimiento del perfil por una sesión nueva.

Consulta el [registro de validación](validacion-copa.md) para distinguir las comprobaciones realizadas de las pendientes.
