import os
all_txt_files = list(filter(lambda x: x.endswith('.txt'), os.listdir()))
len_files = [sum(1 for line in open(file,'r', encoding='utf-8')) for file in all_txt_files]
files_dict = dict(zip(all_txt_files, len_files))
sorted_dict = dict(sorted(files_dict.items(), key=lambda item: item[1]))

with open('result.txt','a', encoding='utf-8') as new_file:
    for ff in sorted_dict:
        with open(ff, encoding='utf-8') as f:
            txt = f.read()
        new_file.write(f'{ff}\n{sorted_dict[ff]}\n')
        new_file.write(txt)
        new_file.write('\n')
