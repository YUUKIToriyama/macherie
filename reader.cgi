#!/usr/local/bin/ruby

print "Content-type: text/html\n\n"

puts "<html><head><title>簡易リーダー | 簡易掲示板</title></head>"
puts "<body>"


File.open('board.log') do |log|
	log.each_line do |line|
		puts "<p>" + line + "</p>"
	end
end

puts "</body></html>"