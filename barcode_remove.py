#!/usr/bin/python
with open("og_forward.fastq", "r") as data_in, open("forward.fastq", "w") as data_out:
        for line in data_in:
                if line.startswith("@SRR12"):
                        sequence = data_in.next()[12:]
                        sign = data_in.next()
                        quality = data_in.next()[12:]
                else:
                        sequence = data_in.next()
                        sign = data_in.next()
                        quality = data_in.next()
                data_out.write("{}{}{}{}".format(line, sequence, sign, quality))




