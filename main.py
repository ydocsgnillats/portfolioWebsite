from flask import Flask, render_template, request
app = Flask(__name__)
import reddit, stocks

@app.route('/', methods=['GET', 'POST'])
def homeIndex():
    if request.method == 'POST':
        try:
            username = request.values.get('username')
            email = request.values.get('email')
            password = request.values.get('password')
        except Exception as e:
            print(e)
        return render_template('home.html', username=username,email=email,password=password)
    else:
        return render_template('home.html')
    return render_template('home.html')
    
@app.route('/bridget')
def bridgeIndex():
	return render_template('bridget.html')
    
@app.route('/post', methods=['GET', 'POST'])
def postIndex():
	if request.method == 'POST':
		title = request.values.get('title')
		link = request.values.get('link')
		sub1 = request.values.get('sub1')
		sub2 = request.values.get('sub2')
		sub3 = request.values.get('sub3')
		sub4 = request.values.get('sub4')
		sub5 = request.values.get('sub5')

		bot = reddit.Bot()
		bot.clearSubreddits()
		bot.popSubreddits(sub1, sub2, sub3, sub4, sub5)
		bot.setTitle(title)
		bot.setLink(link)
		pop = bot.getResults()
		bot.post()
		return render_template(
			'post_results.html',
			title=title,link=link,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,pop=pop)
	else:
		return render_template('post.html')
	return render_template('post.html')
    
@app.route('/stocks', methods=['GET', 'POST'])
def stockIndex():
    if request.method == 'POST':
        try:
            stock = request.values.get('stock')
        except Exception as e:
            print(e)
            
        s = stocks.Stocks()
        try:
            search = s.search(stock)
            stock_info = s.get_daily_data(stock)
        except:
            print("Error getting Stock Info")
            
        b = reddit.Bot()
        try:
            redSearch = b.search(stock, "investing", "stocks", "robinhood")
            return render_template('stock_results.html', stock=stock, search = search, redSearch = redSearch, stock_info = stock_info)
        except:
            print("Error performing reddit search")
    else:
        return render_template('stocks.html')
    return render_template('stocks.html')
    
@app.route('/resume')
def resumIndex():
    return render_template('resume.html')
    
@app.route('/login', methods=['GET', 'POST'])
def logIndex():
    if request.method == 'POST':
        flash('Login Succesful!')
        return render_template('login.html', username = username, password = password, email = email)
    else: 
        return render_template('home.html')
    return render_template('home.html')
    
@app.route('/watches')
def watchIndex():
    return render_template('watches.html')

@app.route('/collection')
def collectionIndex():
    return render_template('collection.html')

@app.route('/law')
def lawIndex():
    return render_template('law.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug = True)
