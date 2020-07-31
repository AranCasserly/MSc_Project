#!/usr/bin/python
with open("sequence.fastq", "r") as data_in, open("barcodes.fastq", "w") as data_out:
	for line in data_in:
		if line.startswith("@SRR12"):
			sequence = data_in.next()[0:12]
			sign = data_in.next()
			quality = data_in.next()[0:12]
		else:
			sequence = data_in.next()
			sign = data_in.next()
			quality = data_in.next()
		data_out.write("{}{}\n{}{}\n".format(line, sequence, sign, quality))
