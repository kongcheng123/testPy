import re

a='<a class="user-hover user-avatar" href="/jira/secure/ViewProfile.jspa?name=sunilg" id="commentauthor_16017563_verbose" rel="sunilg"><span class="aui-avatar aui-avatar-xsmall"><span class="aui-avatar-inner"><img alt="sunilg" src="/jira/secure/useravatar?size=xsmall&amp;avatarId=10452"/></span></span> Sunil G</a>'
m=re.search(r'rel="(.+)"><span class="aui-avatar aui-avatar-xsmall">',a)
print(m.groups()[0])