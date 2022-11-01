import sys
import files as f


text = f.textfle_read((sys.argv[1]))
print(text)
print(f.textfle_write(sys.argv[2],text =text))