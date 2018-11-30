.data
	array:	.double -1.13, 3, 4, 5, 6, 2.0, 5, 90, 12, 30, 2, -1, 2.2, 2, -1.5, 3.22, 25.77
	length:	.double 17
	length1:	.word 17
	length2:	.double 16
	sum:	.double 0
	average:	.double 0
	var:	.double 0
	funcion: .asciiz "Var: "

.text
	main:
	la $t0, array
	li $t1, 0
	ldc1 $f2, length
	lw $t2, length1
	ldc1 $f4, sum
	sumLoop:
		ldc1 $f6, ($t0)
		add.d $f4, $f4, $f6
		add $t1, $t1, 1
		add $t0, $t0, 8
		blt $t1, $t2, sumLoop
	swc1 $f4, sum

	#li $v0, 3
	#mov.d $f12, $f4
	#syscall

	div.d $f6, $f4, $f2
	swc1 $f6, average
	mov.d $f8, $f6

	#li $v0, 3
	#mov.d $f12, $f8
	#syscall

	la $t0, array
	li $t1, 0
	ldc1 $f2, length2
	lw $t2, length1
	ldc1 $f10, var
	devLoop:
		ldc1 $f6, ($t0)
		sub.d $f4, $f6, $f8
		mul.d $f4, $f4, $f4
		add.d $f10, $f10, $f4
		add $t1, $t1, 1
		add $t0, $t0, 8
		blt $t1, $t2, devLoop
	swc1 $f10, sum

	div.d $f10, $f10, $f2
	swc1 $f10, average

	li $v0, 4
	la $a0, funcion
	syscall

	li $v0, 3
	mov.d $f12, $f10
	syscall

	li $v0, 10
	syscall