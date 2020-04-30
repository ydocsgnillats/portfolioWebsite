from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homeIndex():
    return render_template('home.html')
    
@app.route('/bridget')
def bridgeIndex():
    return render_template('bridget.html')

@app.route('/post', methods=['GET','POST'])
def postIndex():
    return render_template('post.html')

@app.route('/post_results')
def generate_form():
	title = request.args.get('title')
	link = request.args.get('link')
	sub1 = request.args.get('sub1')
	sub2 = request.args.get('sub2')
	sub3 = request.args.get('sub3')
	sub4 = request.args.get('sub4')
	sub5 = request.args.get('sub5')

	bot = reddit.Bot(title, link)
	bot.clearSubreddits()
	bot.popSubreddits(sub1, sub2, sub3, sub4, sub5)
	pop = bot.getResult()

	return render_template('post_results.html', pop=pop,title=title, link=link, sub1=sub1, sub2=sub2, sub3=sub3, sub4=sub4, sub5=sub5)

@app.route('/movies')
def moviesIndex():
    return render_template('movies.html')
    
@app.route('/stocks')
def stockIndex():
    return render_template('stocks.html')
    
@app.route('/stock_results')
def stockRes(stock):
    return render_template('stock_results.html')
    
if __name__ == '__main__':
    app.run(debug=True)