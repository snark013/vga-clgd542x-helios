f = open("rom.bin", "rb")
o = open("rom-out-rev0.3.bin", "wb")
i = 0
while i < 16*1024:
	f.seek(i)
	r = f.read(1)
	e = ((r[0]&1)<<7)+((r[0]&2)<<5)+((r[0]&4)<<3)+((r[0]&8)<<1)+((r[0]&16)>>1)+((r[0]&32)>>3)+((r[0]&64)>>5)+((r[0]&128)>>7)
	u = int.to_bytes(e, byteorder="big", length=1)
	o.write(u)
	f.seek(i+16*1024)
	r = f.read(1)
	e = ((r[0]&1)<<7)+((r[0]&2)<<5)+((r[0]&4)<<3)+((r[0]&8)<<1)+((r[0]&16)>>1)+((r[0]&32)>>3)+((r[0]&64)>>5)+((r[0]&128)>>7)
	u = int.to_bytes(e, byteorder="big", length=1)
	o.write(u)
	i=i+1

o.close()
f.close()

