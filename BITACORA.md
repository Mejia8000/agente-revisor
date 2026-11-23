# BITÁCORA — Agente revisor

## Estado actual
Código listo (23 nov. 2026). Corre gratis en GitHub Actions; Gemini lee y escribe los informes, Nemotron (OpenRouter) es el respaldo. No usa tokens de Claude.

## Cómo funciona
- Todos los días a las 3:17 a. m. (Managua) busca repositorios con cambios en las organizaciones de `fuentes.json` (google, google-gemini, google-deepmind, NVIDIA).
- Repositorio nuevo: clona y le pasa a Gemini el código completo (hasta 15 000 líneas; se cambia en `fuentes.json`).
- Repositorio ya revisado: solo le pasa lo que cambió desde la vez anterior.
- Revisa primero los de más estrellas, 15 por corrida; lo que espera más de 14 días se descarta.
- Informes en `informes/AAAA-MM-DD/`; `RESUMEN.md` tiene una línea por repositorio.

## Agregar más
Editar `fuentes.json`: `organizaciones`, `repositorios` (dueño/nombre) o `webs` (direcciones). Para revisar algo ya: Actions → Agente revisor → Run workflow → escribir el repositorio o la web.

## Dónde quedó y qué sigue
- Falta: crear el repositorio, subir el código y poner los secretos GEMINI_API_KEY y OPENROUTER_API_KEY.
- Después de la primera semana: ajustar `repos_por_corrida` según el límite diario gratis de Gemini (sin confirmar cuántas solicitudes da hoy).
