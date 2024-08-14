contents = ["I have to write research plan proposal for LUT", 
            "I need to apply to the saveed jobs in linkedin", 
            "Need to lear more Norsk vocabolary"]

file_names = ["phd.txt","job.txt","learn_norsk.txt"]

for content, filename in zip(contents, file_names):
    file = open(f"files/{filename}", 'w')
    file.write(content)
    