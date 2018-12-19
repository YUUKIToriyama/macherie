#!/usr/local/bin/ruby
print "Content-type: text/html\n\n"

require "cgi-lib"
input = CGI.new

string_name = input["user_name"]
string_name = CGI.escapeHTML(string_name)
string_kakikomi = input["kakikomi"]
string_kakikomi = CGI.escapeHTML(string_kakikomi)

#Timeメソッドで現在時刻をUSTで取得、strftimeで表示フォーマットを変換
string_time = Time.new.strftime("%Y年%-m月%-d日 %-H時%-M分%S秒 UST").to_s

#書き込むテキストファイルのパーミッションは664に設定しておく

File.open('board.log', mode = 'a') do |file|
	file.write(string_time + "\t" + string_name + "\t" + string_kakikomi + "\n")
end

puts "<p>入力された文字をファイルに書き込みました</p>"
puts '<a href="board.log">board.log</a>'
puts "<p>現在時刻: " + Time.new.to_s + "</p>"