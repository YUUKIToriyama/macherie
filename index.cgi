#!/usr/local/bin/ruby
print "Content-type: text/html\n\n"

puts "<!DOCTYPE html>"
puts "<html>"
puts "<head>"
puts '	<meta charset="UTF-8">'
puts "	<title>簡易掲示板</title>"
puts "</head>"
puts "<body>"
puts "	<h1>簡易掲示板</h1>"
puts "	<p>http://redstar.jpn.org/bulletin_board/index.cgi</p>"
puts '	<form action="send_to_board.cgi" method="POST">'
puts "		<h3>名前</h3>"
puts '		<input type="text" name="user_name">'
puts "		<h3>書き込み内容</h3>"
puts '		<input type="text" name="kakikomi">'
puts "		<h3>実行</h3>"
puts '		<input type="submit" value="書き込み">'
puts "	</form>"

puts "<br/>"


#スレッドの表示
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

puts "</body>"
puts "</html>"
