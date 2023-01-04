astro={'message': 'success',
 'people': [{'name': 'Sergey Prokopyev', 'craft': 'ISS'},
            {'name': 'Dmitry Petelin', 'craft': 'ISS'},
            {'name': 'Frank Rubio', 'craft': 'ISS'},
            {'name': 'Nicole Mann', 'craft': 'ISS'},
            {'name': 'Josh Cassada', 'craft': 'ISS'},
            {'name': 'Koichi Wakata', 'craft': 'ISS'},
            {'name': 'Anna Kikina', 'craft': 'ISS'},
            {'name': 'Fei Junlong', 'craft': 'Shenzhou 15'},
            {'name': 'Deng Qingming', 'craft': 'Shenzhou 15'},
            {'name': 'Zhang Lu', 'craft': 'Shenzhou 15'}],
 'number': 10}

# print(astro['people'][5]['name'])
a=astro['people'][0]['name']
print(a)
# for i in astro:
#     print(i['people'])