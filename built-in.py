#!/usr/bin/env python

sample_list = [1, 2, 5, 6, "hello", 'this is an example', True]
append_list = [67, "appended list"]
extend_list = [72, "extend list"]

# methods
sample_list.append(append_list)
print "after append list, sample_list: {0}".format(sample_list)

cnt = sample_list.count("hello")
print "count of hello in sample list: {0}".format(cnt)

sample_list.extend(extend_list)
print "after extend list, sample_list: {0}".format(sample_list)

index_found = sample_list.index(72)
print "found index of 72 in sample_list: {0}".format(index_found)

sample_list.insert(-1, "This is an inserted item")
print "after inserted item to sample list, sample_list: {0}".format(sample_list)

sample_list.remove(5)
print "after remove item '5', sample_list: {0}".format(sample_list)

sample_list.reverse()
print "after reverse, sample_list: {0}".format(sample_list)

sample_list.sort()
print "sorted sample_list: {0}".format(sample_list)