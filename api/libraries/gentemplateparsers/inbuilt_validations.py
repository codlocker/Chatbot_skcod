inbuilt = ['delay']

def delay_checker(reply_value):
    if type(reply_value['delay'] == type(1)):
        return "ok"
    else:
        return {"error":True,"message":"please check the type of delay"}


def combiner(reply_values,output_values):
    output = []
    index = 0
    for i in reply_values:
        flag = 0
        for j in inbuilt:
            if j in i:
                flag = 1
                output.append(i)
        if flag == 0:
            output.append(output_values[index])
            index = index + 1
    return output