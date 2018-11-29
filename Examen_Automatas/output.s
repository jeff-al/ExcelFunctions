.data
	array:	.double 3, 4, 5, 6, 2, 3
	length:	.double 6
	length1: .word 6
	sum:	.double 0
	average:	.double 0
.text
	main:
	la $t0, array
	li $t1, 0
	ldc1 $f2, length
	lw $t2, length1
	ldc1 $f4, sum
	sumLoop:
		lwc1 $f6, ($t0)
		add.d $f4, $f4, $f6
		add $t1, $t1, 1
		add $t0, $t0, 4
		blt $t1, $t2, sumLoop
	swc1 $f4, sum

	li $v0, 3
	mov.d $f12, $f4
	syscall

	div.d $f6, $f2, $f8
	swc1 $f6, average

	li $v0, 10
	syscall
