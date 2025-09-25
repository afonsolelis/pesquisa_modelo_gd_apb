#!/bin/bash
# Script para usar PlantUML facilmente
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
java -jar "$SCRIPT_DIR/plantuml.jar" "$@"