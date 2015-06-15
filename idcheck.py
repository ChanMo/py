#! user/bin/env python

import string

alphas = string.letters + '_'
nums = string.digits

# print '*'*20 + 'Identifier' + '*'*20
print '%s%s%s' % ('*'*20, 'Identifier', '*'*20)
print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Indentifiler to test? ')

if len(myInput) > 1:

    if myInput[0] not in alphas:
        print '''invalid: first symbol must be alphabetic'''
    else:
        alphnums = alphas + nums
        for otherChar in myInput[1:]:

            if otherChar not in alphnums:
            # if otherChar not in alphas + nums:
                print '''invalid:
                    remaining symbols must be alphanumeric'''
                break
        else:
            print "okay as an identifier"

else:
    print "testees must be as least 2 chars long"
