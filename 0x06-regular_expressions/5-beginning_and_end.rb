#!/usr/bin/env ruby
# Match string that starts with h ends with n and can have any single character in between
# (.  Any single character)
puts ARGV[0].scan(/h.n/).join
