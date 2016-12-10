for file in "$@"
do

echo '$file'
echo "$file"
cat raw/header.txt "$file" > processed/$file
done
echo "done!"


#cd processed

#for input in *.txt
#do 
#	echo "analyzing $input..."
#	pytho 
