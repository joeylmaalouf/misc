cwd=$(pwd)
file=$cwd/hello.txt
touch $file
echo "current directory is: $cwd">$file
exec python2 $cwd/mouse.py
