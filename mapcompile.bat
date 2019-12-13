@echo off
py scripts/setupmapcompile.py
java -cp enigma.jar cuchaz.enigma.CommandMain convert-mappings enigma mappings/ tiny:proguard:named dontpush/client.tiny