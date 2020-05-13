from flask import Flask, render_template, request
app = Flask(__name__)
import reddit, stocks

@app.route('/')
def homeIndex():
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
        search = s.search(stock)
        return render_template('stock_results.html', stock=stock, search = search)
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

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug = True)
