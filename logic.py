import re

PAT = r'(\+7|8)*[\s\(]*(\d{3})[\s\)]*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s)*[\(]*(доб\.)*[\s]*(\d{4})*[\)]*'
SUB = r'+7(\2)-\3-\4-\5\6\7\8'

def new_list(con_list: list):
  new_list = list()
  for item in con_list:
    name = ' '.join(item[:3]).split(' ')
    stroka = [name[0], name[1], name[2], item[3], item[4], re.sub(PAT, SUB, item[5]), item[6]]
    new_list.append(stroka)
  return red_n_l(new_list)

def red_n_l(cons: list):
  for con in cons:
    first_name = con[0]
    last_name = con[1]
    for new_con in cons:
      new_first_name = new_con[0]
      new_last_name = new_con[1]
      if first_name == new_first_name and last_name == new_last_name:
        if con[2] == "":
          con[2] = new_con[2]
        if con[3] == "":
          con[3] = new_con[3]
        if con[4] == "":
          con[4] = new_con[4]
        if con[5] == "":
          con[5] = new_con[5]
        if con[6] == "":
          con[6] = new_con[6]

  result_list = list()
  for i in cons:
      if i not in result_list:
          result_list.append(i)

  return result_list
