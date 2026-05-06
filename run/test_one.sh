#!/bin/bash
# Single-field, single-subrun smoke test for gulls.
# Usage: ./test_one.sh [FIELD_ID] [SUBRUN]
#   FIELD_ID defaults to 0
#   SUBRUN   defaults to 0

set -euo pipefail

F=${1:-0}
S=${2:-0}


PRM=$GULLS_INPUT_DIR/parameter_files/test.prm
BIN=$GULLS_BASE_DIR/bin/gulls_general.x

SRC=$GULLS_STARS_DIR/Huston2024_surot2d_binaries/binary_gulls_surot2d_H2024.sources
LNS=$GULLS_STARS_DIR/Huston2024_surot2d_binaries/binary_gulls_surot2d_H2024.lenses
SFL=$GULLS_STARS_DIR/Huston2023_surot2d/gulls_surot2d_H2023.starfields

LOGDIR=/fs/scratch/PAS3230/gulls_logs
OUTDIR=/fs/scratch/PAS3230/gulls_outputs
mkdir -p "$LOGDIR" "$OUTDIR"

n_src=$(grep -c "^$F " "$SRC" || true)
n_lns=$(grep -c "^$F " "$LNS" || true)
n_sfl=$(grep -c "^$F " "$SFL" || true)
echo "field $F  -> src=$n_src  lens=$n_lns  sf=$n_sfl"

if [ "$n_src" -ne 1 ] || [ "$n_lns" -ne 1 ] || [ "$n_sfl" -ne 5 ]; then
    echo "ERROR: field $F doesn't have the expected (1,1,5) row counts. Pick another field." >&2
    exit 1
fi

LOG=$LOGDIR/test_${S}_${F}.log
echo "Running: $BIN -i $PRM -s $S -f $F -d -d"
echo "Logging to: $LOG"

"$BIN" -i "$PRM" -s "$S" -f "$F" -d -d 2>&1 | tee "$LOG"
