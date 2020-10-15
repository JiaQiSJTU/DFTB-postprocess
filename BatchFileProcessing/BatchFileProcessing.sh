export INPUT_PATH="" 
export OUT_PATH=""

filelist=`ls $INPUT_PATH`
echo $filelist
for file in $filelist 
do
  echo $INPUT_PATH'/'$file
  cp $INPUT_PATH'/'$file dftb_in.xyz
  xtb --gfn 2 dftb_in.xyz > output.log
  mv $OUT_PATH'/'output.log $OUT_PATH'/'$file'.log'
  rm dftb_in.xyz
done