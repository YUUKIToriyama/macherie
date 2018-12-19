#!/usr/local/bin/ruby
print "Content-type: text/html\n\n"

puts "<html>"
puts "<head>"
puts '	<meta charset="UTF-8";>'
puts "	<title>スレッド表示 | 簡易掲示板</title>"
puts "</head>"
puts "<body>"
puts '<table border="2">'
puts "	<tr>"
puts "		<th>書き込み日時</th>"
puts "		<th>ユーザー名</th>"
puts "		<th>書き込み内容</th>"
puts "	</tr>"
puts "	<tr>"
puts "		<td>2018年12月20日 4時59分58秒 UST</td>"
puts "		<td>ヤマダタロウ</td>"
puts "		<td>これはテストです。</td>"
puts "	</tr>"

#ログファイルを読み込みHTML表形式に変換する部分
File.open('board.log') do |file|
	file.each do |line|
		arr_tmp = line.split("\t")
		puts "<tr>"
		puts "	<td>" + arr_tmp[0].chomp + "</td>"
		puts "	<td>" + arr_tmp[1].chomp + "</td>"
		puts "	<td>" + arr_tmp[2].chomp + "</td>"
		puts "</tr>"
	end
end


puts "</table>"
puts "</body>"
puts "</html>"
