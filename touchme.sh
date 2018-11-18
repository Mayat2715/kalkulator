cd $PREFIX/bin
a='$1'
b='$2'
c='$3'
if [ ! -f itung ]; then
	echo "python2 $HOME/kalkulator/kalkulator.py $a $b $c" >> itung
	chmod +x itung
fi
pkg install -y python2
clear
echo '\033[0;1m[\033[1;36m#\033[0;1m]\033[1;32mdone!'
echo '\033[0;1m[\033[1;36m!\033[0;1m]\033[1;32mlangsung panggil dengan perintah "itung", baik di dalam ataupun di luar tool ini!'
