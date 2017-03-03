gcc -fPIC -c add_two.c
gcc -fPIC -c arrays.c
gcc -shared add_two.o arrays.o -o libmate.so
