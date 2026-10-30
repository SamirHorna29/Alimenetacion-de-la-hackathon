# Alimenetacion-de-la-hackathon

Base de apoyo para los retos, elaborada a partir de `Capsulas Informativas - Microsoft.pdf`. Incluye una skill de Codex, un agente especializado y una revisión de fiabilidad con referencias a las páginas y a documentación primaria.

El PDF es útil para aprender los conceptos iniciales. Para operar con ellos se corrigieron el ejemplo de registros recientes en KQL y las simplificaciones sobre tablas, CORS y captura de telemetría. Su membrete dice Business IT; el nombre del archivo no acredita autoría de Microsoft.

## Archivos para trabajar

- [Skill hackathon-microsoft](.agents/skills/hackathon-microsoft/SKILL.md): decide qué referencia consultar y cómo aplicar la base al reto.
- [Agente hackathon_microsoft](.codex/agents/hackathon_microsoft.toml): perfil reutilizable de especialista.
- [Revisión de fiabilidad](.agents/skills/hackathon-microsoft/references/fiabilidad.md): procedencia, correcciones, fuentes y límites.
- [Mapa de las 17 cápsulas](.agents/skills/hackathon-microsoft/references/capsulas.md): páginas y usos prácticos.
- [Diagnóstico](.agents/skills/hackathon-microsoft/references/diagnostico.md) y [KQL](.agents/skills/hackathon-microsoft/references/consultas-kql.md): guías de aplicación.

## Uso en Codex

Abre esta carpeta como proyecto en Codex. También puedes iniciar el CLI desde PowerShell:

```powershell
Set-Location -LiteralPath 'C:\Users\SamirHorna\OneDrive\Documentos\GitHub\Alimenetacion-de-la-hackathon'
codex
```

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
