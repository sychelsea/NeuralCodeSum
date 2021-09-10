from preprocess import Preprocess
import base64
from javalang import javadoc


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
    #name = base64.b64decode(tokens[0]).decode("utf-8")
    
    comment = base64.b64decode(tokens[1]).decode("utf-8")
    doc_block = javadoc.parse("/** " + comment+ " */")
    comment = doc_block.description

    body = base64.b64decode(tokens[2]).decode("utf-8")

    return comment, body


DATA_DIR = "/data/share/ml4se/data/mutation/"

MUTATION = "return-condition"
fout_code = open(
    DATA_DIR + "NeuralCodeSum/code.java_small_" + MUTATION + ".txt", "w")
fout_comment = open(
    DATA_DIR + "NeuralCodeSum/javadoc.java_samll_" + MUTATION + ".txt", "w")
data_file = DATA_DIR + "java_small_" + MUTATION + ".txt"

code_preprocess = Preprocess("code")
comment_preprocess = Preprocess("anno")

with open(data_file, "r") as f:
    for line in f.readlines():
        comment, body = get_method(line)
        if len(comment) > 0:
            fout_code.write(code_preprocess.clean(body) + "\n")
            fout_comment.write(comment_preprocess.clean(comment) + "\n")
         
