#!/bin/bash

tests=( "3d-cube" "access-binary-trees" "access-fannkuch" "access-nbody" "access-nsieve" "bitops-3bit-bits-in-byte" "bitops-bits-in-byte" "bitops-bitwise-and" "controlflow-recursive" "math-cordic" "math-partial-sums" "math-spectral-norm" "string-base64" "string-fasta" "string-validate-input" )
icc2spec="icc2specavg.py"

mkdir -p icc
mkdir -p spec
for test in ${tests[@]}
do
  echo "====${test}===="
  echo "Profiling..."
  ./ejsvm --iccprof ./icc/${test}.icc ./sbc/${test}.sbc
  echo "Generating spec file..."
  python3 ${icc2spec} ./icc/${test}.icc ./spec/${test}.spec
done
echo "Done."