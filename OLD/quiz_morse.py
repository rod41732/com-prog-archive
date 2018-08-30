file = open(input().strip(), 'r')
mode = file.readline().strip()
pattern = file.readline().strip()
rest_of_file = [line.strip() for line in file]
if mode == 'T2M':
    for text in rest_of_file:
        morse = ''
        isvalid = 1
        for char in text:
            pos = pattern.find(char)
            if pos == -1: # invalid char
                isvalid = 0
                break
            else:
                right_brk = pattern.rfind(']', 0, pos)
                left_brk = pattern.rfind('[' ,0 , right_brk)
                morse += pattern[left_brk+1:right_brk] + ' '
        if isvalid:
            print(morse.strip())
        else:
            print('Invalid :', text)
elif mode == 'M2T':
    for morse in rest_of_file:
        morse = morse.split()
        text = ''
        isvalid = 1
        for part in morse:
            pos = pattern.find('[' + part + ']')
            # print(part, pos)
            if pos == -1:
                isvalid = 0
                break
            else:
                text += pattern[pos+len(part)+2] # from bracket to char is len() + 2 characters
        if isvalid:
            print(text.strip())
        else:
            print("Invalid :", ' '.join(morse).strip()) 
            # coz we split earlier, so we join again; can also keep orig string
else:
    print("Invalid code")
