#!/usr/bin/env ruby
# OutPut from a 'TextMe .log' file ([SENDER],[RECEIVER],[FLAGS])
sender = ARGV[0].scan(/from:(.*?)\]/).join(',')
receiver = ARGV[0].scan(/to:(.*?)\]/).join(',')
flags = ARGV[0].scan(/flags:(.*?)\]/).join
puts "#{sender},#{receiver},#{flags}"
