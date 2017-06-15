require "active_record"
ActiveRecord::Base.establish_connection(host: "127.0.0.1", username: "root", port: 3306, adapter: "mysql2", database: "fintech")
Dir.glob("db/*").each do |file|
    require "./" + file
end