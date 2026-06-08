#!/bin/bash
# script maker

read -p "path: " p
read -p "name: " n

mkdir -p $p
cd $pth

if [ -f $n ]; then
	echo "file exist"
	exit 1
fi

echo "#!/bin/bash" > $n
echo "echo \"hello world\"" >> $n

chmod +x $n
