#!/usr/bin/env ruby
# Match exactly a 10 digit phone number
# {\A Start of string + \d  Any digit + a{num}  Exactly num of a}
puts ARGV[0].scan(/^\d{10}$/).join
