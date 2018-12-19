#!/usr/local/bin/ruby

print "Content-type: text/html\n\n"

puts "<html>"
puts "<head>"
puts "<title>簡易リーダー | 簡易掲示板</title>"
puts '<meta charset="UTF-8";>'
puts "</head>"
puts "<body>"


File.open('board.log') do |log|
	log.each_line do |line|
		puts "<p>" + line + "</p>"
	end
end

puts "</body></html>"