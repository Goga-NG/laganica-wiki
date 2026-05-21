# Elongacija polipeptidnog lanca i okončanje sinteze proteina

*Pitanje nije zavrseno* 
for %f in (docs\druga-godina\medicinska-biohemija\proteini\*.md) do if not "%~nxf"=="index.md" (echo.>> "%f" && echo [← Nazad na pitanja](index.md) >> "%f")