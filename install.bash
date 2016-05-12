PROJECT_NAME="uptime-display"
PROJECT_PATH=`dirname $0`
TMP_DIR=`mktemp -d`
ZIP_PATH="$TMP_DIR/uptime-display.zip"
(cd uptime-display && zip -r "$ZIP_PATH" .)

plasmapkg -r "$PROJECT_NAME"
plasmapkg -i "$ZIP_PATH"

rm -rf "$TMP_DIR"
