from preprocess import Preprocess

parser = Preprocess("code")
with open("/data/share/ml4se/example/common/create/correspondence.java",
          "r") as f:

    code_snippet = f.read()
    print(code_snippet)
    code_snippet = parser.clean(code_snippet)
    print(code_snippet)
