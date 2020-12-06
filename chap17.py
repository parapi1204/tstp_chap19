import re

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""

string = "Two too."

line = "123 hi 34 hello."

t = "__one__ __two__ __three__"

text = """キリンは大昔から __複数名詞__ の興味の対象でした．キリンは
__複数名詞__ の中で一番背が高いですが，科学者たちはそのような長い
 __体の一部__ をどうやって獲得したのか説明できません．キリンの伸長は
 __数値__ __単位__ 近くあり，その高さのほとんどは脚と__体の一部__
 によるものです．
"""
challenge2 = "Arizona 479, 501, 870. California 209, 213, 650."
challenge3 = "The ghost that says boo haunts the loo"

def mad_libs(mls):
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "Input {}: ".format(word)
            new = input(q)
            mls = mls.replace(word, new)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("Argument mls is invalid.")

# mad_libs(text)

astaoo = re.findall(".*.oo", challenge3)
print(astaoo)