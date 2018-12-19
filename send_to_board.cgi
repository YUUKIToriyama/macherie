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

#HTMLを表示
puts "<!DOCTYPE html>"
puts "<html>"
puts "<head>"
puts '	<meta charset="UTF-8">'
puts "	<title>入力内容を書き込みました | 簡易掲示板</title>"
puts "</head>"
puts "<body>"
puts "	<p>入力内容をファイルに書き込みました</p>"
puts '	<a href="index.cgi">スレッド表示画面に戻る</a>'
puts "	<p>現在時刻: " + Time.new.to_s + "</p>"
puts "</body>"
puts "</html>"