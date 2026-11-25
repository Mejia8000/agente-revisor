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
- 25 nov. 2026: repo y secretos listos. La 1.ª corrida trabajó 69 min pero no guardó nada: `git add` fallaba porque la carpeta `.webs` no existía. Corregido (`git add -A`) y ahora se guarda `ultima-corrida.log` para diagnosticar.
- Después de la primera semana: ajustar `repos_por_corrida` según el límite diario gratis de Gemini (sin confirmar cuántas solicitudes da hoy).
