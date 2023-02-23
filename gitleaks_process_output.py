import os

input_dir: str = '/home/ruso/Documents/processing/'
output_dir = '/home/ruso/Documents/processed/'
output_prefix = 'output_'  # Change this to the prefix you want for the output files

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, output_prefix + filename)

        with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
            for line in f_input:
                if line.startswith('Finding') or line.startswith('Secret') or line.startswith('File'):
                    f_output.write(line)

file = open("/home/ruso/Documents/processed/output_testfile.txt", "r")
data = file.read()
occurrences = data.count("Finding")
#occurrences_string = str(occurrences)
#with open("/home/ruso/Documents/processed/output_testfile.txt", "w") as work_file:
#    work_file.write(occurrences_string)
print('Number of Findings:', occurrences)



