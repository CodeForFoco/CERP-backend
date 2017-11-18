#!/usr/bin/env bash

# -----------------------------
# shp-to-geojson.sh
# Convert shapefiles to GeoJSON
# -----------------------------

SOURCE_SHP="${1:-cerp/static/VoterPrecinct.shp}"
DEST_GEOJSON="${2:-cerp/static/VoterPrecinct.geojson}"
FIELDS_TO_KEEP="PRECINCT,SENATEDIST,HOUSEDIST,COMMDIST,UPDATEDATE"
TOLERANCE=0.00015 # smaller decimal = higher precision

# ogr2ogr cannot overwrite GeoJSON?
rm -f $DEST_GEOJSON

# Convert shp to geojson
ogr2ogr \
  -f "GeoJSON" \
  -lco COORDINATE_PRECISION=5 \
  -simplify $TOLERANCE \
  -select $FIELDS_TO_KEEP \
  "$DEST_GEOJSON.tmp" \
  $SOURCE_SHP

# Check if `json-minify` exists, install if not
if ! type json-minify &> /dev/null; then
  npm i -g json-minify
fi

# Minify GeoJSON
json-minify "$DEST_GEOJSON.tmp" > $DEST_GEOJSON

# Delete temp file
rm "$DEST_GEOJSON.tmp"

# topojson example
# topojson $DEST_GEOJSON > "$DEST_GEOJSON.topojson" -p
