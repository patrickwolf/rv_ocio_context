@echo off
taskkill /IM rv* /F
REM This batch file sets up the environment for RV and launches it with a specific media file.
SET OCIO=C:\test_ocio\_ocio\config.ocio
SET PYTHONPATH=C:\test_ocio\_ocio;%PYTHONPATH%
REM SET RV_SUPPORT_PATH=C:\Temp\RV_PACKAGES
uvx --from opencolorio ociocheck
start "" "C:\Program Files\Autodesk\RV-2024.2.1\bin\rv.exe" "C:\test_ocio\_media_green\HSO_0510_comp_green_v001.1000.exr" "C:\test_ocio\_media_red\HSO_0510_comp_red_v004.1000.exr"
