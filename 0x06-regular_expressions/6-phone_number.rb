#!/usr/bin/env ruby
# Match exactly a 10 digit phone number
# {^ Start of line + \d  Any digit + a{num}  Exactly num of a + $ End of line}
puts ARGV[0].scan(/^\d{10}$/).join
