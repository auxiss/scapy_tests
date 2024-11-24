


def readLine(fileName,line):
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            number_of_lines = content.count('\n') + 1

            # Check if the specified line number is valid
            if 0 < int(line) <= number_of_lines :
                linedata = content.split('\n')[int(line) - 1].strip()
                return linedata
            
            else:
                print("Error: file only hase",number_of_lines,"line(s). you are tring to accses line",line)

    except IOError as e:
        print(f"Error reading the file: {e}")


def addline(fileName,lineContent):
    try:
        # add line content to the and of the file
        with open(fileName,'a') as file:
            file.write(lineContent)

    except IOError as e:
        print(f"Error reading the file: {e}")
            

def addStringToLine(fileName, line_number, string_to_add):
    try:
        # Read the existing content
        with open(fileName, 'r') as file:
            lines = file.readlines()

        # Check if the specified line number is valid
        if 0 < line_number <= len(lines):
            # Modify the specified line by adding the string
            lines[line_number - 1] = lines[line_number - 1].rstrip('\n') + string_to_add + '\n'

            # Write the modified content back to the file
            with open(fileName, 'w') as file:
                file.writelines(lines)
        else:
            print(f"Error: Line number {line_number} is out of range.")
    except IOError as e:
        print(f"Error updating the file: {e}")


def readfile(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            number_of_lines = content.count('\n') + 1

            textfile = []

            # Check if the specified line number is valid
            line = 0
            while( line < number_of_lines):
                linedata = content.split('\n')[int(line) - 1].strip()
                textfile.append(linedata)
                line = line + 1
            return textfile
    except IOError as e:
        print(f"Error reading the file: {e}")

#print(readLine(input("Enter file name:"),input("ENter line to read: ")))