import re
import os

# Getting the current work directory (cwd)
directory = "Tests"

json_tags = [{"name": "FUNCTIONNALITY1", "tests": ["TEST1", "TEST1", "TEST9"]},
             {"name": "FUNCTIONNALITY1", "tests": ["TEST3", "TEST3", "TEST4"]},
             {"name": "FUNCTIONNALITY1", "tests": ["TEST5", "TEST8", "TEST7"]}
             ]


def convert_case(match_obj):
        if not(match_obj.group(3)):
            print('dosent match group3')
            return match_obj.group(1).upper() + match_obj.group(2).upper() + "  " + functionality_name.upper()
        else:
            print('do match group3')
            return match_obj.group(1).upper() + match_obj.group(2).upper() + match_obj.group(3).upper()


# r=root, d=directories, f = files
for r, d, f in os.walk(directory):
    for file in f:
        if file.endswith(".robot"):
            print(os.path.join(r, file))
            with open(os.path.join(r, file), 'w') as fd:
                    for funct in json_tags:
                        global functionality_name
                        functionality_name = funct["name"]

                        for test in funct["tests"]:
                            print(test)
                            textToSearch = r'(\[TAGS\])(.*' + test + ')(.*' + functionality_name + ')?'
                            # add tags
                            try:
                                text, counter = re.subn(textToSearch, convert_case, fd.read(), re.I)
                                if counter > 0:
                                    fd.write(text)
                            except:
                                print('exception')




