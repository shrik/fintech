# encoding=utf-8

require "./db.rb"

STOCKS = Stock.all()
STOCK_NAMES = STOCKS.collect(&:symbol)
STOCK_CODES = STOCKS.collect(&:abbrev_symbol)
STOCK_NAME_CODE_MAPPING = {}
STOCKS.each do |stock|
    STOCK_NAME_CODE_MAPPING[stock.symbol] = stock.abbrev_symbol
end
ADVICE_WORDS = %w{谨慎增持  增持 买入 持有 卖出 看好 维持 中性 看淡 减持 }


def with_advice?(line)
    ADVICE_WORDS.each do |word|
        if line.include?(word)
            return true
        end
    end
    return false
end

def get_advice(line)
    ADVICE_WORDS.each do |word|
        if line.include?(word)
            return word
        end
    end
    return false
end

def get_stock(line)
    STOCK_NAMES.each do |stock_name|
        if line.include? stock_name
            return stock_name
        end
    end
    return false
end


Doctext.all().each do |doctext|
    doctext.content.split("\n").each do |line|
        if with_advice?(line)
            advice = get_advice(line)
            stock = get_stock(line)
            if stock
                StockAdvice.create(grade: advice, cooperation_name: stock, line: line, hibor_doc_id: doctext.hibor_doc_id, abbrev_symbol: STOCK_NAME_CODE_MAPPING[stock])
            end
        end
    end
end





