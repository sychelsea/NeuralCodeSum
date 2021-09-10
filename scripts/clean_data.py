from preprocess import Preprocess
import base64


def single_method_cleaner(data_file):
    '''
    data_file: the code snippet of a method
    '''
    preprocess = Preprocess("code")
    with open(data_file, "r") as f:
        code_snippet = f.read()
        print(code_snippet)
        code_snippet = preprocess.clean(code_snippet)
        print(code_snippet)


DELIM = " @@ "


def get_method(line):
    tokens = line.split(DELIM)
    name = base64.b64decode(tokens[0])
    comment = base64.b64decode(tokens[1])
    body = base64.b64decode(tokens[2])


OUTPUT_DATA_DIR = "/data/share/ml4se/data/mutation/NeuralCodeSum/"
MUTATION = "branch-swap"
fout_code = open(OUTPUT_DATA_DIR + "code.java_small_" + MUTATION + ".txt", "w")
fout_comment = open(OUTPUT_DATA_DIR + "javadoc.java_samll" + MUTATION + ".txt",
                    "w")

code_preprocess = Preprocess("code")
comment_preprocess = Preprocess("anno")

with open(data_file, "r") as f:
    for line in f.readlines():
        name, comment, body = get_method(line)
        if len(comment) > 0:
            fout_code.write(code_preprocess.clean(body) + "\n")
            fout_comment.write(comment_preprocess.clean(comment) + "\n")
