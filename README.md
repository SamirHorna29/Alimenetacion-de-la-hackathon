# Base de preparación para la hackathon de Copa

Base de apoyo para los retos de Copa con tres documentos: Cápsulas Informativas de Microsoft, Sesión 1 de Dynatrace y Charla 2 de Microsoft, Operación Bajo Presión. Incluye dos skills, siete perfiles de agentes y referencias por página con precisiones contrastadas.

El PDF es útil para aprender los conceptos iniciales. Para operar con ellos se corrigieron el ejemplo de registros recientes en KQL y las simplificaciones sobre tablas, CORS y captura de telemetría. Su membrete dice Business IT; el nombre del archivo no acredita autoría de Microsoft.

## Equipo multiagente de Copa

La [guía del equipo](docs/equipo-copa.md) presenta seis perfiles para coordinación, infraestructura, servicios/trazas, DQL, implementación y verificación. La base integra la sesión 1 de Dynatrace y el especialista Azure/KQL con las cápsulas y Operación Bajo Presión. La Charla 2 de Microsoft no es la sesión 2 pendiente de Dynatrace.

```text
Usa $copa-observabilidad y coordina los agentes necesarios para resolver este reto con evidencia: [enunciado].
```

Consulta la [skill Copa](.agents/skills/copa-observabilidad/SKILL.md) y el [análisis del primer documento](.agents/skills/copa-observabilidad/references/sesion-1.md). No se requiere acceso a Dynatrace para estudiar; ejecutar consultas y validar el entorno requiere las herramientas y permisos correspondientes.

- [Charla 2: análisis y precisiones](.agents/skills/hackathon-microsoft/references/charla-2.md).
- [Operación bajo presión](.agents/skills/hackathon-microsoft/references/operacion-bajo-presion.md): ciclo de incidentes y reparto de tareas.
- [Bitácora reutilizable](.agents/skills/copa-observabilidad/assets/bitacora-incidente.md): hipótesis, cambios, evidencia y validación.

## Archivos para trabajar

- [Skill hackathon-microsoft](.agents/skills/hackathon-microsoft/SKILL.md): decide qué referencia consultar y cómo aplicar la base al reto.
- [Agente hackathon_microsoft](.codex/agents/hackathon_microsoft.toml): perfil reutilizable de especialista.
- [Revisión de fiabilidad](.agents/skills/hackathon-microsoft/references/fiabilidad.md): procedencia, correcciones, fuentes y límites.
- [Mapa de las 17 cápsulas](.agents/skills/hackathon-microsoft/references/capsulas.md): páginas y usos prácticos.
- [Diagnóstico](.agents/skills/hackathon-microsoft/references/diagnostico.md) y [KQL](.agents/skills/hackathon-microsoft/references/consultas-kql.md): guías de aplicación.

## Uso en Codex

El material está en la rama `codex/capsulas-skill-agente`; `main` solo contiene el título inicial. Desde una carpeta donde quieras guardar una nueva copia, usa PowerShell con Git y Codex CLI instalados:

```powershell
git clone --branch codex/capsulas-skill-agente https://github.com/SamirHorna29/Alimenetacion-de-la-hackathon.git
Set-Location -LiteralPath './Alimenetacion-de-la-hackathon'
codex
```

Si ya tienes una copia, abre su carpeta y comprueba `git status`. Conserva los cambios locales pendientes antes de cambiar de rama; después ejecuta `git fetch origin` y `git switch codex/capsulas-skill-agente`. También puedes abrir esa carpeta como proyecto en la aplicación.

Para estudiar o trabajar sobre un reto:

```text
Usa $hackathon-microsoft para analizar este enunciado y proponer una solución verificable: [enunciado].
```

Para utilizar el perfil de agente:

```text
Delega al agente hackathon_microsoft la revisión de este reto usando las cápsulas y las evidencias adjuntas: [enunciado o archivos].
```

La skill mantiene la selección automática predeterminada cuando la petición corresponde a esta hackathon. La sesión debe estar abierta en este proyecto para descubrir sus archivos. Si la skill no aparece, vuelve a abrir el proyecto o reinicia Codex. El perfil de agente hereda el modelo y los permisos de la sesión.

Estos formatos siguen la documentación de [skills](https://learn.chatgpt.com/docs/build-skills) y [agentes personalizados](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Estado y fuente

Material preparado el 30/10/2026 para el repositorio [SamirHorna29/Alimenetacion-de-la-hackathon](https://github.com/SamirHorna29/Alimenetacion-de-la-hackathon).

El PDF original está en la carpeta Documentos de OneDrive proporcionada por el usuario. La revisión conserva su hash y sus metadatos para reconocer la versión utilizada. Para cotejar páginas en otro equipo, utiliza una copia autorizada del archivo identificado en la revisión. Las referencias derivadas permiten trabajar con la skill y el agente sin depender de una ruta personal al PDF.

El documento no incluye los retos reales ni sus criterios de evaluación; añade el enunciado cuando esté disponible. Las consultas y guías requieren validación en el entorno que corresponda. La [revisión](.agents/skills/hackathon-microsoft/references/fiabilidad.md#validación-del-paquete) detalla las comprobaciones de formato y los tres casos de prueba del agente, así como lo pendiente de validar.
