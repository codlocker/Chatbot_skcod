import inspect
import api.bot.df as df
import api.bot.df_rules as dfRules
import api.bot.generation_templates as genTemplates
import api.bot.generation_rules as genRules

def generateDfRules():
    source_code = list(inspect.getsourcelines(dfRules.main_function))[0]
    source_code_out = ''
    indent = source_code[1].strip(" ").strip('\t')
    indenta = len(source_code[1])-len(indent)
    for i in range(1,len(source_code)-1):
        final_indent = indenta
        for j in range(0, indenta):
            if (source_code[i][j] != " "):
                final_indent = j
                break
        temp_string = source_code[i][final_indent:]
        source_code_out = source_code_out + temp_string
    df_rules_file = open('df_rules.py','wb')
    df_rules_file.write(source_code_out)
    df_rules_file.close()

def generateGenRules():
    source_code = list(inspect.getsourcelines(genRules))[0]
    source_code_out = ''
    indent = source_code[1].strip(" ").strip('\t')
    indenta = len(source_code[1]) - len(indent)
    for i in range(1,len(source_code)-1):
        final_indent = indenta
        for j in range(0, indenta):
            if (source_code[i][j] != " "):
                final_indent = j
                break
        temp_string = source_code[i][final_indent:]
        source_code_out = source_code_out + temp_string
    gen_rules_file = open('gen_rules.py','wb')
    gen_rules_file.write(source_code_out)
    gen_rules_file.close()

def generateGenTemplates():
    source_code = list(inspect.getsourcelines(genTemplates))[0]
    source_code_out = ''
    indent = source_code[1].strip(" ").strip('\t')
    indenta = len(source_code[1]) - len(indent)
    for i in range(1,len(source_code)-1):
        final_indent = indenta
        for j in range(0, indenta):
            if (source_code[i][j] != " "):
                final_indent = j
                break
        temp_string = source_code[i][final_indent:]
        source_code_out = source_code_out + temp_string
    gen_templates_rules_file = open('gen_templates.py','wb')
    gen_templates_rules_file.write(source_code_out)
    gen_templates_rules_file.close()

def generateDf():
    source_code = list(inspect.getsourcelines(df))[0]
    source_code_out = ''
    for i in range(0,len(source_code)):
        temp_string = source_code[i]
        source_code_out = source_code_out + temp_string
    df_file = open('df.py','wb')
    df_file.write(source_code_out)
    df_file.close()

generateDf()
generateDfRules()
generateGenRules()
generateGenTemplates()