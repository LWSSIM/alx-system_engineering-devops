#!/usr/bin/env ruby
# Match (t{3,6}  Between 2 and 5 of t)
puts ARGV[0].scan(/hbt{2,5}n/).join
