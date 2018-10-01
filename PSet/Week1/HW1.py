s = 'qwdheuiwanfke'
count = 0
# a = len(s)
for i in range(len(s)):
    if ((s[i]=='a')or(s[i]=='e')or(s[i]=='i')or(s[i]=='o')or(s[i]=='u')):
        count+=1
# for i in range(12):
#     if ((s[i]=='a')or(s[i]=='e')or(s[i]=='i')or(s[i]=='o')or(s[i]=='u')):
#         count+=1
print(count)