#! /usr/bin/env python

choice = ('s', 'j', 'b')

print '%s%s%s' % ('-'*20, 'Welcome', '-'*20)

me = raw_input(' Please make your choice: ').strip()[0].lower()
# print me
robot = choice[0]

if me == robot:
    print 'you eq robot'
else:
    print 'I do not know'
