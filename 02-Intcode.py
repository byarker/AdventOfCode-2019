

debugging: bool = False;
required_output: int = 19690720

def main():
    with open("data/02-Intcode.txt") as file:
        raw_data = file.read(None).split(",")

        #Convert to ints
        for i in range(0, len(raw_data)):
            raw_data[i] = int(raw_data[i])

    for noun in range(0, 99):
        for verb in range(0, 99):
            intcode = raw_data[:]
            intcode[1] = noun
            intcode[2] = verb
            if(debugging):
                print("%s, Verb = %s" % (noun, verb))
    
            intcode = run_code(intcode)

            if (intcode[0] == required_output):
                print("Code to produce %s is %s" % (required_output, 100 * noun + verb))

    #print("Value at index 0: %s" % (ints[0]))

def run_code(int_list):
    for i in range(0, len(int_list), 4):
        code: int = int(int_list[i])
        #Debugging
        if(debugging):
            print("Index: %s, Code: %s" % (i, code))

        if code == 1:
            total = int_list[int_list[i+1]] + int_list[int_list[i+2]]
            int_list[int_list[i+3]] = total
        elif code == 2:
            total = int_list[int_list[i+1]] * int_list[int_list[i+2]]
            int_list[int_list[i+3]] = total
        elif code == 99:
            return int_list
        else:
            print("Unknown code found")
            return None




if __name__ == "__main__":
    main()
